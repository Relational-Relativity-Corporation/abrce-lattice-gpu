# Upstream Relationships -- abrce-lattice-gpu

## Structural Authority

### Invariant Relational Kernel
Repository: Invariant_Relational_Kernel_ABRCE
Relationship: kernel authority
Operators A, B, R, C, E are defined there.
Nothing in this repository modifies the kernel.
If any document here conflicts with the kernel, the kernel takes precedence.

### ABRCE-ROAP
Repository: ABRCE-ROAP
Relationship: protocol authority
All ROAP declarations in docs/ implement the five-declaration
protocol specified in ABRCE-ROAP/docs/roap.md.
The lattice topology in this repository directly extends:
  ABRCE-ROAP/examples/lattice-topology/declaration.md

The open Verifier flag declared in that example is carried
forward here and gates all simulation and detection work.

## Downstream
This repository produces no downstream dependents at v0.1.0.
