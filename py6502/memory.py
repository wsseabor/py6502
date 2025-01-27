

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