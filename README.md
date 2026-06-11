# CHSH

A Python simulation of the CHSH (Clauser-Horne-Shimony-Holt) game comparing classical and quantum strategies. Demonstrates quantum advantage in a non-local game using IBM's Qiskit SDK.

## Background

The CHSH game is a variant of Bell's theorem thought experiment. Two players, Alice and Bob, each receive a random input bit from a referee and must produce an output bit. They win if:

    (alice_output XOR bob_output) == (alice_input AND bob_input)

Players can agree on a strategy beforehand but cannot communicate once the game begins. Classical strategies (local hidden variable theories) cap the win rate at 75%, while quantum entanglement allows a win rate of approximately 85.36% (Tsirelson's bound).

## Results

- Classical win rate: 0.75 (optimal deterministic strategy)
- Quantum win rate: ~0.8536 (Tsirelson's bound)
- Quantum advantage: ~0.1036

## Requirements

- Python 3.11+
- Qiskit 2.x
- NumPy

## Usage

```bash
python core/chsh.py
```

## Project Structure

- `core/chsh.py` -- Entry point that runs both simulations and prints a comparison
- `core/classical_chsh.py` -- Classical CHSH game simulation
- `core/quantum_chsh.py` -- Quantum CHSH game simulation using Qiskit

## License

MIT
