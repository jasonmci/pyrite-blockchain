# test_escrow_contract.py
from pyrite.escrow_contract import EscrowContract

def test_escrow_contract_creation():
    escrow = EscrowContract("Alexandra", "Benjamin", 10)
    assert escrow.buyer == "Alexandra"
    assert escrow.seller == "Benjamin"
    assert escrow.amount == 10
    assert escrow.released == False

def test_escrow_contract_release():
    escrow = EscrowContract("Alexandra", "Benjamin", 10)
    release_message = escrow.release()
    assert release_message == "Alexandra releases 10 coins to Benjamin"
    assert escrow.released == True

def test_escrow_contract_double_release():
    escrow = EscrowContract("Alexandra", "Benjamin", 10)
    escrow.release()
    release_message = escrow.release()
    assert release_message == "Escrow has already been released."
    assert escrow.released == True

def test_escrow_contract_str():
    escrow = EscrowContract("Alexandra", "Benjamin", 10)
    escrow_str = str(escrow)
    assert escrow_str == "Escrow between Alexandra and Benjamin for 10 coins"
