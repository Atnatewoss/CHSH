from classical_chsh import classical_chsh
from quantum_chsh import quantum_chsh

classical_rate = classical_chsh()
quantum_rate = quantum_chsh()

print(f"Classical Win rate: {classical_rate:.4f}")
print(f"Expected classical maximum: 0.75")

print(f"Quantum win rate: {quantum_rate:.4f}")
print(f"Expected quantum maximum: ~0.8536")


print(f"\nQuantum advantage: {quantum_rate - classical_rate:.4f}")