# blockchain.py
import time
from hashlib import sha256
import random
from typing import List, Any
from block import Block

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.validators = {"Dillon": 10, "Owen": 15, "Austin": 25, "Jennifer": 50}

    def create_genesis_block(self) -> Block:
        return Block(0, [], "0", 100)

    def add_block(self, block: Block):
        if self.is_valid_block(block):
            self.chain.append(block)
        else:
            print("Block is not valid and could not be added.")

    def is_valid_block(self, block: Block) -> bool:
        previous_block = self.chain[-1]
        if block.previous_hash != previous_block.compute_hash():
            return False
        if block.index != 0 and not self.is_valid_proof(block):
            return False
        return True

    def is_valid_proof(self, block: Block) -> bool:
        block_hash = block.compute_hash()
        return block_hash[:2].isdigit()

    def proof_of_work(self, previous_proof: int) -> int:
        proof = 0
        while not self.is_valid_proof_for_proofs(previous_proof, proof):
            proof += 1
        return proof
    
    def proof_of_stake(self):
        total_stake = sum(self.validators.values())
        stake_threshold = random.uniform(0, total_stake)
        current_stake = 0
        for validator, stake in self.validators.items():
            current_stake += stake
            if current_stake >= stake_threshold:
                return validator
        return None

    def is_valid_proof_for_proofs(self, previous_proof: int, proof: int) -> bool:
        proof_string = f"{previous_proof}{proof}"
        proof_hash = sha256(proof_string.encode()).hexdigest()
        return proof_hash[:2].isdigit()

    def mine_block_pos(self, transactions: List[Any]) -> Block:
        last_block = self.chain[-1]
        validator = self.proof_of_stake()
        new_block = Block(len(self.chain), transactions, last_block.compute_hash(), validator)

        if self.is_valid_block(new_block):
            return new_block
        else:
            print("Block is not valid and could not be added.")
            return None

    def mine_block(self, transactions: List[Any], max_retries: int = 5) -> Block:
        last_block = self.chain[-1]
        retries = 0
        
        while retries < max_retries:
            proof = self.proof_of_work(last_block.proof)
            new_block = Block(len(self.chain), transactions, last_block.compute_hash(), proof)
            
            if self.is_valid_block(new_block):
                return new_block
            else:
                retries += 1
                print(f"Retrying mining... ({retries}/{max_retries})")
        
        print("Failed to mine block after maximum retries.")
        return None
