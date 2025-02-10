import unittest
from py6502 import memory

"""
Homegrown test suite just like mother used to make
"""

class MemTest(unittest.TestCase):
    def setUp(self):

        #Init memory before each test, setUp is unittest's own method
        self.mem = memory.Memory()

    def test_init_memory_size(self) -> None:
        """
        Test memory initalization
    
        @Return: None
        """

        #Test case one
        print(f"Test case one: Default memory init")
        self.size = 65535
        self.size_hex = hex(self.size)
        
        print(f"\nMemory size: {self.mem.size}")
        print(f"\nExpected size: {self.size}")
        self.assertEqual(self.mem.size, self.size)

    def test_read_word(self) -> None:
        """
        Test memory method to read words
        Read byte also tested by way of word read

        @Return: None
        """

        #Test case one
        print("\nTest case One: Read word")
        self.mem.write(0x0000, 0x34)
        self.mem.write(0x0001, 0x12)

        print(f"Wrote bytes: ${self.mem.read_byte(0x0000):02X} (low) ${self.mem.read_byte(0x0001):02X} (high)")
        res = self.mem.read_word(0x0000)
        print(f"Read word: ${res:04X}")
        print(f"Expected: $1234")
        self.assertEqual(res, 0x1234)

        #Test case two
        print("\nTest case two: Read word at end of page")
        self.mem.write(0x00FF, 0x34)
        self.mem.write(0x0100, 0x12)
        
        print(f"Wrote bytes: ${self.mem.read_byte(0x00FF):02X} (low) ${self.mem.read_byte(0x0100):02X} (high)")
        res = self.mem.read_word(0x00FF)
        print(f"Read word: ${res:04X}")
        print(f"Expected: $1234")
        self.assertEqual(res, 0x1234)

        #Test case three 
        print("\nTest case three: Read / write zero value")
        self.mem.write(0x0400, 0x00)
        self.mem.write(0x0401, 0x00)
        print(f"Wrote bytes: ${self.mem.read_byte(0x0400):02X} (low) ${self.mem.read_byte(0x0401):02X} (high)")
        res = self.mem.read_word(0x0400)
        print(f"Read word: ${res:04X}")
        print(f"Expected: 0000")
        self.assertEqual(res, 0x00)

        #Test case four
        print(f"Test case four: Read / write maximum value")
        self.mem.write(0x0500, 0xFF)
        self.mem.write(0x0501, 0xFF)
        print(f"Wrote bytes: ${self.mem.read_byte(0x0500):02X} (low) ${self.mem.read_byte(0x0501):02X} (high)")
        res = self.mem.read_word(0x0500)
        print(f"Read word: ${res:04X}")
        print(f"Expected: $FFFF")
        self.assertEqual(res, 0xFFFF)


if __name__ == "__main__":
    unittest.main(verbosity=2)