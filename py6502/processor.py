from memory import Memory

"""
6502 processor emulator

Whole thing is going to be littered with comments that will function as a readme as you go along in the code
Everything explained in gratuitous detail (for my own purposes)
Hopefully it will read clearly and helpfully
"""

class Processor:
    def __init__(self, memory: Memory) -> None:
        """
        Processor class for the 6502. Boilerplate initializes the memory (from the previous memory class)
        and defines all registers and status flags. Also includes all instruction from the 6502 instruction set.

        Accumulator
        X register
        Y register
        Program Counter
        Stack pointer
        Status flags:

            -Negative
            -Overflow
            -Unused
            -Break
            -Decimal
            -Interrupt disable
            -Zero
            -Carry

        Cycles to keep track of where we are as 6502 is a cycle-accurate processory to rely on precise timing

        Initialize processor class boilerplate

        @Param memory: Memory to use
        @Return: None
        """

        self.memory = memory

        self.reg_a = 0
        self.reg_x = 0
        self.reg_y = 0
        self.program_counter = 0
        self.stack_pointer = 0
        self.cycles = 0

        #Status flags
        self.flag_n = False #Negative flag
        self.flag_z = False #Zero flag
        self.flag_i = True #Interrupt disable
        self.flag_d = False #Decimal flag
        self.flag_b = True #Break flag
        self.flag_v = False #Overflow flag
        self.flag_c = False #Carry flag

    def reset(self) -> None:
        """
        Reset processor to initial state

        Certain values from the 6502 manual are used to reset program counter and stack pointer to their default values
        Certain flags are also set to their default values per the manual

        @Return: None
        """

        self.program_counter = 0xFCE2
        self.stack_pointer = 0x01FD
        self.cycles = 0

        self.flag_i = True
        self.flag_d = False
        self.flag_b = True

    def read_reg_a(self) -> int:
        """
        Read status of the A register

        @Return: int
        """

        self.cycles += 1
        return self.reg_a
    
    def read_reg_x(self) -> int:
        """
        Read status of the X register

        @Return: int
        """

        self.cycles += 1
        return self.reg_x
    
    def read_reg_y(self) -> int:
        """
        Read status of the Y register

        @Return: int
        """

        self.cycles += 1
        return self.reg_y
    
    def push(self, data: int) -> None:
        """
        Push data onto stack and don't bypass memory safety checks ok

        @Return: None
        """

        self.memory.write(self.stack_pointer, data)
        self.stack_pointer -= 1
        self.cycles +=1

    def pop(self) -> int:
        """
        Pop data from stack

        @Return: int
        """

        self.stack_pointer += 1
        self.cycles +=1
        return self.memory[self.stack_pointer - 1]

    def calculate_effective_address(self, mode: str, op: int) -> int:
        """
        Caclulates the effective address of each addressing mode for instructions such as LDA, STA...

        -Absolute (Where the full 16 bit address is provided as an operand, eg. LDA #$42, value $42 is loaded to accumulator)
        -Zero page (Where address is specified as an 8-bit values, within the first 256 bytes of memory 0x0000 -> 0x00FF)
        -Absolute X and Y (Address is calculated by adding the value in the the X or Y register to a 16-bit base address)
        -Zero page X and Y (Address is calculated by adding the value in register X or Y to an 8-bit zero page address)
        -Indirect X and Y (Address is calculated using indexed indirect or indirect indexed addressing)

        @Param mode: Addressing mode
        @Param op: operand

        @Return: int
        """

        if mode == "absolute":
            return op
        elif mode == "zero_page":
            return op & 0xFF
        elif mode == "absolute_x":
            return op + self.reg_x
        elif mode == "absolute_y":
            return op + self.reg_y
        elif mode == "zero_page_x":
            return (op + self.reg_x) & 0xFF
        elif mode == "zero_page_y":
            return (op + self.reg_y) & 0xFF
        else:
            raise ValueError(f"Unsupported addressing mode: {mode}")
        
    def get_cycles_for_mode(self, mode: str) -> int:
        """
        To keep the processor cycle-accurate, values for each addressing mode must be accurate

        Store cycles in a dictionary with key(mode) and value(cycles to be added)

        @Param mode: addressing mode
        @Return: int
        """

        cycles = {
            "absolute" : 4,
            "zero_page" : 3,
            "absolute_x" : 4,
            "absolute_y" : 4,
            "zero_page_x" : 4,
            "zero_page_y" : 4
        }

        return cycles.get(mode, 0)
    
    def ins_nop(self) -> None:
        """
        NOP - No operation

        A special instruction to signify no operation performed
        Rarely used in the instruction set
        NOP instruction represented by opcode 0xEA

        Processor fetches NOP opcode from memory, deceodes and recognizes it as NOP, increments program counter
        to point to next instruction, consumes a small number of cycles (typically 2 in the 6502), and no
        registers or flags are modified

        @Return: None
        """

        self.cycles += 2

    def ins_clc(self) -> None:
        """
        CLC - Clear carry flag

        Sets the carry flag to false

        @Return: None
        """

        self.flag_c = False
        self.cycles += 2

    def ins_cld(self) -> None:
        """
        CLD - Clear decimal mode

        Sets decimal flag to false

        @Return: None
        """
        self.flag_d = False
        self.cycles += 2

    def ins_cli(self) -> None:
        """
        CLI - Clear interrupt disable bit

        Set interrupt flag to false

        @Return: None
        """

        self.flag_i = False
        self.cycles += 2

    def ins_clv(self) -> None:
        """
        CLV - Clear overflow flag

        Set overflow flag to false

        @Return: None
        """

        self.flag_v = False
        self.cycles += 2

    def ins_sec(self) -> None:
        """
        SEC - Set carry flag

        Set carry flag to true

        @Return: None
        """

        self.flag_c = True
        self.cycles += 2

    def ins_sed(self) -> None:
        """
        SED - Set decimal flag

        Set decimal flag to true

        @Return: None
        """

        self.flag_d = True
        self.cycles += 2

    def ins_sei(self) -> None:
        """
        SEI - Set interrupt disable flag

        Set interrupt disable to true

        @Return: None
        """

        self.flag_i = True
        self.cylces += 2

    def ins_lda(self, mode: str, op: int, val: int) -> None:
        """
        LDA - Load data accumulator from memory

        When instruction LDA is executed, data is transferred from memory to the accumulator and stored therein.

        LDA affects the contents of the accumulator, does not affect the carry or overflow flags; sets the zero flag
        if the accumulator is zero as a result of LDA, otherwise resets the zero flag; set the negative flag if
        bit 7 of the accumulator is 1, otherwise resets the negative flag.

        @Param mode: addressing mode to be used
        @Param op: operand
        @Param val: value to be loaded to accumulator
        @Return: None
        """

        """

        *** OLD - immediate only ***

        #Value of accumulator register is stored
        self.reg_a = val

        #If accumulator is zero, set zero flag
        if (self.reg_a == 0):
            self.flag_z = True

        #If bit 7 is 1, set negative flag
        #Performs bitwise & on accumulator comparing reg_a value to 10000000
        #If true, result is just 0x80 again, if false, result is zero
        if (self.reg_a & 0x80):
            self.flag_n = True

        #Cycle increment
        self.cycles += 1
        
        """

        effective_addr = self.calculate_effective_address(mode, op)
        self.reg_a = self.memory.read(effective_addr)

        if (self.reg_a & 0x80):
            self.flag_n = True
        if (self.reg_a == 0):
            self.flag_z = True
        self.cycles += self.get_cycles_for_mode(mode)

    def ins_sta(self, mode: str, op: int) -> None:
        """
        STA - Store contents of accumulator to memory

        Affects none of the flags in the processor status register and does not affect accumulator

        Multiple addressing modes:
            -Absolute (Full 16-bit address is provided as operand)
            -Zero page (Address is specified as an 8-bit value, and refers to the first 256 bytes of memory, addresses 0x0000 to 0x00FF)
            -Absolute X, Y (Address is calculated by adding the value of X or Y register to a 16-bit address)
            -Zero page X, Y (Address is calculated by adding the value or X or Y register to an 8-bit zero pages address)
            -Indirect X, Y (Address is calculated using indexed indirec tof indirect indexed addressing)

        @Param mode: addressing mode
        @Param op: operand
        @Return: None
        """

        effective_addr = self.calculate_effective_address(mode, op)
        self.memory.write(effective_addr, self.reg_a)
        self.cycles += self.get_cycles_for_mode(mode)

    def ins_tax(self) -> None:
        """
        TAX - Transfer accumulator to index x, does not disturb the contents of accumulator
        Implied addressing only

        Only affects the index register x, does not affect carry or overflow flags
        Negative flag is set if bit 7 is 1, otherwise is reset.
        Zero flag is set if the contents of register x is as a result of the operation, otherwise reset

        @Return: None
        """

        self.reg_x = self.reg_a
        if (self.reg_x == 0):
            self.flag_z = True
        if(self.reg_x & 0x80):
            self.flag_n = True
        self.cycles += 2

    def ins_txa(self) -> None:
        """
        TXA - Transfer index x to accumulator without disturbing the contents of the x register

        Does not affect any register other than accumulator and does not affect carry or overflow flag

        If result has bit 7 on, negative flag is set, otherwise reset.
        If the result value in the accumulator is zero, then zero flag is set, otherwise reset. 

        Implied addressing  

        @Return: None
        """

        self.reg_a = self.reg_x
        if (self.reg_a == 0):
            self.flag_z = True
        if (self.reg_a & 0x80):
            self.flag_n = True
        self.cycles += 2

    def ins_tay(self) -> None:
        """
        TAY - Transfer accumulator to index y

        See ins_tax above

        @Return: None
        """

        self.reg_y = self.reg_a
        if (self.reg_y == 0):
            self.flag_z = True
        if(self.reg_y & 0x80):
            self.flag_n = True
        self.cycles += 2

    def ins_tya(self) -> None:
        """
        TYA - transfer index y to accumulator

        See ins_txa above

        @Return: None
        """

        self.reg_a = self.reg_y
        if (self.reg_a == 0):
            self.flag_z = True
        if (self.reg_a & 0x80):
            self.flag_n = True
        self.cycles += 2

    def ins_tsx(self) -> None:
        """
        TSX - transfer stack pointer to index x

        Transfers value in stack pointer to index x
        Does not affect carry or overflow flags

        Sets negative flag if bit 7 is on in index x as a result of instruction, otherwise reset
        Sets zero flag is index x is zero as a result of instruction, otherwise reset

        TSX changes the value of index x, making it equal to the content of the SP

        @Return: None
        """

        self.reg_x = self.stack_pointer

        if (self.reg_x == 0):
            self.flag_z = True
        if (self.reg_x & 0x80):
            self.flag_n = True

        self.cycles += 2

    def ins_txs(self) -> None:
        """
        TXS - transfer index x to stack pointer

        TXS only changes the stack pointer, making it equal to the content of index register x

        Affects no flags

        @Return: None
        """

        self.stack_pointer = self.reg_x
        self.cycles += 2
