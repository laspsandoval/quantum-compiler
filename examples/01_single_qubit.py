"""Day 1: a single qubit as a vector."""

import numpy as np

from quantum_compiler.simulator.statevector import apply

# Make a qubit that is OFF.
# OFF → [1, 0]
ket0 = np.array([1, 0], dtype=np.complex128)
# Make a qubit that is ON.
# ON → [0, 1]
ket1 = np.array([0, 1], dtype=np.complex128)
# Create X-gate which is used to flip the switch.
X = np.array([[0, 1], [1, 0]], dtype=np.complex128)
# Flip the switch
flipped_1 = apply(X, ket0)
flipped_2 = apply(X, ket1)

print("|0> =", ket0)
print("|1> =", ket1)
print("X|0> =", flipped_1)
print("X|1> =", flipped_2)

# Create H-gate: puts a qubit into superposition (an equal mix of OFF and ON).
H = 1 / np.sqrt(2) * np.array([[1, 1], [1, -1]], dtype=np.complex128)
superposition = apply(H, ket0)
print("H|0> =", superposition)

back = apply(H, apply(H, ket0))
print("H(H|0>) =", back)
