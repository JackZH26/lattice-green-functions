# #003 LGF 关键发现记录

**日期:** 2026-03-18
**状态:** Phase 1/2 进行中

---

## 发现 1：4D SC Walk 数的 Domb 分解 ⭐⭐⭐

**4D simple cubic lattice walk 数有优美的因式分解：**

$$c_n = \binom{2n}{n} \cdot D_n$$

其中 $D_n$ 是 Domb 数（OEIS A002895），即 diamond lattice walk 数。

**验证（n=0..7 精确匹配）：**

| n | C(2n,n) | D_n | C(2n,n)·D_n | c_n (递推) | ✓ |
|---|---------|-----|-------------|-----------|---|
| 0 | 1 | 1 | 1 | 1 | ✓ |
| 1 | 2 | 4 | 8 | 8 | ✓ |
| 2 | 6 | 28 | 168 | 168 | ✓ |
| 3 | 20 | 256 | 5120 | 5120 | ✓ |
| 4 | 70 | 2716 | 190120 | 190120 | ✓ |
| 5 | 252 | 31504 | 7939008 | 7939008 | ✓ |
| 6 | 924 | 387136 | 357713664 | 357713664 | ✓ |
| 7 | 3432 | 4951552 | 16993726464 | 16993726464 | ✓ |

**推论：**

$$G_4(0) = \sum_{n=0}^{\infty} \frac{\binom{2n}{n} \cdot D_n}{64^n}$$

这是 1D 随机游走 GF ($1/\sqrt{1-4z}$) 与 Diamond lattice GF ($\sum D_n z^n$) 的 **Hadamard 乘积**在 $z=1/64$ 处的值。

**ODE 层面：** AESZ #16 (4D SC, 4阶) = Hadamard product of $1/\sqrt{1-4z}$ (1阶) × AESZ #34 (Diamond, 3阶)

**文献状态：** Glasser-Guttmann 1994 和 Guttmann 2009 均未明确记录此分解。

---

## 发现 2：积分表示

由 $\binom{2n}{n}/4^n = (\frac{1}{2})_n/n!$ 和 Beta 函数积分：

$$G_4(0) = \frac{1}{\pi}\int_0^1 \frac{G_D(x/16)}{\sqrt{x(1-x)}}\,dx$$

其中 $G_D(z) = \sum D_n z^n$ 是 Domb 数生成函数（diamond lattice GF，满足 AESZ #34 三阶 ODE）。

**意义：** 将 4 阶 CY period 分解为 3 阶 CY period 的 arcsine 核积分。

---

## 发现 3：Paramodular Form 对应

AESZ #16 (CYDB 编号 2.52) 在不同参数处对应 weight 3 Siegel paramodular Hecke eigenforms：

| 参数 t | Conductor | Paramodular Form |
|--------|-----------|------------------|
| -1/64 | 160 | 2.K.160.3.0.a.a |
| 1/8 | 224 | 2.K.224.3.0.a.b |
| 1 | 315 | 2.K.315.3.0.a.b |
| -1/16 | 640 | 2.K.640.3.0.a.d |

**G₄(0) = y₀(1/64)**，CY 参数 $t = -1/64$（需确认符号约定）→ 对应 **conductor 160**。

---

## 发现 4：Domb 数的 1/π 公式

已知 (Chan-Chan-Liu 2004 等)：

$$\sum_{n=0}^{\infty} (5n+1) \frac{D_n}{(-64)^n} = \frac{2}{\pi\sqrt{3}}$$

（符号待确认，可能有 $(-1)^n$ 因子）

G₄(0) 是 $D_n$ 的 $\binom{2n}{n}$-加权版本，可能存在类似的 closed-form 表达。

---

## 发现 5：PSLQ 排除结果（系统性）

**精度 400-800 位，maxcoeff ≤ 10000，全部 null：**

1. G₄(0) 不是代数数 (degree ≤ 15)
2. 不在 {π, ζ(3), ζ(5), ln2, √2, √3} 线性张成
3. 不在 {Γ(p/q), p/q 分母 ≤ 24} 的乘法张成
4. 不是 K(k) 在 singular moduli 处的简单乘积
5. 不是 ₄F₃(½,½,½,½;1,1,1;1) 的简单倍数
6. 不是 3D Watson 积分值的线性组合
7. G₄/G₅, G₄/G₆ 等维度间比值不是代数数
8. Catalan 常数无关

---

## 高精度数值

| d | G_d(0) | 精度 | 文件 |
|---|--------|------|------|
| 4 | 1.23946712184848171267869766485900... | 1000 dps | G4_1000dps.txt |
| 5 | 1.15630812484023117870713512193856... | 500 dps | G5_500dps.txt |
| 6 | 1.11696337322667184368564433196861... | 500 dps | G6_500dps.txt |
| 7 | 1.09390631558784799668327182355901... | 500 dps | G7_500dps.txt |

---

## 下一步攻击方向

1. **L(F, 2) 特殊值：** 计算 conductor 160, weight 3 paramodular form 的 L-function 在 $s=2$ 处的值
2. **Domb GF 解析延拓：** 用 AESZ #34 的 ODE 把 G_D(z) 解析延拓到边界
3. **Hadamard 乘积文献：** 搜索 CY 文献中 AESZ #16 = Had(algebraic, AESZ #34) 的讨论
4. **Mahler measure：** 计算 $m(4 - \cos k_1 - \cos k_2 - \cos k_3 - \cos k_4)$ 是否与 G₄(0) 相关
5. **Guillera 型 1/π² 公式：** 检查是否存在涉及 $\binom{2n}{n} D_n$ 的 Ramanujan-Guillera 型级数

---

## 递推关系

**4D SC walk 数 $c_n$ (= $r_n$ in Glasser-Guttmann):**
$$n^4 c_n = 4(2n-1)^2(5n^2-5n+2)\,c_{n-1} - 256(n-1)^2(2n-3)(2n-1)\,c_{n-2}$$

**Domb 数 $D_n$:**
$$(n+1)^3 D_{n+1} = (2n+1)(10n^2+10n+3)\,D_n - 64n^3\,D_{n-1}$$

**分解恒等式：** $c_n = \binom{2n}{n} \cdot D_n$

---

*最后更新：2026-03-18 15:00*
