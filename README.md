# pyrite-blockchain

Experiments with blockchain. 

## Installation

```bash
pip install -r requirements.txt
```

## Running examples

```bash
python pow_main.py

python pos_main.py
```

The first one uses proof of work and includes retries if it does not solve the puzzle the first time. 
The second one use proof of stake. Its success rate varies depending upon successful verification of proof, which is fine for this sample. 

## Running tests

```bash
pytest tests
```

Again, illustrating the importance of proof of work and proof of stake, when the proof fails the test fails. Rerunning the tests will eventually result in all tests passing. 

## EscrowContract

A simplistic example of a smart contract that might execute and add a transaction to the ledger

## Tampering

The `pow_main.py` and the `pos_main.py` also have a test inside them that shows what happens when there is tampering with transactions, which is great to see what that really means in terms of a test
