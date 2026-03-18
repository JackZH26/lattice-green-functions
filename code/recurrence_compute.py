"""
Compute G_4(0) via the Glasser-Guttmann three-term recurrence relation.

r_n satisfies:
  n^4 r_n = 4(20n^4 - 40n^3 + 33n^2 - 13n + 2) r_{n-1} 
          - 256(4n^4 - 16n^3 + 23n^2 - 14n + 3) r_{n-2}

with r_0 = 1, r_1 = 8.

Then a_n = r_n / 64^n, and G_4(0) = P(1) = sum(a_n, n=0..inf).

Since a_n ~ 2/(pi^2 n^2), we use Richardson extrapolation or 
Levin's u-transform for series acceleration.
"""

from mpmath import mp, mpf, nstr, pi, mpf, richardson, nsum, inf
import time


def compute_rn(N, dps=100):
    """Compute r_0, ..., r_N using integer recurrence."""
    mp.dps = dps + 20
    r = [mpf(0)] * (N + 1)
    r[0] = mpf(1)
    if N >= 1:
        r[1] = mpf(8)
    
    for n in range(2, N + 1):
        n4 = n**4
        c1 = 4 * (20*n**4 - 40*n**3 + 33*n**2 - 13*n + 2)
        c2 = 256 * (4*n**4 - 16*n**3 + 23*n**2 - 14*n + 3)
        r[n] = (c1 * r[n-1] - c2 * r[n-2]) / n4
    
    return r


def partial_sums(r_list, dps=100):
    """Compute partial sums S_N = sum_{n=0}^{N} r_n / 64^n."""
    mp.dps = dps + 20
    S = mpf(0)
    sums = []
    for n, rn in enumerate(r_list):
        S += rn / mpf(64)**n
        sums.append(S)
    return sums


def richardson_extrap(sums, order=20):
    """Apply Richardson extrapolation to partial sums."""
    N = len(sums)
    if N < order + 1:
        order = N - 1
    
    # Richardson extrapolation for S_n → L as S_n = L + c1/n + c2/n^2 + ...
    # Use the last 'order+1' partial sums
    from mpmath import binomial
    
    k = order
    start = N - k - 1
    
    result = mpf(0)
    for j in range(k + 1):
        n = start + j
        coeff = (-1)**(k - j) * binomial(k, j) * (n + 1)**k
        result += coeff * sums[n]
    
    # Normalize
    norm = mpf(0)
    for j in range(k + 1):
        n = start + j
        norm += (-1)**(k - j) * binomial(k, j) * (n + 1)**k
    
    return result / norm


def wynn_epsilon(sums, max_order=None):
    """Wynn's epsilon algorithm for series acceleration."""
    n = len(sums)
    if max_order is None:
        max_order = n - 1
    
    # epsilon table: eps[k][j]
    eps = [[mpf(0)] * (max_order + 2) for _ in range(n)]
    
    for i in range(n):
        eps[i][0] = mpf(0)
        eps[i][1] = sums[i]
    
    for j in range(2, min(max_order + 2, n)):
        for i in range(n - j):
            diff = eps[i+1][j-1] - eps[i][j-1]
            if abs(diff) < mpf(10)**(-mp.dps + 5):
                eps[i][j] = eps[i][j-1]
            else:
                eps[i][j] = eps[i][j-2] + 1 / diff
    
    # Return the best estimate (last even column)
    best = sums[-1]
    for j in range(1, min(max_order + 2, n)):
        if j % 2 == 1:  # odd columns are the "epsilon" accelerated values
            idx = n - j - 1
            if idx >= 0:
                best = eps[idx][j]
    
    return best


if __name__ == "__main__":
    # Test 1: Verify recurrence against known values
    print("=" * 60)
    print("Recurrence verification")
    print("=" * 60)
    
    r = compute_rn(10, dps=50)
    known = [1, 8, 168, 5120, 190120, 7939008, 357713664, 
             16993726464, 839358285480, 42714450658880, 2225741588095168]
    
    for n in range(min(11, len(r))):
        match = "✓" if int(r[n]) == known[n] else "✗"
        print(f"  r_{n:2d} = {int(r[n]):>25d}  {match}")
    
    # Test 2: Compute G4(0) with increasing precision
    print()
    print("=" * 60)
    print("G_4(0) via recurrence + series acceleration")
    print("=" * 60)
    
    for N in [100, 500, 2000, 5000]:
        DPS = 100
        mp.dps = DPS + 20
        t0 = time.time()
        
        r = compute_rn(N, dps=DPS)
        sums = partial_sums(r, dps=DPS)
        
        # Raw partial sum
        raw = sums[-1]
        
        # Richardson extrapolation (various orders)
        rich20 = richardson_extrap(sums, order=20)
        rich40 = richardson_extrap(sums, order=min(40, N//2))
        
        elapsed = time.time() - t0
        
        mp.dps = DPS
        print(f"\n  N = {N} [{elapsed:.2f}s]")
        print(f"    Raw partial sum  = {nstr(raw, 30)}")
        print(f"    Richardson(20)   = {nstr(rich20, 30)}")
        print(f"    Richardson({min(40,N//2)})   = {nstr(rich40, 30)}")
    
    # Compare with known Bessel integral value
    print()
    print("=" * 60)
    print("Comparison with Bessel integral value")
    print("=" * 60)
    mp.dps = 100
    with open('../data/G4_500dps.txt', 'r') as f:
        G4_bessel = mpf(f.read().strip())
    print(f"  Bessel integral = {nstr(G4_bessel, 50)}")
    
    # High-precision attempt with many terms
    DPS = 200
    mp.dps = DPS + 20
    N = 10000
    t0 = time.time()
    r = compute_rn(N, dps=DPS)
    sums = partial_sums(r, dps=DPS)
    rich = richardson_extrap(sums, order=60)
    elapsed = time.time() - t0
    
    mp.dps = DPS
    print(f"\n  N=10000, Richardson(60) [{elapsed:.2f}s]:")
    print(f"    = {nstr(rich, 50)}")
    
    # Digit agreement
    from mpmath import log10
    diff = abs(rich - G4_bessel)
    if diff > 0:
        digits = -int(log10(diff / abs(G4_bessel)))
        print(f"    Agreement with Bessel: {digits} digits")
