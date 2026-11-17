"""Day 2: measuring a qubit many times."""

import numpy as np

from quantum_compiler.simulator.measurement import measure
from quantum_compiler.simulator.statevector import apply

# Qubit that is OFF.
ket0 = np.array([1, 0], dtype=np.complex128)
# H-gate: puts a qubit into an equal mix of OFF and ON.
H = 1 / np.sqrt(2) * np.array([[1, 1], [1, -1]], dtype=np.complex128)

# Build the superposition once; measuring does not change it here.
superposition = apply(H, ket0)

# Measure 1,000 times and count the answers.
zeros = 0
ones = 0
for _ in range(1000):
    if measure(superposition) == 0:
        zeros += 1
    else:
        ones += 1

print("0s:", zeros)
print("1s:", ones)
