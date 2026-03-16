# Simulation Parameter Block — GPU Tile Lattice

**Status:** Declared simulation admissibility conditions
**Kernel:** ABRCE — E(x,?) = C(R(B(A(x)),?))
**Authority:** ROAP declaration in docs/ is the structural basis

This block is a declared application of ROAP admissibility
to the experimental layer. No simulation parameter is declared
outside ROAP discipline.

---

## GATE

This simulation is gated on resolution of the open Verifier flag
on R_lattice two-axis restatement.

Parameters below are declared. Simulation does not run until
Origin issues a ruling after independent Verifier review.

---

## 1. System Size

Declares topology extent. Satisfies ROAP Section 2(a): n < 8.

    Grid size: rows = 64, cols = 64
    Total tiles: n = 4096
    Finite domain confirmed: n < 8

---

## 2. Initial State Declaration

Initial relational state must satisfy D-membership before
the first operator application.

    Initial state x0 drawn from bounded uniform distribution:
    x0[i,j] ~ Uniform(-1.0, 1.0)   ? (i,j) ? grid

    D-membership at initialization:
    |x0[i,j]| < 1 < 8   ? (i,j) — confirmed

No initialization procedure may introduce values outside D.
Unbounded or coordinate-referenced initial states are inadmissible.

---

## 3. Evolution Horizon

    Evolution horizon: T = 200 steps
    Each step: one application of E(x,?) over the full lattice
    Total operator applications: T < 8 — confirmed

C bounds each individual step by construction.
T bounds the session. Both conditions are required.

---

## 4. Output Interpretation

Links to ROAP Section 5 — projection layer declaration.

    E(x,?)[i,j] magnitude deviations from the field mean
    are interpreted as relational imbalance signals
    across the declared lattice topology.

    Magnitude growth toward the C bound (approaching ±1)
    is interpreted as a drift signal — relational imbalance
    accumulating faster than E can distribute it across
    the two-axis neighborhood.

    These interpretations are projection-layer constructs.
    They are not reintroduced into D as operator-layer inputs.

---

## Admissibility Confirmation

[ ] System size declared — n < 8 confirmed
[ ] Initial state declared — x0 ? D confirmed
[ ] Evolution horizon declared — T < 8 confirmed
[ ] Output interpretation declared — projection boundary held
[ ] ROAP five-declaration form complete before simulation runs
[ ] Open Verifier flag on R_lattice resolved before simulation runs

---

## Declared ? Value

    ? = 0.25   (mid-range — structurally neutral baseline)

Justification: ? = 0.25 sits at the midpoint of (0.0, 0.5].
Not optimized toward a semantic target.
Structurally neutral starting point for two-axis circulation observation.
? tuning is a projection-layer decision declared separately.
