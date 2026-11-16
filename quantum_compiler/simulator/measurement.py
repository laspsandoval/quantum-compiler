"""Measure state vectors."""

import numpy as np
from numpy.typing import NDArray


def measure(state: NDArray[np.complex128]) -> int:
    """Measure a state vector, collapsing it to a single basis-state outcome.

    Works out the coin's weights but never flips it using Born rule.

    Parameters
    ----------
    state : NDArray[np.complex128]
        State vector of the qubit(s). Entry ``i`` is the amplitude of
        basis state ``|i>``.

    Returns
    -------
    int
        Index of the measured basis state (0 or 1 for a single qubit).
    """
    probs = np.abs(state) ** 2
