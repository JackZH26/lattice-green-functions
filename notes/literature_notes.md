# LGF 文献笔记

## 1. Glasser & Guttmann 1994 (cond-mat/9408097) — ⭐ 最关键

**标题:** Lattice Green function (at 0) for the 4d hypercubic lattice  
**核心定义:**
$$P(z) = \frac{1}{\pi^4} \int_0^\pi \cdots \int_0^\pi \frac{d^4k}{1 - \frac{z}{4}\sum_{j=1}^4 \cos k_j}$$

**Bessel 积分:**
$$P(z) = \int_0^\infty e^{-x} I_0^4\!\left(\frac{xz}{4}\right) dx$$

**⭐ 椭圆积分表示 (equation 3):**
$$P(z) = \frac{8}{\pi^3} \int_0^1 \frac{K(k_+) K(k_-)}{\sqrt{1-x^2}}\, dx$$
其中 $k_\pm^2 = \frac{1}{2}[1 \pm x^2 z^2 \sqrt{1 - \frac{1}{4}x^2 z^2 - (1-\frac{1}{2}x^2 z^2)\sqrt{1-x^2 z^2}}]$

**数值:** $P(1) = G_4(0) = 1.23946712\ldots$ (仅 8 位)

**Fuchsian ODE (变量 $u = z^2$):**
$$4u^3(u-4)(u-1)p^{(iv)} + 8u^2(5u^2-20u+12)p''' + u(99u^2-293u+112)p'' + (57u^2-106u+16)p' + (3u-2)p = 0$$

奇异点: $u = 0, 1, 4, \infty$

**⭐ 三项递推关系 (for $r_n = 64^n a_n$):**
$$n^4 r_n - 4(20n^4 - 40n^3 + 33n^2 - 13n + 2)r_{n-1} + 256(4n^4 - 16n^3 + 23n^2 - 14n + 3)r_{n-2} = 0$$
初始值: $r_0 = 1, r_1 = 8$

$P(1) = \sum_{n=0}^\infty a_n = \sum r_n/64^n$，渐近 $a_n \sim 2/(\pi^2 n^2)$

**Kampé de Fériet 表示:**
$$P(z) = F^{2:1:1}_{0:2:2}\left[\frac{1}{2}, 1; \frac{1}{2}; \frac{1}{2}; -; 1,1; 1,1; \frac{z^2}{4}, \frac{z^2}{4}\right]$$

**关键判断:** 作者明确表示 "it is doubtful that P(z) can be expressed in terms of elliptic integrals as for the 3D case."

## 2. Bailey-Borwein-Broadhurst-Glasser 2008 (0801.0891) — PSLQ 方法论

**核心:** 用 PSLQ 发现 Bessel moments $c_{n,k} = \int_0^\infty t^k K_0(t)^n dt$ 的闭合形式。

**与我们相关的关键公式:**

- $c_{4,0} = \frac{\pi^4}{4} \cdot {}_4F_3([\frac{1}{2}]^4; [1]^3; 1)$
- $c_{4,1} = \frac{7}{8}\zeta(3)$
- Diamond lattice GF: $W_4(z) = \sum b_k (z/16)^k$，$b_k$ = A002895
- 参数化: $W_4(z_4) = \theta_3^2(q)\theta_3^2(q^3)$

**⚠️ 重要区分:** 
- ${}_4F_3([\frac{1}{2}]^4; [1]^3; z)$ 生成 $\binom{2n}{n}^4/256^n$ (A008977) → **BCC/Diamond lattice**
- 4D SC lattice 的 walk numbers $r_n$ (A002894) 是不同序列！
- 所以 $G_4(0) \neq {}_4F_3(1) = 1.1186\ldots$

**PSLQ 方法启示:**
- 他们用 100-1200+ digits
- Basis 包括 K at singular moduli, $\Gamma$ values, $\pi$, $\zeta$ values
- d=4 情况的闭合形式涉及 $_4F_3$ 和 theta functions

## 3. Bostan et al. 2011 — Ising Model / CY ODE

**关键:** $_4F_3([\frac{1}{2}]^4; [1]^3; z)$ 满足 CY ODE:
$$\theta^4 - 256x(\theta + \frac{1}{2})^4$$
这是 AESZ 表中的 #3。

**Hadamard 平方结构:** $_4F_3 = K \star K$ (K的Hadamard平方)

## 核心洞察 & PSLQ 策略修正

### G₄(0) 的正确数学身份

$$G_4(0) = P(1) = \sum_{n=0}^\infty a_n = \sum_{n=0}^\infty \frac{r_n}{64^n}$$

其中 $a_n = \frac{1}{\pi^4}\int[\frac{1}{4}\sum\cos k_j]^{2n} d^4k$，$r_n$ 满足上述三项递推。

序列 $r_n$: 1, 8, 168, 5120, 190120, 7939008, ... (OEIS A002894)

### 最有希望的 PSLQ basis（下一轮）

1. **椭圆积分核:** 从 eq.(3) 出发，$G_4(0) = \frac{8}{\pi^3}\int_0^1 K(k_+)K(k_-)/\sqrt{1-x^2}\,dx$
2. **Period 值:** 4阶 ODE 在 $u=1$ 附近有 4 个 periods（含 log 项）
3. **Modular form 值:** 如果 ODE 有 modular 参数化
4. **Apéry-like 常数:** $\sum r_n/(64^n n^s)$ 在特定 $s$ 值

### 计算策略改进

1. **递推法:** 用三项递推快速计算 $r_n$ 到 $n=10^6$+
2. **级数加速:** Levin u-transform 或 Wynn epsilon 加速 $\sum a_n$
3. **ODE 连接:** 在 $u$ 略小于 1 处用级数，再减去已知奇异部分
4. **交叉验证:** Bessel 积分 vs 递推+加速
