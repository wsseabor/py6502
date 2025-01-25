"""
6502 processor emulator

Whole thing is going to be littered with comments that will function as a readme as you go along in the code
Everything explained in gratuitous detail (for my own purposes)
Hopefully it will read clearly and helpfully
"""

class Memory:
    def __init__(self, size: int = 65536) -> None:
        """
        Memory class for the 6502 processor. Initializes a 'protected' empty list where each index is of uint8 data type
        Sets a list of 'memory' that extends to max value

        @Param size: size of memory, 2^16 or 65536
        @Return: None

        """
        self.size = size
        self._mem = [0] * self.size

    def read(self, addr: int) -> int:
        """
        Reads an address from the memory array

        @Param addr: address index to read
        @Return: int (address of memory to be retrieved)
        """

        #If not between 0 and self.size, raise value error
        if  not 0x0000 <= addr < self.size:
            raise ValueError("Memory address is not valid")
        else:
            return self._mem[addr]

    def write(self, addr: int, value: int) -> None:
        """
        Writes to a specific memory address

        @Param addr: address index to retrieve
        @Param value: value to write at specific memory address
        @Peturn: None
        """

        #Same as the read check
        if not 0x0000 <= addr < self.size:
            raise ValueError("Memory address is not valid")
        #If not between a value of 0 (lowest value of 8 bytes) and 255 (maximum value of 8 bytes)
        if not 0x0000 <= value <= 0xFF:
            raise ValueError("Value too large. Must be of size uint8.")
        else:
            #Write to address
            self._mem[addr] = value

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
        self.flag_n = True #Negative flag
        self.flag_z = True #Zero flag
        self.flag_i = True #Interrupt disable
        self.flag_d = True #Decimal flag
        self.flag_b = True #Break flag
        self.flag_v = True #Overflow flag
        self.flag_c = True #Carry flag

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
        Push data onto stack

        @Return: None
        """

        self.memory[self.stack_pointer] = data
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

    def clear_nop_flag(self) -> None:
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

    def clear_carry_flag(self) -> None:
        """
        CLC - Clear carry flag

        Sets the carry flag to false

        @Return: None
        """

        self.flag_c = False
        self.cycles += 1

    def clear_negative_flag(self) -> None:
        """
        Clear Negative Flag

        Sets the negative flag to false

        @Return: None
        
        """
        self.flag_n = False
        self.cycles += 1

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

    def ins_lda_immediate(self, val: int) -> None:
        """
        LDA - Load data accumulator (with memory)

        When instruction LDA is executed, data is transferred from memory to the accumulator and store therein.

        LDA affects the contents of the accumulator, does not affect the carry or overflow flags; sets the zero flag
        if the accumulator is zero as a result of LDA, otherwise resets the zero flag; set the negative flag if
        bit 7 of the accumulator is 1, otherwise resets the negative flag.

        @Param val: value to be loaded to accumulator
        @Return: None
        """

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



