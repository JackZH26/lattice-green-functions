"""
Compute G_d(0) via the Bessel integral representation:
    G_d(0) = d * ∫₀^∞ e^{-dt} [I₀(t)]^d dt

Usage: python bessel_integral.py [dimension] [decimal_places]
Default: d=4, dps=100
"""
import sys
from mpmath import mp, mpf, quad, besseli, exp

def compute_Gd(d, dps=100):
    mp.dps = dps + 50  # extra guard digits
    integrand = lambda t: exp(-d*t) * besseli(0, t)**d
    # Split integral for better convergence
    result = mpf(0)
    breakpoints = [0, 1, 5, 20, 100, 500]
    for i in range(len(breakpoints)-1):
        result += quad(integrand, [breakpoints[i], breakpoints[i+1]], maxdegree=12)
    # Asymptotic tail
    T = breakpoints[-1]
    from mpmath import pi
    result += 1/(2*pi)**((d-1)/mpf(2)) / (d/2 - 1) / T**(d/2 - 1) if d > 2 else 0
    mp.dps = dps
    return d * result

if __name__ == '__main__':
    d = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    dps = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    print(f"Computing G_{d}(0) to {dps} decimal places...")
    result = compute_Gd(d, dps)
    print(f"G_{d}(0) = {result}")
