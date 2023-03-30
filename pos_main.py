from typing import List, Any
from block import Block
from blockchain import Blockchain
from escrow_contract import EscrowContract

def test_tampering(blockchain: Blockchain):
    print("\nTampering with transactions test:")

    # Tamper with a transaction in Block 1
    original_transaction = blockchain.chain[1].transactions[0]
    print(f"\nOriginal transaction in Block 1: {original_transaction}")
    tampered_transaction = "Alexandra sends 15 coins to Benjamin"
    blockchain.chain[1].transactions[0] = tampered_transaction
    print(f"Tampered transaction in Block 1: {tampered_transaction}")

    # Check the validity of the blockchain after tampering
    is_valid = True
    for i in range(1, len(blockchain.chain)):
        if not blockchain.is_valid_block(blockchain.chain[i]):
            print(f"Block {i} is invalid after tampering.")
            is_valid = False
            break

    if is_valid:
        print("The blockchain is still valid after tampering.")
    else:
        print("The blockchain is invalid after tampering.")
    
    # Revert the tampering to restore the blockchain's validity
    blockchain.chain[1].transactions[0] = original_transaction
    print(f"Reverted transaction in Block 1: {original_transaction}")


def main():
    # Initialize a new blockchain
    blockchain = Blockchain()

    # Add some transactions and mine a new block
    transactions = ["Alexandra sends 10 coins to Benjamin", "Benjamin sends 5 coins to Caroline"]
    new_block = blockchain.mine_block_pos(transactions)
    if new_block:
        blockchain.add_block(new_block)
        print("Block 1 added to the blockchain")
    else:
        print("Failed to mine Block 1")

    # Add more transactions and mine another block
    transactions = ["Caroline sends 2 coins to Dave", "Dave sends 1 coin to Alexandra"]
    new_block = blockchain.mine_block_pos(transactions)
    if new_block:
        blockchain.add_block(new_block)
        print("Block 2 added to the blockchain")
    else:
        print("Failed to mine Block 2")


    # Create an escrow contract between Alexandra and Benjamin
    escrow = EscrowContract("Alexandra", "Benjamin", 10)
    print(f"\nCreated escrow contract: {escrow}")

    # Add the escrow contract to a new block and mine it
    transactions = [str(escrow)]
    new_block = blockchain.mine_block_pos(transactions)
    if new_block:
        blockchain.add_block(new_block)
        print("Block 3 added to the blockchain")
    else:
        print("Failed to mine Block 3")
        
    # Simulate the release of escrow funds when Alexandra confirms the receipt of goods
    release_transaction = escrow.release()
    print(f"\n{release_transaction}")

    # Add the release transaction to a new block and mine it
    transactions = [release_transaction]
    new_block = blockchain.mine_block_pos(transactions)
    if new_block:
        blockchain.add_block(new_block)
        print("Block 4 added to the blockchain")
    else:
        print("Failed to mine Block 4")
        

    # Display the entire blockchain
    print("\nBlockchain:")
    for i, block in enumerate(blockchain.chain):
        print(f"Block {i}: {block.compute_hash()}")

    # Test tampering with transactions
    test_tampering(blockchain)

if __name__ == "__main__":
    main()
