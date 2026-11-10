# AGENTS.md

`quantum-compiler` is a personal learning-and-portfolio project: a quantum circuit
simulator and compiler written from scratch in Python. The goal is to understand
compilation deeply enough to work on neutral-atom compiler stacks (Cirq / Superstaq).

**This is a learning project. The owner writes the core algorithms.** When asked for
help, prefer explaining, reviewing, writing tests, and pointing to references over
writing the simulator, decomposer, optimization passes, or router for them, unless
explicitly asked to.

## Roadmap (planned package layout)

| Phase | Months | Deliverable | Planned module |
|---|---|---|---|
| Foundations | 1–3 | State-vector simulator: gates as matrices, measurement sampling | `quantum_compiler/simulator/` |
| Gates & optimization | 3–5 | Single-qubit decomposer to a native gate set; gate-cancellation and commutation passes | `quantum_compiler/gates/`, `quantum_compiler/passes/` |
| Mapping & routing | 5–8 | Own router, benchmarked against Qiskit's SABRE | `quantum_compiler/routing/`, `benchmarks/` |
| Noise-aware / neutral atom | 8–11 | Calibration-aware layout; neutral-atom compilation reproduction or upstream PR | `quantum_compiler/neutral_atom/` |
| Public | 11–12 | Blog series / talk | `docs/` |

Create these modules as each phase starts; don't scaffold empty ones ahead of time.

## Correctness is checked against references

- Every simulator/compiler result must be verified numerically: unitaries via
  `np.testing.assert_allclose` (up to global phase where appropriate), state
  vectors against known textbook outputs (Bell, GHZ, QFT), and, where possible,
  against Qiskit (`qiskit` extra, tests marked `@pytest.mark.qiskit` and using
  `pytest.importorskip("qiskit")`).
- Compiler passes must preserve circuit semantics: test that the output circuit's
  unitary equals the input's up to global phase.
- Use `hypothesis` for property tests (e.g. random unitaries, random circuits).
- Qubit ordering convention must be stated in docstrings. Note Qiskit is
  little-endian (qubit 0 is the least significant bit); be explicit when comparing.

## Environment and commands

Poetry 2.x, local `venv/` (same as the other repos).

```bash
python3 -m venv venv && source venv/bin/activate
poetry install --all-extras        # or --extras "dev test"
pre-commit install                 # once

pytest -n auto                     # full suite
pytest -m "not slow"               # skip benchmarks
pre-commit run --all-files         # ruff, mypy (strict), numpydoc, codespell
```

## Conventions

- Ruff (`ruff check` / `ruff format`) and mypy (`strict = true`, tests excluded)
  are enforced in pre-commit and CI. Config lives in `pyproject.toml`.
- numpydoc docstrings are validated on non-test code (summary, `Parameters`,
  `Returns` with types). Tests are exempt.
- Modern type hints; use `numpy.typing.NDArray[np.complex128]` for states and
  unitaries. Target is `py311`.
- Uppercase names for matrices/gates (`U`, `H`, `CX`) are allowed by the ruff config.
- `logger = logging.getLogger(__name__)`, never `print()` in library code.
  Notebooks and benchmark scripts may print.
- Tests live in `tests/`, mirroring the package layout.

## Gotchas

- Pre-commit blocks direct commits to `main`. Work on a feature branch and open a PR.
- CI runs Linux/macOS/Windows × Python 3.11–3.14.
- Codecov targets 90% patch coverage.
