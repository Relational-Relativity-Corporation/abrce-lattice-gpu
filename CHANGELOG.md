# Changelog -- abrce-lattice-gpu

## v0.1.0 -- initial structure

### Added
- README.md -- scope declared (GPU tile lattice, not NVLink)
- operators/lattice_operators.md -- B_lattice and R_lattice restated,
  reflective boundary declared, open Verifier flag explicit
- docs/roap_declaration_lattice.md -- ROAP five-declaration scaffold
- examples/simulation/simulation_parameters.md -- Sim Parameter Block
- examples/simulation/simulate_lattice.py -- declared, gated on Verifier flag

### Gated
- Lattice simulation: open Verifier flag on R_lattice two-axis restatement
- Lattice detection layer: gated on flag resolution and baseline confirmation

### Open
- ROAP declaration: Origin completion required
- Detection layer: not yet generated
