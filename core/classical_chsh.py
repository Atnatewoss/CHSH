import numpy as np

def classical_chsh(num_rounds=10000):
  wins = 0
  for _ in range(num_rounds):
    # Referee sends random bits to Alice and Bob
    alice_input = np.random.randint(0, 2)
    bob_input = np.random.randint(0, 2)

    # Best classical strategy: always output 0
    alice_output = 0
    bob_output = 0

    # Win condition: alice XOR bob = alice and bob
    if (alice_output ^ bob_output) == (alice_input & bob_input):
      wins += 1

  return wins / num_rounds
