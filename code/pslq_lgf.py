"""
PSLQ search for closed-form expressions of G_4(0).

Project #003: Lattice Green Functions
Author: Jian Zhou
Date: 2026-03-18
"""

from mpmath import (mp, mpf, pi, sqrt, gamma, log, nstr, 
                    ellipk, catalan, euler, zeta, pslq)
import time


def load_G4(dps=500):
    """Load precomputed G_4(0) value."""
    mp.dps = dps + 20
    with open('../data/G4_500dps.txt', 'r') as f:
        val = mpf(f.read().strip())
    mp.dps = dps
    return +val


def build_basis_level0(G4, dps=200):
    """Level 0: Check if G4 is algebraic (low degree)."""
    mp.dps = dps
    powers = [G4**k for k in range(20)]
    return powers, [f"G4^{k}" for k in range(20)]


def build_basis_level1(G4, dps=200):
    """Level 1: Classical constants."""
    mp.dps = dps
    
    constants = {
        '1': mpf(1),
        'G4': G4,
        'pi': pi,
        'pi^2': pi**2,
        'pi^3': pi**3,
        'pi^4': pi**4,
        'ln2': log(2),
        'zeta3': zeta(3),
        'zeta5': zeta(5),
        'Ga14': gamma(mpf(1)/4),
        'Ga13': gamma(mpf(1)/3),
        'Ga16': gamma(mpf(1)/6),
        'sqrt2': sqrt(2),
        'sqrt3': sqrt(3),
    }
    
    names = list(constants.keys())
    vals = [constants[n] for n in names]
    return vals, names


def build_basis_level2(G4, dps=200):
    """Level 2: Gamma products and elliptic integrals at singular moduli."""
    mp.dps = dps
    
    Ga14 = gamma(mpf(1)/4)
    Ga13 = gamma(mpf(1)/3)
    Ga16 = gamma(mpf(1)/6)
    
    # Singular moduli for K(k)
    # k_1 = 1/sqrt(2) → K(1/2) = Γ(1/4)²/(4√π)
    # k_3 = (√6-√2)/4
    k1sq = mpf(1)/2
    k3 = (sqrt(6) - sqrt(2)) / 4
    k3sq = k3**2
    
    K_k1 = ellipk(k1sq)
    K_k3 = ellipk(k3sq)
    
    constants = {
        '1': mpf(1),
        'G4': G4,
        'pi': pi,
        'pi^2': pi**2,
        'K(k1)': K_k1,
        'K(k1)^2': K_k1**2,
        'K(k3)': K_k3,
        'K(k3)^2': K_k3**2,
        'K(k1)*K(k3)': K_k1 * K_k3,
        'Ga14^2/pi': Ga14**2 / pi,
        'Ga14^4/pi^3': Ga14**4 / pi**3,
        'Ga13^3/pi': Ga13**3 / pi,
        'sqrt2': sqrt(2),
        'sqrt3': sqrt(3),
        'sqrt6': sqrt(6),
    }
    
    names = list(constants.keys())
    vals = [constants[n] for n in names]
    return vals, names


def build_basis_level2b(G4, dps=200):
    """Level 2b: Multiplicative PSLQ on log(G4)."""
    mp.dps = dps
    
    constants = {
        'lnG4': log(G4),
        'ln_pi': log(pi),
        'ln2': log(2),
        'ln3': log(3),
        'lnGa14': log(gamma(mpf(1)/4)),
        'lnGa13': log(gamma(mpf(1)/3)),
        '1': mpf(1),
    }
    
    names = list(constants.keys())
    vals = [constants[n] for n in names]
    return vals, names


def build_basis_level3(G4, dps=200):
    """Level 3: K(k)^3, mixed products, Catalan constant."""
    mp.dps = dps
    
    k1sq = mpf(1)/2
    K_k1 = ellipk(k1sq)
    
    constants = {
        '1': mpf(1),
        'G4': G4,
        'pi': pi,
        'pi^2': pi**2,
        'K(k1)^2': K_k1**2,
        'K(k1)^3': K_k1**3,
        'Catalan': catalan,
        'zeta3': zeta(3),
        'G4*pi': G4 * pi,
        'G4*pi^2': G4 * pi**2,
        'G4^2': G4**2,
    }
    
    names = list(constants.keys())
    vals = [constants[n] for n in names]
    return vals, names


def run_pslq_search(vals, names, dps=200, maxcoeff=1000, label=""):
    """Run PSLQ and report results."""
    mp.dps = dps
    
    print(f"\n{'='*60}")
    print(f"PSLQ Search: {label}")
    print(f"  Basis dimension: {len(vals)}")
    print(f"  Precision: {dps} dps")
    print(f"  Max coefficient: {maxcoeff}")
    print(f"  Basis: {', '.join(names)}")
    print(f"{'='*60}")
    
    t0 = time.time()
    try:
        rel = pslq(vals, maxcoeff=maxcoeff, maxsteps=10000)
    except Exception as e:
        print(f"  PSLQ error: {e}")
        return None
    elapsed = time.time() - t0
    
    if rel is None:
        print(f"  Result: NO RELATION FOUND [{elapsed:.2f}s]")
        return None
    else:
        print(f"  Result: RELATION FOUND! [{elapsed:.2f}s]")
        print(f"  Coefficients: {rel}")
        # Format the relation
        terms = []
        for coeff, name in zip(rel, names):
            if coeff != 0:
                terms.append(f"({coeff})*{name}")
        print(f"  Relation: {' + '.join(terms)} = 0")
        
        # Verify
        check = sum(c * v for c, v in zip(rel, vals))
        print(f"  Verification: |sum| = {nstr(abs(check), 10)}")
        return rel


if __name__ == "__main__":
    DPS = 400  # use 400 of our 500 available digits
    
    print("Loading G_4(0) at 500 dps...")
    G4 = load_G4(dps=DPS + 50)
    mp.dps = DPS
    G4 = +G4
    print(f"G_4(0) = {nstr(G4, 50)}...")
    
    # Level 0: Algebraic check
    print("\n\n### LEVEL 0: Algebraic number check ###")
    vals, names = build_basis_level0(G4, dps=DPS)
    run_pslq_search(vals[:10], names[:10], dps=DPS, maxcoeff=10000, 
                    label="Algebraic degree <= 9")
    
    # Level 1: Classical constants
    print("\n\n### LEVEL 1: Classical constants ###")
    vals, names = build_basis_level1(G4, dps=DPS)
    run_pslq_search(vals, names, dps=DPS, maxcoeff=1000,
                    label="Classical constants (14-dim)")
    
    # Level 2: Gamma products + elliptic integrals
    print("\n\n### LEVEL 2: Gamma products + K(k) ###")
    vals, names = build_basis_level2(G4, dps=DPS)
    run_pslq_search(vals, names, dps=DPS, maxcoeff=1000,
                    label="Gamma products + K(k) (15-dim)")
    
    # Level 2b: Multiplicative PSLQ
    print("\n\n### LEVEL 2b: Multiplicative PSLQ ###")
    vals, names = build_basis_level2b(G4, dps=DPS)
    run_pslq_search(vals, names, dps=DPS, maxcoeff=1000,
                    label="Multiplicative (log space, 7-dim)")
    
    # Level 3: K(k)^3 and mixed
    print("\n\n### LEVEL 3: K(k)^3 + mixed ###")
    vals, names = build_basis_level3(G4, dps=DPS)
    run_pslq_search(vals, names, dps=DPS, maxcoeff=1000,
                    label="K(k)^3 + mixed (11-dim)")
    
    # Bonus: search G4^2 and 1/G4
    print("\n\n### BONUS: G4^2 and 1/G4 variants ###")
    mp.dps = DPS
    for transform, tname in [(G4**2, "G4^2"), (1/G4, "1/G4"), (G4*pi, "G4*pi"), (G4*pi**2, "G4*pi^2")]:
        vals = [mpf(1), transform, pi, pi**2, gamma(mpf(1)/4)**4/pi**3, 
                gamma(mpf(1)/3)**3/pi, sqrt(2), sqrt(3), zeta(3)]
        names_t = ['1', tname, 'pi', 'pi^2', 'Ga14^4/pi^3', 'Ga13^3/pi', 'sqrt2', 'sqrt3', 'zeta3']
        run_pslq_search(vals, names_t, dps=DPS, maxcoeff=1000,
                       label=f"Transform: {tname} (9-dim)")
    
    print("\n\nDone. All results logged above.")
