# test_blockchain.py
import pytest
from pyrite.blockchain import Blockchain
from pyrite.block import Block

def test_blockchain_creation():
    blockchain = Blockchain()
    assert len(blockchain.chain) == 1
    assert isinstance(blockchain.chain[0], Block)
    assert blockchain.chain[0].index == 0

def test_blockchain_genesis_block():
    blockchain = Blockchain()
    genesis_block = blockchain.create_genesis_block()
    assert genesis_block.index == 0
    assert genesis_block.transactions == []
    assert genesis_block.previous_hash == "0"
    assert genesis_block.proof == 100

def test_blockchain_is_valid_block_valid():
    blockchain = Blockchain()
    block = Block(1, ["Alice sends 10 coins to Bob"], blockchain.chain[0].compute_hash(), "Alice")
    assert blockchain.is_valid_block(block) == True

def test_blockchain_is_valid_block_invalid_previous_hash():
    blockchain = Blockchain()
    block = Block(1, ["Alice sends 10 coins to Bob"], "invalid_previous_hash", "Alice")
    assert blockchain.is_valid_block(block) == False

def test_blockchain_mine_block():
    blockchain = Blockchain()
    transactions = ["Alice sends 10 coins to Bob"]
    new_block = blockchain.mine_block(transactions)
    assert isinstance(new_block, Block)
    assert new_block.transactions == transactions

def test_blockchain_add_block():
    blockchain = Blockchain()
    transactions = ["Alice sends 10 coins to Bob"]
    new_block = blockchain.mine_block(transactions)
    blockchain.add_block(new_block)
    assert len(blockchain.chain) == 2
    assert blockchain.chain[1].transactions == transactions

def test_blockchain_choose_validator():
    blockchain = Blockchain()
    validator = blockchain.proof_of_stake()
    assert validator in blockchain.validators
