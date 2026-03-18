# Lattice Green Functions in d ≥ 4

**Paper:** *Lattice Green Functions in d ≥ 4: A Domb Number Decomposition and the Absence of Classical Closed Forms*
**Author:** Jian Zhou (jackzhou.sci@gmail.com)

## Overview

This repository contains the computational code and data for our study of lattice Green functions (LGF) on the simple cubic lattice in dimensions d ≥ 4.

### Key Results

1. **Domb Number Decomposition:** The 4D walk numbers factor as c_n = C(2n,n) · D_n, where D_n are Domb numbers (OEIS A002895)
2. **Hadamard Product:** Sol(AESZ #16) = Had(1/√(1-4z), Sol(AESZ #34))
3. **High-Precision Values:** G₄(0) computed to 999 decimal places, G₅–G₇ to 500 places
4. **PSLQ Exclusion:** Systematic exclusion of all classical closed-form candidates for G₄(0)

### G₄(0) First 50 Digits
```
1.23946712184848171267869766485900071015328906916175...
```

## Repository Structure

```
paper/                          # LaTeX source and compiled PDF
code/scripts/
  bessel_integral.py           # Bessel integral computation of G_d(0)
  recurrence_walk.py           # Walk numbers, Domb numbers, Richardson extrapolation
  pslq_search.py               # PSLQ integer relation searches
data/
  G4_500dps.txt                # G₄(0) to 500 decimal places
  G4_1000dps.txt               # G₄(0) to 999 decimal places
```

## Requirements

- Python 3.8+
- [mpmath](https://mpmath.org/) (`pip install mpmath`)
- matplotlib (for plots)

## Usage

```bash
# Compute G_4(0) to 100 digits
python code/scripts/bessel_integral.py 4 100

# Verify Domb decomposition
python code/scripts/recurrence_walk.py

# Run PSLQ searches
python code/scripts/pslq_search.py
```

## License

MIT License

## Citation

If you use this code or data, please cite:
```
J. Zhou, "Lattice Green Functions in d ≥ 4: A Domb Number Decomposition
and the Absence of Classical Closed Forms," 2026.
```
