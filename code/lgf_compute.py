"""
Lattice Green Function (LGF) high-precision computation.

G_d(0) for d-dimensional hypercubic lattice using Bessel integral representation:
    G_d(0) = ∫₀^∞ e^{-dt} [I₀(t)]^d dt

Project #003: Closed-Form Expressions for Higher-Dimensional LGFs
Author: Jian Zhou
Date: 2026-03-18
"""

from mpmath import mp, mpf, besseli, exp, quad, inf, pi, sqrt, gamma, log10, nstr
import time


def lgf_bessel(d, dps=100, verbose=True):
    """
    Compute G_d(0) using the Bessel integral representation.
    
    G_d(0) = ∫₀^∞ e^{-dt} [I₀(t)]^d dt
    
    Parameters:
        d: dimension (integer >= 2)
        dps: decimal places of precision
        verbose: print progress info
    
    Returns:
        G_d(0) as mpf
    """
    mp.dps = dps + 50  # extra guard digits
    
    def integrand(t):
        return exp(-d * t) * besseli(0, t) ** d
    
    if verbose:
        t0 = time.time()
        print(f"Computing G_{d}(0) via Bessel integral at {dps} dps...")
    
    result = quad(integrand, [0, inf], error=True)
    val = result[0] if isinstance(result, tuple) else result
    
    mp.dps = dps
    val = +val  # round to target precision
    
    if verbose:
        elapsed = time.time() - t0
        print(f"  Done in {elapsed:.1f}s")
        print(f"  G_{d}(0) = {nstr(val, 50)}...")
    
    return val


def lgf_bessel_optimized(d, dps=100, verbose=True):
    """
    Optimized Bessel integral using series expansion for I₀(t).
    
    I₀(t) = Σ_{k=0}^∞ (t/2)^{2k} / (k!)²
    
    For large t, use asymptotic: I₀(t) ~ e^t / √(2πt)
    So e^{-dt} I₀(t)^d ~ e^{-dt} e^{dt} / (2πt)^{d/2} = 1/(2πt)^{d/2}
    Actually the integrand decays for d >= 3 since e^{-dt} I₀(t)^d → 0.
    """
    mp.dps = dps + 50
    
    if verbose:
        t0 = time.time()
        print(f"Computing G_{d}(0) via optimized Bessel integral at {dps} dps...")
    
    # For moderate precision, split integral at a cutoff
    # The integrand peaks near t ~ 1/(2(d-1)) approximately
    # Use adaptive quadrature with hints
    result = quad(lambda t: exp(-d * t) * besseli(0, t) ** d, 
                  [0, 1, 5, 20, inf])
    
    mp.dps = dps
    val = +result
    
    if verbose:
        elapsed = time.time() - t0
        print(f"  Done in {elapsed:.1f}s")
        print(f"  G_{d}(0) = {nstr(val, 50)}...")
    
    return val


def lgf_series_4d(dps=100, nterms=None, verbose=True):
    """
    Compute G_4(0) using the binomial coefficient series.
    
    G_4(0) = Σ_{n=0}^∞ a_n  where a_n = [Σ_{k=0}^n C(2k,k)² C(2(n-k),n-k)² / 16^n] * (1/16^n)
    
    Actually: a_n = (1/16^n) * Σ_{k=0}^n C(2k,k)² C(2(n-k),n-k)²  ... needs verification from Guttmann.
    
    Alternative: use the known formula
    G_4(0) = Σ_{n=0}^∞ [C(2n,n)/4^n]^4  (to be verified)
    
    For now, use the Bessel moment representation:
    G_4(0) = Σ_{n=0}^∞ c_n  where c_n = [C(2n,n)/4^n]^4
    
    Note: This formula needs verification against literature.
    The actual series is: G_d(0) = Σ_n [C(2n,n)/2^{2n}]^d ... NO this is P(return).
    
    TODO: Extract correct series from Guttmann 2009/Glasser-Guttmann 1994.
    """
    mp.dps = dps + 50
    
    if verbose:
        t0 = time.time()
        print(f"Computing G_4(0) via series at {dps} dps...")
    
    # The random walk return probability generating function:
    # P_d(z) = Σ_{n=0}^∞ u_n z^n  where u_n = [C(2n,n)/4^n]^d = [C(2n,n)]^d / 4^{nd}
    # G_d(0) = P_d(1) = Σ u_n
    # BUT this series diverges for d <= 2 and converges for d >= 3
    
    # For d=4: u_n ~ C / (πn)^2 → converges but slowly
    # Need acceleration (Richardson extrapolation)
    
    if nterms is None:
        # Estimate terms needed: for d=4, u_n ~ 1/n², need N ~ 10^(dps/2) terms
        # This is too many for high precision. Series method alone won't reach 2000 dps.
        # For 100 dps benchmark, need ~10^50 terms — NOT feasible directly.
        # Must use analytic continuation / ODE method instead.
        # 
        # For now, compute partial sums + Richardson to get modest precision.
        nterms = min(5000, 10 ** min(6, dps // 20))
    
    from mpmath import binomial
    
    S = mpf(0)
    partial_sums = []
    for n in range(int(nterms)):
        cn2n = binomial(2*n, n)
        u_n = (cn2n / mpf(4)**n) ** 4
        S += u_n
        if n % 100 == 0 and n > 0:
            partial_sums.append(S)
    
    mp.dps = dps
    val = +S
    
    if verbose:
        elapsed = time.time() - t0
        print(f"  Done in {elapsed:.1f}s ({int(nterms)} terms)")
        print(f"  G_4(0) partial sum = {nstr(val, 30)}...")
        print(f"  (Note: series converges slowly, this is NOT full precision)")
    
    return val, partial_sums


# ============================================================
# 3D Benchmark: Joyce's closed form for G_3^SC(0)
# ============================================================

def joyce_G3_exact(dps=100):
    """
    Joyce (1994/2002) closed form for 3D simple cubic lattice G_3(0).
    
    G_3^SC(0) = (√6 / 96π³) Γ(1/4)² Γ(1/3) Γ(1/6)
    
    ... actually the exact formula needs to be verified from Joyce's paper.
    
    Known numerical value: G_3^SC(0) = 1.516386059190396...
    
    Alternative representation using K(k):
    G_3^SC(0) = (√6 / 4π²) [K(k₃)]²  where k₃ = (√6 - √2)/4
    
    TODO: Verify exact formula from Joyce 1994.
    """
    mp.dps = dps + 20
    
    # Use the K(k) representation (more standard)
    # k₃ = (√6 - √2)/4
    from mpmath import ellipk
    k3 = (sqrt(6) - sqrt(2)) / 4
    K3 = ellipk(k3**2)  # ellipk takes m = k²
    
    # G_3^SC(0) = (√6/(4π²)) K(k₃)²  ... needs verification
    # Let's try: G_3^SC(0) = √6/(4π²) · K(k₃)²  
    val = sqrt(6) / (4 * pi**2) * K3**2
    
    mp.dps = dps
    return +val


# ============================================================
# Main: Run benchmarks
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Lattice Green Function Computation Benchmarks")
    print("=" * 60)
    
    # Test 1: G_3(0) at 100 dps via Bessel integral
    print("\n--- Test 1: G_3(0) via Bessel integral (100 dps) ---")
    G3_bessel = lgf_bessel(3, dps=100)
    
    # Test 2: Joyce closed form for G_3(0)
    print("\n--- Test 2: G_3(0) via Joyce closed form (100 dps) ---")
    G3_joyce = joyce_G3_exact(dps=100)
    print(f"  G_3^Joyce = {nstr(G3_joyce, 50)}...")
    
    # Compare
    mp.dps = 100
    diff = abs(G3_bessel - G3_joyce)
    if diff > 0:
        digits = -int(log10(diff / abs(G3_bessel)))
        print(f"\n  Agreement: {digits} digits")
    else:
        print(f"\n  Exact agreement!")
    
    # Test 3: G_4(0) at 50 dps via Bessel integral
    print("\n--- Test 3: G_4(0) via Bessel integral (50 dps) ---")
    G4_50 = lgf_bessel(4, dps=50)
    
    # Test 4: G_4(0) at 100 dps via Bessel integral
    print("\n--- Test 4: G_4(0) via Bessel integral (100 dps) ---")
    G4_100 = lgf_bessel(4, dps=100)
    
    # Compare 50 vs 100
    mp.dps = 50
    diff = abs(mpf(G4_50) - mpf(G4_100))
    if diff > 0:
        digits = -int(log10(diff / abs(G4_50)))
        print(f"\n  G_4(0) 50dps vs 100dps: {digits} digit agreement")
    
    # Test 5: G_5(0) at 50 dps
    print("\n--- Test 5: G_5(0) via Bessel integral (50 dps) ---")
    G5_50 = lgf_bessel(5, dps=50)
    
    # Summary
    print("\n" + "=" * 60)
    print("Summary of G_d(0) values:")
    print("=" * 60)
    mp.dps = 50
    print(f"  G_3(0) = {nstr(G3_bessel, 40)}")
    print(f"  G_4(0) = {nstr(G4_100, 40)}")
    print(f"  G_5(0) = {nstr(G5_50, 40)}")
    print()
    print("Timings recorded above. Evaluate feasibility of 2000 dps.")
