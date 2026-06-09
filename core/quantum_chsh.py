import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

def quantum_chsh(num_rounds=10000):
  wins = 0

  # CHSH optmial angles
  alice_angles = [0, np.pi/2]
  bob_angles = [np.pi/4, -np.pi/4]
  
  for _ in range(num_rounds):
    # Referee sends random bits
    alice_input = np.random.randint(0, 2)
    bob_input = np.random.randint(0, 2)

    # Create entangled pair (Bell state)
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)

    # Rotate to measurement basis
    qc.ry(alice_angles[alice_input], 0)
    qc.ry(bob_angles[bob_input], 1)

    # Get probabilities from statevector
    sv = Statevector.from_label('00')
    sv = sv.evolve(qc)
    probs = sv.probabilities()

    # Get measurement outcome
    outcome = np.random.choice([0, 1, 2, 3], p=probs)
    
    alice_output = (outcome >> 1) & 1
    bob_output = outcome & 1

    # Win condition
    if (alice_output ^ bob_output) == (alice_input & bob_input):
      wins += 1

  return wins / num_rounds

# quantum_rate = quantum_chsh()
# print(f"Quantum win rate: {quantum_rate}:.4f")
# print(f"Expected quantum maximum: ~0.8536")