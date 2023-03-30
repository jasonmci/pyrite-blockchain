import time
from hashlib import sha256
from typing import List, Any


class Block:
    def __init__(self, index: int, transactions: List[Any], previous_hash: str, proof: str):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.proof = proof

    def compute_hash(self) -> str:
        block_string = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.proof}"
        return sha256(block_string.encode()).hexdigest()
