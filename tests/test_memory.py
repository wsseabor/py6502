from py6502 import memory

def test(size: int) -> None:
    mem = memory.Memory(size)
    assert len(mem._mem) == size

test(0)

