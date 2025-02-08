class Memory:
    def __init__(self, size: int = 65535) -> None:
        """
        Memory class for the 6502 processor. Initializes a 'protected' empty list where each index is of uint8 data type
        Sets a list of 'memory' that extends to max value

        @Param size: size of memory, 2^16 - 1 or 65535
        @Return: None

        """
        self.size = size
        self._mem = [0] * self.size

    def read_byte(self, addr: int) -> int:
        """
        Reads a byte address from the memory array

        @Param addr: address index to read
        @Return: int (byte in memory to be retrieved)
        """

        #If not between 0 and self.size, raise value error
        if  not 0x0000 <= addr < self.size:
            raise ValueError("Memory address is not valid")
        else:
            return self._mem[addr]
        
    def read_word(self, addr: int) -> int:
        """
        Reads a word (2 byte) address from the memory array

        Accounting for little-endian, the first byte read will be the low_byte, high_byte will be second byte 
        to be read, concatenate them both by shifting the high byte left by 8 and using bitwise OR to finish

        @Param addr: address index to read
        @Return: int (word in memory to be retrieved)
        """

        low_byte = self.read_byte(addr)
        high_byte = self.read_byte(addr + 1)
        return (high_byte << 8) | low_byte
        
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