# -*- coding: utf-8 -*-
# simulate_lattice.py
#
# Simulation Parameter Block:
#   Grid size:         rows=64, cols=64 (n=4096)
#   Initial state:     x0 ~ Uniform(-1, 1), |x0[i,j]| < 1
#   Evolution horizon: T = 200 steps
#   rho:               0.25
#   Output interp:     Origin declaration required
#
# OPEN VERIFIER FLAG:
# R_lattice two-axis restatement pending independent Verifier review.
# File declared but not executed until flag is resolved.

import numpy as np
import matplotlib.pyplot as plt

ROWS     = 64
COLS     = 64
N        = ROWS * COLS
T        = 200
RHO      = 0.25
RNG_SEED = 42

def _nbrs(x):
    up    = np.roll(x, -1, axis=0);  up[-1, :]    = x[-1, :]
    down  = np.roll(x,  1, axis=0);  down[0, :]   = x[0, :]
    right = np.roll(x, -1, axis=1);  right[:, -1] = x[:, -1]
    left  = np.roll(x,  1, axis=1);  left[:, 0]   = x[:, 0]
    return up, down, right, left

def operator_a(x):
    return x - np.mean(x)

def operator_b(x):
    up, down, right, left = _nbrs(x)
    return x + up + down + right + left

def operator_r(x, rho):
    # OPEN VERIFIER FLAG -- two-axis restatement pending review
    up, down, right, left = _nbrs(x)
    return x + rho * ((up - down) + (right - left))

def operator_c(x):
    return x / (1.0 + np.abs(x))

def operator_e(x, rho):
    return operator_c(operator_r(operator_b(operator_a(x)), rho))

rng = np.random.default_rng(RNG_SEED)
x0  = rng.uniform(-1.0, 1.0, size=(ROWS, COLS))
assert np.all(np.abs(x0) < 1.0), "Initial state violates D-membership"

history = np.zeros((T + 1, ROWS, COLS))
history[0] = x0
x = x0.copy()
for t in range(T):
    x = operator_e(x, RHO)
    history[t + 1] = x

print("=== Lattice Simulation -- Baseline Verification ===")
print(f"  rows={ROWS}, cols={COLS}, n={N}, T={T}, rho={RHO}")
max_mag = np.max(np.abs(history))
print(f"  Max magnitude: {max_mag:.6f}")
print(f"  D-membership preserved: {max_mag < 1.0}")
a0 = operator_a(x0)
print(f"  A zero-sum at step 0: {np.abs(np.sum(a0)):.2e}")
means = np.mean(history.reshape(T+1,-1), axis=1)
print(f"  Field mean step 0: {means[0]:.6f}  step {T}: {means[T]:.6f}")
print()
print("  NOTE: Verifier flag on R_lattice -- confirm resolved before")
print("  treating output as admissible.")

mean_mag = np.mean(np.abs(history.reshape(T+1,-1)), axis=1)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].plot(mean_mag)
axes[0].set_xlabel('Step (t)')
axes[0].set_ylabel('Mean |E(x,rho)|')
axes[0].set_title('Mean Magnitude Over Time')
axes[0].set_ylim(0, 1.0)
im = axes[1].imshow(history[T], cmap='RdBu_r', vmin=-1.0, vmax=1.0)
plt.colorbar(im, ax=axes[1], label='E(x,rho)[i,j]')
axes[1].set_title(f'Final State -- {ROWS}x{COLS}, T={T}, rho={RHO}')
plt.tight_layout()
plt.savefig('lattice_evolution.png', dpi=150)
plt.close()
print("  Output saved: lattice_evolution.png")
