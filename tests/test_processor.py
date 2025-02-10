import unittest
from py6502 import memory
from py6502 import processor


INITIAL_STATE_ON = 1
INITIAL_STATE_OFF = 0
FLAG_ON = True
FLAG_OFF = False

class ProcessorTest(unittest.TestCase):
    def setUp(self):
        self.mem = memory.Memory()
        self.proc = processor.Processor(self.mem)

    def test_proc_init(self):
        """
        Test processor inital state and setup

        @Return: None
        """
        
        print(f"\nTest case 1-1: Processor inital state")
        self.assertEqual(self.proc.reg_a, INITIAL_STATE_OFF)
        self.assertEqual(self.proc.reg_x, INITIAL_STATE_OFF)
        self.assertEqual(self.proc.reg_y, INITIAL_STATE_OFF)
        self.assertEqual(self.proc.flag_b, FLAG_ON)
        self.assertEqual(self.proc.flag_c, FLAG_OFF)
        self.assertEqual(self.proc.flag_d, FLAG_OFF)
        self.assertEqual(self.proc.flag_i, FLAG_ON)
        self.assertEqual(self.proc.flag_n, FLAG_OFF)
        self.assertEqual(self.proc.flag_v, FLAG_OFF)
        self.assertEqual(self.proc.flag_z, FLAG_OFF)


if __name__ == "__main__":
    unittest.main(verbosity=2)