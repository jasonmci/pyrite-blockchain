# test_block.py
import time
from block import Block

def test_block_creation():
    block = Block(0, [], "0000000000000000000000000000000000000000000000000000000000000000", "Alice")
    assert block.index == 0
    assert block.transactions == []
    assert block.previous_hash == "0000000000000000000000000000000000000000000000000000000000000000"
    assert block.proof == "Alice"

def test_block_timestamp():
    block = Block(0, [], "0000000000000000000000000000000000000000000000000000000000000000", "Alice")
    current_time = time.time()
    assert abs(block.timestamp - current_time) < 0.1

def test_block_compute_hash():
    block = Block(0, [], "0000000000000000000000000000000000000000000000000000000000000000", "Alice")
    computed_hash = block.compute_hash()
    assert len(computed_hash) == 64
