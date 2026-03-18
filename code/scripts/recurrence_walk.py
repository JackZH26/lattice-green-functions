"""
Compute 4D walk numbers c_n and Domb numbers D_n via recurrence,
verify c_n = C(2n,n) * D_n, and compute G_4(0) via Richardson extrapolation.
"""
from mpmath import mp, mpf, binomial

def walk_numbers(N, dps=50):
    mp.dps = dps
    c = [mpf(1), mpf(8)]
    for n in range(2, N+1):
        c.append((4*(2*n-1)**2*(5*n**2-5*n+2)*c[n-1]
                  - 256*(n-1)**2*(2*n-3)*(2*n-1)*c[n-2]) / n**4)
    return c

def domb_numbers(N, dps=50):
    mp.dps = dps
    D = [mpf(1), mpf(4)]
    for n in range(1, N):
        D.append(((2*n+1)*(10*n**2+10*n+4)*D[n] - 64*n**3*D[n-1]) / (n+1)**3)
    return D

def verify_decomposition(N=20):
    c = walk_numbers(N)
    D = domb_numbers(N)
    print(f"{'n':>3} {'c_n':>20} {'C(2n,n)*D_n':>20} {'Match':>6}")
    for n in range(N+1):
        prod = int(binomial(2*n, n) * D[n])
        print(f"{n:>3} {int(c[n]):>20} {prod:>20} {'✓' if int(c[n])==prod else '✗':>6}")

def richardson_G4(N=10000, dps=50):
    mp.dps = dps
    c = walk_numbers(N, dps)
    S = [mpf(0)] * (N+1)
    S[0] = c[0]
    for n in range(1, N+1):
        S[n] = S[n-1] + c[n] / mpf(64)**n
    # Richardson: R = (N²S_N - M²S_M)/(N²-M²)
    M = N // 2
    R = (mpf(N)**2 * S[N] - mpf(M)**2 * S[M]) / (mpf(N)**2 - mpf(M)**2)
    return R

if __name__ == '__main__':
    print("=== Domb Decomposition Verification ===")
    verify_decomposition(10)
    print("\n=== Richardson Extrapolation for G_4(0) ===")
    G4 = richardson_G4(10000, 50)
    print(f"G_4(0) ≈ {G4}")
