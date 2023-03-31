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
The second one use proof of stake. Its success rate varies depending upon successfull verification of proof, which is fine for this sample. 

## Running tests

```bash
pytest tests
```

Again, illustrating the importance of proof of work and proof of stake, when the proof fails the test fails. Rerunning the tests will eventually result in all tests passing. 
