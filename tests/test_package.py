"""Smoke tests for the package itself."""

import numpy as np

import quantum_compiler


def test_version():
    assert quantum_compiler.__version__


def test_numpy_complex_linear_algebra():
    """Sanity check that the numerical stack behaves as the simulator expects."""
    H = np.array([[1, 1], [1, -1]], dtype=np.complex128) / np.sqrt(2)
    np.testing.assert_allclose(H @ H.conj().T, np.eye(2), atol=1e-12)
