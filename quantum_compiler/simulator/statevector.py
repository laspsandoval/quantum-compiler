"""Apply gates to state vectors."""

import numpy as np
from numpy.typing import NDArray


def apply(
    gate: NDArray[np.complex128], state: NDArray[np.complex128]
) -> NDArray[np.complex128]:
    """Apply a gate to a state vector.

    Parameters
    ----------
    gate : NDArray[np.complex128]
        Square matrix for the gate.
    state : NDArray[np.complex128]
        State vector of the qubit(s).

    Returns
    -------
    NDArray[np.complex128]
        The new state after the gate.
    """
    return gate @ state
