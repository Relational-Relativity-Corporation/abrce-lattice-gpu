# Lattice Topology — Operator Restatement

**Topology:** 2D lattice, von Neumann 4-connectivity
**ROAP topology check:** non-canonical — B and R restated below
**Boundary:** reflective
**Kernel authority:** Invariant_Relational_Kernel_ABRCE

---

## OPEN VERIFIER FLAG

The two-axis antisymmetric circulation restatement of R_lattice
is flagged as a structurally novel condition relative to the
canonical ring and graph cases.

This restatement is pending independent Verifier review
before any implementation proceeds.

Source: ABRCE-ROAP/examples/lattice-topology/declaration.md

No implementation of R_lattice should proceed until Origin
issues a ruling after Verifier review.

---

## Index Structure

Tiles indexed as (i, j) where:
    i ? {0, ..., rows-1}
    j ? {0, ..., cols-1}

Flattened to 1D index: k = i · cols + j

---

## Neighborhood Declaration

Von Neumann 4-connectivity:

    N(i,j) = { (i+1,j), (i-1,j), (i,j+1), (i,j-1) }

Boundary condition: reflective

    At edge i=0:      neighbor (i-1,j) ? reflected to (i,j)
    At edge i=rows-1: neighbor (i+1,j) ? reflected to (i,j)
    At edge j=0:      neighbor (i,j-1) ? reflected to (i,j)
    At edge j=cols-1: neighbor (i,j+1) ? reflected to (i,j)

Reflective boundary substitutes the tile itself for the
out-of-bounds neighbor. This preserves finite index access
at all boundary positions.

---

## Restated Operators

B_lattice(x)[i,j] =
    x[i,j]
    + x[i+1,j]    (or x[i,j] if i = rows-1)
    + x[i-1,j]    (or x[i,j] if i = 0)
    + x[i,j+1]    (or x[i,j] if j = cols-1)
    + x[i,j-1]    (or x[i,j] if j = 0)

R_lattice(x)[i,j] =     [OPEN VERIFIER FLAG — see above]
    x[i,j]
    + ? · [ (x[i+1,j] - x[i-1,j])     (row-axis circulation)
           + (x[i,j+1] - x[i,j-1]) ]   (col-axis circulation)

    Boundary substitution applies per the reflective rule above.
    ? ? (0.0, 0.5] — required for D-membership preservation.

---

## Admissibility Confirmation

1. Finite neighborhood reach:        N(i,j) = 4 neighbors — confirmed
2. Bounded index access:             reflective boundary declared — confirmed
3. Antisymmetric circulation in R:   two-axis (row/col) difference — OPEN FLAG
4. D-membership preservation:        C applied in E — confirmed

Condition 3 carries the open Verifier flag declared above.
Admissibility of the full restatement is conditional on
Verifier review and Origin ruling.
