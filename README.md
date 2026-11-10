# quantum-compiler

A quantum circuit simulator and compiler, written from scratch in Python. It covers
state-vector simulation, gate decomposition, optimization passes, and qubit
mapping/routing benchmarked against Qiskit's SABRE, and then moves on to noise-aware
and neutral-atom compilation.

## Development

```bash
python3 -m venv venv
source venv/bin/activate
poetry install --all-extras
pre-commit install
pytest -n auto
```

See [AGENTS.md](AGENTS.md) for the roadmap and conventions.
