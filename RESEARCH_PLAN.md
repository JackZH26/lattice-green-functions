# 研究计划：Closed-Form Expressions for Higher-Dimensional Lattice Green Functions via Integer Relation Algorithms

**研究者：** Jack（独立研究者）
**制定日期：** 2026-03-18
**预计周期：** 10-14 周
**技术栈：** Python + mpmath + PSLQ + Richardson extrapolation
**算力：** 4核 8GB VPS

---

## 目录

1. [文献调研清单](#1-文献调研清单)
2. [数学基础](#2-数学基础)
3. [技术路线图](#3-技术路线图phase-1-5)
4. [PSLQ 搜索策略](#4-pslq-搜索策略)
5. [计算可行性评估](#5-计算可行性详细评估)
6. [风险评估 + Plan B](#6-风险评估--plan-b)
7. [里程碑和 Go/No-Go 决策点](#7-里程碑和-gono-go-决策点)
8. [论文结构草案](#8-论文结构草案)
9. [投稿策略](#9-投稿策略)
10. [立即行动清单](#10-立即行动清单phase-1-第一周)

---

## 1. 文献调研清单

### 核心论文（按重要性排序）

**[L1] Watson (1939) — 奠基之作**
- G.N. Watson, "Three triple integrals"
- *Quart. J. Math. Oxford Ser.* **os-10**(1), 266–276
- DOI: `10.1093/qmath/os-10.1.266`
- 💡 首次精确计算 3D SC/BCC/FCC lattice 的 return probability 积分，开创了 LGF 闭合形式研究

**[L2] Joyce (1994) — 3D 闭合形式突破**
- G.S. Joyce, "On the cubic lattice Green functions"
- *Proc. R. Soc. A* **445**(1924), 463–477
- DOI: `10.1098/rspa.1994.0072`
- 💡 证明 3D SC 和 FCC lattice LGF 可用 complete elliptic integral K(k) 的平方表示

**[L3] Joyce (2002) — 3D 一般格点**
- G.S. Joyce, "Exact evaluation of the simple cubic lattice Green function for a general lattice point"
- *J. Phys. A: Math. Gen.* **35**, 9811
- DOI: `10.1088/0305-4470/35/46/307`
- 💡 将 Joyce 1994 推广到一般格点，给出系统的 K(k)² 表达式

**[L4] Joyce (2001) — 高精度 + 奇异行为**
- G.S. Joyce, "Singular behaviour of the cubic lattice Green functions and associated integrals"
- *J. Phys. A: Math. Gen.* **34**, 3831
- DOI: `10.1088/0305-4470/34/18/311`
- 💡 发展极高精度数值计算 LGF 的方法，分析奇异行为——方法论上的重要参考

**[L5] Glasser & Guttmann (1994) — 4D 先驱工作**
- M.L. Glasser, A.J. Guttmann, "Lattice Green function (at 0) for the 4d hypercubic lattice"
- *J. Phys. A: Math. Gen.* **27**(21), 7011
- DOI: `10.1088/0305-4470/27/21/016` | arXiv: `cond-mat/9408097`
- 💡 首次系统研究 4D hypercubic LGF，用 Kampé de Fériet 函数表示生成函数——4D 的关键起点

**[L6] Guttmann (2009) — LGF 与 Calabi-Yau 联系**
- A.J. Guttmann, "Lattice Green functions and Calabi-Yau differential equations"
- *J. Phys. A: Math. Theor.* **42**(23), 232001
- DOI: `10.1088/1751-8113/42/23/232001`
- 💡 发现所有 4D LGF 满足 Calabi-Yau 四阶 ODE——这是理解 4D 结构的关键论文

**[L7] Koutschan (2013) — Computer algebra + 高维 FCC**
- C. Koutschan, "Lattice Green's functions of the higher-dimensional face-centered cubic lattices"
- *J. Phys. A: Math. Theor.* **46**, 125005
- arXiv: `1108.2164`
- 💡 用 creative telescoping 推导 4D/5D/6D FCC lattice LGF 的 ODE——方法论参考

**[L8] Bailey, Borwein, Broadhurst, Glasser (2008) — Bessel moments**
- D.H. Bailey, J.M. Borwein, D.J. Broadhurst, M.L. Glasser, "Elliptic integral evaluations of Bessel moments"
- *J. Phys. A: Math. Theor.* **41**, 205203
- arXiv: `0801.0891`
- 💡 Bessel function moments 与 LGF 的联系，用 PSLQ 发现 elliptic integral 闭合形式——方法论的直接先例

**[L9] Broadhurst (2009) — Bessel moments + Calabi-Yau**
- D.J. Broadhurst, "Bessel moments, random walks and Calabi-Yau equations"
- 未正式发表，preprint 广泛引用
- 💡 将 Bessel moments 与 random walks、Calabi-Yau ODE 联系起来——理论框架参考

**[L10] Borwein, Glasser, McPhedran, Wan, Zucker (2013) — 综合参考书**
- J.M. Borwein, M.L. Glasser, R.C. McPhedran, J.G. Wan, I.J. Zucker, *"Lattice Sums Then and Now"*
- Cambridge University Press, Encyclopedia of Mathematics and Its Applications **150**
- ISBN: `978-1-107-03990-2`
- 💡 lattice sums 的百科全书式参考，涵盖历史、方法、开放问题——必读

**[L11] Bailey & Borwein (2005) — PSLQ 实战指南**
- D.H. Bailey, J.M. Borwein, "Experimental mathematics: examples, methods and implications"
- *Notices Amer. Math. Soc.* **52**(5), 502–514
- 💡 PSLQ 应用的经典综述，包含搜索策略和判断标准——操作手册

**[L12] Ferguson & Bailey (1992) — PSLQ 算法原始论文**
- H.R.P. Ferguson, D.H. Bailey, S. Arwade, "Analysis of PSLQ, an integer relation finding algorithm"
- *Math. Comp.* **68**(225), 351–369 (1999, 完整版本)
- DOI: `10.1090/S0025-5718-99-00995-3`
- 💡 PSLQ 算法的理论基础和复杂度分析

**[L13] Zucker & Joyce (2001) — Lattice sums 与 elliptic integrals**
- I.J. Zucker, G.S. Joyce, "Special values of the hypergeometric series II"
- *Math. Proc. Cambridge Phil. Soc.* **131**, 309–319
- DOI: `10.1017/S0305004101005254`
- 💡 lattice sums 的特殊值与 hypergeometric series 的联系

**[L14] Borwein & Borwein (1987) — Pi and the AGM**
- J.M. Borwein, P.B. Borwein, *"Pi and the AGM: A Study in Analytic Number Theory and Computational Complexity"*
- Wiley, New York
- 💡 Ramanujan 1/π 公式的严格证明，elliptic modular functions 理论——寻找闭合形式的理论武器

**[L15] Maradudin, Montroll, Weiss (1960) — LGF 物理背景**
- A.A. Maradudin, E.W. Montroll, G.H. Weiss, "Green's functions for monatomic simple cubic lattices"
- *Acad. Roy. Belg. Cl. Sci. Mém.* **14**(7)
- 💡 LGF 在晶格动力学中的物理应用，提供物理 motivation

---

## 2. 数学基础

### 2.1 LGF 的精确定义

**d 维 hypercubic lattice Green function at the origin:**

$$G_d(0) = \frac{1}{\pi^d} \int_0^{\pi} \cdots \int_0^{\pi} \frac{dk_1 \cdots dk_d}{d - \cos k_1 - \cos k_2 - \cdots - \cos k_d}$$

这里利用了被积函数关于每个 $k_i$ 的偶对称性，将积分区间从 $[-\pi, \pi]$ 缩减到 $[0, \pi]$。

**物理含义：** $P_d = 1 - 1/G_d(0)$ 是 d 维 hypercubic lattice 上 random walk 的 return probability。

**已知数值（供 benchmark）：**
- $G_2(0) = \infty$（2D random walk 是 recurrent 的）
- $G_3(0) = 1.516386...$（Watson 1939 首先计算）
- $G_4(0) = 1.239465...$
- $G_5(0) = 1.156528...$

### 2.2 已知闭合形式

**2D Square Lattice（经典结果）：**

2D 的 LGF 在 origin 发散，但偏离 origin 的 Green function 有闭合形式。对于 return probability 的生成函数：

$$P(z) = \frac{2}{\pi} K\left(\frac{4z}{(1+z)^2} \cdot \frac{1}{4}\right)$$

其中 $K(k)$ 是 complete elliptic integral of the first kind。

**3D Simple Cubic Lattice (Joyce 1994, 2002)：**

Watson (1939) 证明了三个著名的 triple integral 恒等式。Joyce 的突破在于：

$$G_3^{SC}(0) = \frac{\sqrt{6}}{96\pi^3} \Gamma\left(\frac{1}{4}\right)^2 \Gamma\left(\frac{1}{3}\right) \Gamma\left(\frac{1}{6}\right)$$

等价地，可以用 $K(k)^2$ 表示：

$$G_3^{SC}(0) = \frac{\sqrt{6}}{4\pi^2} \left[K\left(k_{\text{sc}}\right)\right]^2$$

其中 $k_{\text{sc}} = (2-\sqrt{3})(\sqrt{3}-\sqrt{2})$。

**3D FCC Lattice (Joyce 1994)：**

$$G_3^{FCC}(0) = \frac{4}{3} \cdot \frac{\sqrt{2}}{\pi^2} \left[K\left(k_{\text{fcc}}\right)\right]^2$$

**3D BCC Lattice：**

$$G_3^{BCC}(0) = \frac{\sqrt{3}}{4\pi^3} \Gamma\left(\frac{1}{4}\right)^2 \cdot \frac{1}{2^{5/3}}$$

（具体形式需从 Joyce 原文确认）

### 2.3 闭合形式的结构模式

从 2D→3D 的升维中观察到的模式：

| 维度 | 闭合形式结构 | 涉及的特殊函数 |
|------|-------------|---------------|
| 2D | $K(k)$ | 单个 elliptic integral |
| 3D | $K(k)^2$ | elliptic integral 的平方 |
| 4D | $K(k)^3$? 或更复杂? | **未知！这是核心问题** |

**关键猜测：** 4D LGF 可能涉及：
- $K(k)^3$ 结构（自然升维）
- 更一般的 period integral / Calabi-Yau period
- $\Gamma$ 函数在有理点的乘积
- Ramanujan-type 1/π² 公式

### 2.4 Watson-type 变换与降维

**Watson 变换的核心思想：** 利用三角恒等式将 d 重积分降维。

对于 3D SC lattice，Watson 通过变量替换：
$$\cos k_1 \cos k_2 \cos k_3 = \frac{1}{8}[\cos(k_1+k_2+k_3) + \cdots]$$
将三重积分化为可以用 elliptic integral 表示的形式。

**4D 的降维策略：**

1. **逐步积分法：** 先对 $k_d$ 积分，得到 (d-1) 重积分
   $$\int_0^{\pi} \frac{dk_d}{a - \cos k_d} = \frac{\pi}{\sqrt{a^2 - 1}}$$
   其中 $a = d - \cos k_1 - \cdots - \cos k_{d-1}$

2. **对称性利用：** $G_d(0)$ 的被积函数在 $k_i \to \pi - k_i$ 下不变（对所有 $i$），可以利用这一点简化积分区域

3. **Bessel function 表示：** 利用恒等式
   $$G_d(0) = \int_0^{\infty} e^{-dt} \left[I_0(t)\right]^d dt$$
   其中 $I_0(t)$ 是 modified Bessel function of the first kind。**这是数值计算最实用的形式！**

4. **Fourier 展开 + 级数加速：** 展开为快速收敛级数后用 Richardson extrapolation

### 2.5 与 Ramanujan-type 公式的联系

**核心联系：** Lattice sums 与 1/π 公式共享相同的数学结构（modular forms, elliptic integrals）。

Borwein 兄弟证明 Ramanujan 的 17 个 1/π 公式，本质上是利用了 singular moduli 和 elliptic modular functions。

**类比推理：**
- 2D LGF ↔ K(k) ↔ 1/π 的 Ramanujan 公式（单层）
- 3D LGF ↔ K(k)² ↔ 1/π² 的 Ramanujan-type 公式？
- 4D LGF ↔ ??? ↔ Calabi-Yau periods

Guttmann (2009) 已经证明 4D LGF 满足 Calabi-Yau ODE，这意味着闭合形式（如果存在）将涉及 Calabi-Yau periods——一类高度非平凡的特殊值。

### 2.6 Calabi-Yau 联系的含义

Guttmann 的发现意味着：
- 4D SC lattice 的 LGF 满足四阶 Fuchsian ODE
- 该 ODE 属于 Calabi-Yau 类（monodromy 具有特殊结构）
- 解可以用 period integral 表示
- 闭合形式可能涉及 **新的** 特殊常数（不仅仅是 $\Gamma$ 在有理点的值）

**这既是机遇也是挑战：** 如果 PSLQ 找到了一个关系，它可能揭示 Calabi-Yau periods 与经典常数之间前所未知的联系。

---

## 3. 技术路线图（Phase 1-5）

### Phase 1: 文献 + 理论准备（第 1-2 周）

**目标：** 完全理解已有工作，确定 PSLQ 搜索的理论基础

- [ ] **T1.1** 获取并精读 [L5] Glasser-Guttmann 1994（4D LGF 的 Kampé de Fériet 表示）
- [ ] **T1.2** 精读 [L6] Guttmann 2009（4D Calabi-Yau ODE 的具体形式）
- [ ] **T1.3** 精读 [L2] Joyce 1994 和 [L3] Joyce 2002（理解 3D 闭合形式是如何被发现/证明的）
- [ ] **T1.4** 通读 [L10] Lattice Sums Then and Now 第 4-5 章（高维 LGF 部分）
- [ ] **T1.5** 精读 [L8] Bailey et al. 2008（学习 PSLQ 发现 Bessel moment 闭合形式的方法论）
- [ ] **T1.6** 从 Guttmann 2009 提取 4D SC lattice LGF 的具体 ODE 形式
- [ ] **T1.7** 确认文献中 4D/5D $G_d(0)$ 的已知数值精度（目前已知多少位？）
- [ ] **T1.8** 整理候选 basis 的理论依据（见第 4 节）
- [ ] **T1.9** 从 [L7] Koutschan 2013 学习 creative telescoping 方法是否适用于 hypercubic lattice

**验证标准：**
- 能独立写出 4D SC lattice LGF 的 Bessel integral 表示
- 能列出 Guttmann 2009 中 4D ODE 的具体形式
- 有一份按优先级排序的 PSLQ basis 候选列表

**输入：** 论文 PDF
**输出：** 理论笔记文档 + basis 候选列表

---

### Phase 2: 代码实现 — 高精度 LGF 计算（第 3-5 周）

**目标：** 计算 $G_d(0)$ (d=3,4,5) 到 2000+ 位精度

#### 子任务：

- [ ] **T2.1** 实现 Bessel integral 表示的计算
  ```python
  # G_d(0) = ∫₀^∞ e^{-dt} [I₀(t)]^d dt
  # mpmath.besseli(0, t) 在高精度下的性能测试
  ```
- [ ] **T2.2** 实现 3D benchmark：计算 $G_3^{SC}(0)$ 到 2000 位，与 Joyce 闭合形式对比
- [ ] **T2.3** 实现 ODE 级数展开法（从 Guttmann 的 4D ODE 出发）
  - 从 ODE 推导出 Taylor 系数的递推关系
  - 利用递推关系计算数千项系数
  - 用级数在 $z=1$ 处求和（需要 analytic continuation 技巧）
- [ ] **T2.4** 实现逐步积分降维法
  - 4D → 3重积分（解析积掉一维）
  - 可能 4D → 2重积分（如果变量替换可行）
- [ ] **T2.5** 实现 Richardson extrapolation / Euler-Maclaurin 加速
- [ ] **T2.6** 交叉验证：至少两种独立方法算出相同的 $G_4(0)$ 到 500+ 位
- [ ] **T2.7** 推到 2000+ 位精度
- [ ] **T2.8** 计算 $G_5(0)$ 到 1000+ 位
- [ ] **T2.9** 计算不同格点类型的 4D LGF：BCC, FCC（如果可行）
- [ ] **T2.10** 性能 profiling 和优化

**验证标准：**
- $G_3^{SC}(0)$ 与 Joyce 闭合形式吻合到 2000 位
- $G_4(0)$ 至少两种方法交叉验证到 500 位
- $G_4(0)$ 单一最优方法推到 2000+ 位

**输入：** 理论笔记、ODE 形式
**输出：** `lgf_compute.py` 代码 + 高精度数值文件

#### 关键技术细节：

**Bessel integral 方法的实现：**
```python
from mpmath import mp, mpf, besseli, exp, quad, inf

def G_d_bessel(d, dps=2000):
    mp.dps = dps + 50  # 留 margin
    def integrand(t):
        return exp(-d*t) * besseli(0, t)**d
    result = quad(integrand, [0, inf])
    mp.dps = dps
    return +result  # 截断到目标精度
```

**ODE 递推法（4D SC）：**
Guttmann 2009 给出 4D SC LGF 的生成函数 $f(z) = \sum a_n z^n$ 满足四阶 ODE。
从 ODE 可以推导 $a_n$ 的递推关系，然后：
$$G_4(0) = f(1) = \sum_{n=0}^{\infty} a_n$$
级数在 $z=1$ 处收敛（但可能很慢），需要加速技巧。

---

### Phase 3: PSLQ 系统搜索（第 6-8 周）

**目标：** 对 $G_4(0)$ 及相关量进行系统的 integer relation 搜索

- [ ] **T3.1** 构建 Level 1 basis（基本常数 + $\Gamma$ 值），运行 PSLQ
- [ ] **T3.2** 构建 Level 2 basis（elliptic integral + singular moduli），运行 PSLQ
- [ ] **T3.3** 构建 Level 3 basis（$K(k)^3$ + 混合项），运行 PSLQ
- [ ] **T3.4** Multiplicative PSLQ 搜索（对 $\log G_4(0)$ 搜索）
- [ ] **T3.5** 搜索 $G_4(0)^2$, $G_4(0)^3$, $1/G_4(0)$ 等变换后的量
- [ ] **T3.6** 搜索 $G_4(0) \cdot \pi^n$, $G_4(0) / \Gamma(1/4)^k$ 等归一化
- [ ] **T3.7** 对 5D 重复上述搜索
- [ ] **T3.8** 对 4D BCC, FCC 重复搜索（如果 Phase 2 成功计算了这些值）
- [ ] **T3.9** 搜索不同维度 LGF 之间的关系
- [ ] **T3.10** 记录所有 null result（证明某些形式不存在的证据）

**验证标准：**
- 每次 PSLQ 运行都记录 basis、精度、min relation norm
- 3D benchmark：PSLQ 能重新发现 Joyce 的闭合形式
- 如果找到候选关系：独立验证到更高精度

**输入：** 高精度数值 + basis 列表
**输出：** PSLQ 搜索日志 + 候选关系（如果有）

---

### Phase 4: 扩展和深化（第 9-11 周）

**目标：** 深化结果，寻找更多结构

- [ ] **T4.1** 如果找到闭合形式：尝试证明（从 ODE 出发）
- [ ] **T4.2** 如果找到闭合形式：检查与 Calabi-Yau periods 的联系
- [ ] **T4.3** 如果没找到：扩大 basis 搜索范围（见 Plan B）
- [ ] **T4.4** 计算 $G_4(\mathbf{n})$ 对于近邻格点 $\mathbf{n}$（不仅限于 origin）
- [ ] **T4.5** 研究 $G_d(0)$ 的 generating function 在特殊点的值
- [ ] **T4.6** 探索 LGF 与其他物理/数学量的联系
- [ ] **T4.7** 如果有 partial result（例如 $G_4(0) \cdot \alpha = $ 某个可识别的常数），扩展为猜想

**验证标准：**
- 所有声称的恒等式验证到 2000+ 位
- 理论推导无逻辑跳跃

---

### Phase 5: 论文撰写（第 12-14 周）

**目标：** 完成可投稿论文

- [ ] **T5.1** 确定论文定位（见第 8 节三种情景）
- [ ] **T5.2** 撰写初稿
- [ ] **T5.3** 代码整理，准备 supplementary material
- [ ] **T5.4** 内部审查（自查逻辑、数值、公式）
- [ ] **T5.5** 格式化（目标期刊的 LaTeX 模板）
- [ ] **T5.6** 投稿

---

## 4. PSLQ 搜索策略

### 4.1 从 3D 闭合形式学到的经验

Joyce 的 3D 结果告诉我们：
- $G_3^{SC}(0)$ 的闭合形式涉及 $\Gamma(1/4)^2 \cdot \Gamma(1/3) \cdot \Gamma(1/6)$ 和 $\sqrt{6}$
- 等价于 $K(k)^2$ 在特殊 modulus
- 涉及的代数数都是 cyclotomic field 的元素（$\sqrt{2}$, $\sqrt{3}$）

**升维外推：** 4D 闭合形式可能涉及：
- $\Gamma$ 函数在更多有理点的值（$\Gamma(1/4), \Gamma(1/3), \Gamma(1/6), \Gamma(1/8)$?）
- higher-order singular moduli
- $K(k)^3$ 或更一般的 hypergeometric period
- 平方根 $\sqrt{2}, \sqrt{3}, \sqrt{5}, \sqrt{6}$ 的组合

### 4.2 Basis 层级策略

**Level 0 — Algebraic（快速排除）：**
```
basis = [1, G₄(0), G₄(0)², G₄(0)³, ..., G₄(0)^N]  (N ≤ 30)
```
检查 $G_4(0)$ 是否为低次代数数。几乎肯定不是，但 5 分钟就能排除。

**Level 1 — Classical constants（基本搜索）：**
```
basis = [1, G₄(0), π, π², ln2, ζ(3), ζ(5),
         Γ(1/4)^4/π³, Γ(1/3)^3/π²]
```
以及包含 $G_4(0)$ 与这些常数乘积的扩展 basis。

**Level 2 — Gamma products（针对性搜索）：**

基于 3D 结果的结构，构建涉及 $\Gamma$ 在有理点乘积的 basis：
```
basis = [1, G₄(0),
         Γ(1/4)^2·Γ(1/3)·Γ(1/6) / π^a,   # 类 Joyce 结构
         Γ(1/4)^4 / π^3,                    # ∝ K(1/√2)²
         Γ(1/3)^6 / π^4,                    # ∝ K(k₃)²
         Γ(1/4)^6 / π^{9/2},               # K(k)³ 候选
         Γ(1/3)^9 / π^6,
         ...]
```
注意：用 $\Gamma$ 的 reflection/multiplication 公式化简，避免 basis 元素线性相关。

**Level 3 — Elliptic values at algebraic arguments：**
```
basis = [1, G₄(0),
         K(k₁)², K(k₁)³, K(k₂)², K(k₂)³,
         K(k₁)²·K(k₂), ...]
```
其中 $k_1, k_2, \ldots$ 是 3D 闭合形式中出现的 moduli 和其他候选 singular moduli。

**Level 4 — Hypergeometric special values：**
```
basis = [1, G₄(0),
         ₃F₂(特殊参数; 1),
         ₄F₃(特殊参数; 1),
         ...]
```
这些来自 4D LGF 的 Kampé de Fériet 表示的特化。

**Level 5 — Mixed + exploratory：**
结合 Level 1-4 的元素，探索混合关系。

### 4.3 Multiplicative PSLQ vs Additive PSLQ

**Additive PSLQ（标准）：** 搜索 $\sum a_i x_i = 0$

**Multiplicative PSLQ：** 对 $\log G_4(0)$ 搜索，等价于找 $G_4(0) = \prod c_i^{a_i}$

实践中两者都要做：
1. 先做 additive（更常见的结果形式）
2. 再做 multiplicative（某些闭合形式天然是乘积形式）
3. 对 $G_4(0)^2$, $G_4(0)^{1/2}$ 等也做搜索（闭合形式可能涉及平方根）

### 4.4 搜索纪律

- 每次 PSLQ 运行记录：basis 描述、维度、使用精度、耗时、结果（relation 或 null）
- null result 也有价值：排除了某类闭合形式
- 关系找到后：将精度翻倍验证（从 1000 位 → 2000 位）
- 小系数（|aᵢ| < 100）的关系更可信
- 系数越大，需要的精度越高（经验法则：需要的精度 ≈ N·log₁₀(max|aᵢ|)）

---

## 5. 计算可行性详细评估

### 5.1 四维积分的降维方案

**方案 A: Bessel integral（推荐首选）**

$$G_4(0) = \int_0^{\infty} e^{-4t} \left[I_0(t)\right]^4 dt$$

这是一维积分！但 $I_0(t)^4$ 在高精度下计算较慢。

**性能估计：**
- mpmath `besseli(0, t)` 在 2000 dps 下：每次调用 ~10-50ms
- 被积函数指数衰减，积分区间有效截断在 $t \lesssim 50$
- 自适应 quadrature 需要 ~1000-5000 function evaluations
- **估计总时间：** 2000 dps → **数小时到 1-2 天**

**方案 B: 级数展开（可能更快）**

从 Guttmann 的 4D ODE 推导递推关系，计算 Taylor 系数 $a_n$。

$$G_4(0) = \sum_{n=0}^{\infty} a_n$$

递推关系一旦建立，计算每个 $a_n$ 是多项式时间。需要 $O(N)$ 项达到 $O(N)$ 位精度（取决于收敛率）。

**性能估计：**
- 递推计算：主要是大数乘除，2000 dps 下每项 ~1ms
- 如果需要 $10^4$ 项：~10 秒
- 加上 Richardson extrapolation 或 Euler-Maclaurin 加速
- **估计总时间：** 2000 dps → **分钟到小时级别**

**方案 C: 逐步解析积分**

将 4 重积分降为 3 重（解析积掉一维）：
$$G_4(0) = \frac{1}{\pi^3} \int_0^{\pi}\int_0^{\pi}\int_0^{\pi} \frac{dk_1\,dk_2\,dk_3}{\sqrt{(4 - \cos k_1 - \cos k_2 - \cos k_3)^2 - 1}}$$

（注意：这里的具体形式需要仔细推导，上面只是示意）

3 重积分用 mpmath `quad` 在高精度下非常慢。**不推荐用于 2000+ 位。**

**方案 D: Binomial coefficient 公式（4D SC 特有）**

Guttmann 2009 给出 4D SC lattice 的 Taylor 系数有闭合形式：
$$a_n = \sum_{k} \binom{2k}{k}^2 \binom{2(n-k)}{n-k}^2 / 16^n$$

（具体形式需从论文确认）

这使得级数法高度可行，因为每个系数可以精确计算。

### 5.2 推荐计算路径

```
Phase 2 计算路径：

1. 先用方案 D（binomial 系数递推）快速得到 ~500 位
   → 与文献数值对比验证
   
2. 用方案 B（ODE 递推 + Richardson）推到 2000+ 位
   → 这是主力方法

3. 用方案 A（Bessel integral）独立验证到 500-1000 位
   → 交叉验证

4. 如果方案 B 遇到收敛问题，用方案 A 推到 2000 位
   → 备选主力
```

### 5.3 内存估计

- mpmath 2000 dps 每个数字 ≈ 1KB
- 递推法：需要存储 O(N) 个系数，N ~ 10⁴
- 总内存：~10MB — **完全在 8GB 限制内**
- PSLQ 运行：basis 维度 M，需要 O(M²) 个高精度数，M ~ 20-50
- PSLQ 内存：~100MB — **无问题**

### 5.4 瓶颈分析

| 计算步骤 | 预计时间 | 瓶颈 | 优化策略 |
|---------|---------|------|---------|
| Bessel integral 2000dps | 数小时-2天 | besseli 调用 | 用级数展开替代 mpmath besseli |
| ODE 递推 2000dps | 分钟-小时 | 大数运算 | gmpy2 后端 |
| PSLQ 搜索（单次） | 秒-分钟 | basis 维度 | 控制 M ≤ 30 |
| 全部 PSLQ 搜索 | 小时-天 | 搜索空间 | 层级策略，先粗后细 |

### 5.5 关键优化

1. **安装 gmpy2：** `pip install gmpy2`，mpmath 会自动使用，大数运算加速 3-10x
2. **Bessel function 自建级数：** 对于固定精度的多次调用，预计算 $I_0(t)$ 的 Taylor 系数，避免重复计算
3. **并行化：** 虽然只有 4 核，可以并行运行 4 个独立的 PSLQ 搜索
4. **增量精度：** 先用 500 位快速扫描 basis 空间，有发现再用 2000 位确认

---

## 6. 风险评估 + Plan B

### Risk 1: 4D LGF 没有 "简单" 闭合形式（概率：40%）

**描述：** $G_4(0)$ 不能用已知特殊常数的有限组合表示，或者需要超大系数。

**影响：** 核心目标无法达成。

**Plan B：**
- 即使没有闭合形式，高精度数值本身就有价值（目前文献中 4D/5D 精度有限）
- 报告 null result：PSLQ 证明 $G_4(0)$ 不满足 degree ≤ N 的代数关系，排除特定形式
- 转向发现**近似关系**或**渐近关系**（类似于 Ramanujan 的经验公式）
- 寻找 $G_d(0)$ 在 $d \to \infty$ 时的渐近展开的精确系数
- 论文可以写成 "Systematic search for closed forms of higher-dimensional LGFs: methods and null results"

### Risk 2: 高精度计算遇到技术障碍（概率：20%）

**描述：** 2000 位精度的计算太慢（超过 1 周）或数值不稳定。

**影响：** 延迟项目，降低 PSLQ 的搜索能力。

**Plan B：**
- 降低精度目标到 500-1000 位（仍然足以发现简单关系）
- 使用 ODE 递推法代替直接数值积分
- 考虑用 Arb（C 语言 arbitrary precision library）替代 mpmath 获得更好性能
- 极端情况：租用临时云算力（几美元可得 32 核几小时）

### Risk 3: Basis 选择不对（概率：35%）

**描述：** 闭合形式涉及我们没有预见到的特殊常数（例如某些未知 Calabi-Yau periods）。

**影响：** PSLQ 搜索全部返回 null。

**Plan B：**
- 系统地扩大搜索范围：加入 hypergeometric 特殊值
- 利用 Guttmann 2009 的 ODE 结构，从 local solutions 的 Frobenius 展开中寻找线索
- 检查 ODE 在 singular points 的 monodromy，推断 periods 的性质
- 咨询 Broadhurst/Koutschan 等专家的意见（通过 email）

### Risk 4: 结果已被他人发表（概率：10%）

**描述：** 在研究进行中，有人发表了类似结果。

**影响：** 失去新颖性。

**Plan B：**
- Phase 1 彻底检查 arXiv，之后每两周刷一次
- 如果被抢：转向强调方法论创新（PSLQ 在 LGF 领域的系统应用）
- 或者转向其他格点类型/维度

### Risk 5: 发现了关系但无法证明（概率：25%，条件在 PSLQ 成功）

**描述：** PSLQ 找到了 $G_4(0)$ 的闭合形式候选，但严格证明超出能力范围。

**影响：** 论文只能声称 conjecture。

**Plan B：**
- Experimental Mathematics 和类似期刊接受 well-supported conjectures
- 验证到 2000+ 位本身就是极强证据
- 如果 conjecture 足够漂亮，会吸引理论家来证明
- 这实际上是一个很好的结果——类似 BBP 公式最初也是 experimental discovery

---

## 7. 里程碑和 Go/No-Go 决策点

### Milestone 1: 理论准备完成（Week 2 末）
- **交付物：** 完整理论笔记 + PSLQ basis 候选列表
- **Go/No-Go：** 如果发现 4D 闭合形式已被他人找到 → 调整方向

### Milestone 2: 3D Benchmark 通过（Week 4 末）
- **交付物：** $G_3^{SC}(0)$ 计算到 2000 位，与 Joyce 闭合形式完全吻合
- **Go/No-Go：** 如果 2000 位精度耗时超过 3 天 → 评估优化方案或降低精度目标
- **关键指标：** 3D PSLQ 能重新发现 Joyce 闭合形式

### Milestone 3: 4D 高精度计算完成（Week 5 末）
- **交付物：** $G_4(0)$ 到 2000+ 位，至少两种方法交叉验证
- **Go/No-Go：** 如果只能算到 < 500 位 → 降低 PSLQ 搜索范围，专注简单关系

### ⭐ Milestone 4: PSLQ 初步搜索完成（Week 8 末）— **关键决策点**
- **交付物：** Level 1-3 basis 搜索完成
- **情景分析：**
  - **找到候选关系：** → 全力验证和扩展（Phase 4A）
  - **Level 1-3 全部 null：** → 评估是否继续 Level 4-5 或转向 Plan B
  - **发现有趣的 partial pattern：** → 调整方向深入

### Milestone 5: 论文初稿完成（Week 12 末）
- **交付物：** 完整论文初稿
- **Go/No-Go：** 自评论文贡献是否足够投稿目标期刊

### Milestone 6: 投稿（Week 14 末）
- **交付物：** 投稿确认

---

## 8. 论文结构草案

### 8.1 预期章节

```
1. Introduction
   - LGF 的物理和数学重要性
   - 已知闭合形式的历史（Watson → Joyce）
   - 4D 及以上的 open problem
   - 本文贡献概述

2. Mathematical Preliminaries
   - LGF 定义和基本性质
   - Bessel function 表示
   - 与 Calabi-Yau ODE 的联系

3. High-Precision Computation of G_d(0)
   - 计算方法（ODE 递推 / Bessel integral）
   - 精度验证和交叉检验
   - 数值结果

4. PSLQ Search for Closed-Form Expressions
   - Basis 选择的理论依据
   - 搜索策略
   - 结果（正结果或 null results）

5. [如果有发现] The Closed-Form Expression
   - 闭合形式的陈述
   - 数值验证
   - 证明/推导（如果可能）

6. Discussion
   - 与已知结果的联系
   - 对更高维度的含义
   - 开放问题

7. Conclusion

Appendix A: High-precision numerical values (100+ digits)
Appendix B: Computational details and code availability
```

### 8.2 三种情景

#### 🟢 乐观情景：找到 4D 闭合形式

**论文标题：** "Closed-form expression for the four-dimensional hypercubic lattice Green function"

**核心贡献：** 数学物理中一个 30+ 年 open problem 的解决

**投稿目标：**
1. **J. Phys. A: Math. Theor.** (Letter 形式，快速发表) — 首选
2. **Physical Review Letters** (如果结果足够惊人)
3. **Experimental Mathematics** (如果证明不完整，只有 conjecture)

**预计影响：** 高引用，可能吸引 Calabi-Yau 社区关注

#### 🟡 中性情景：发现有趣的 partial results

例如：找到 $G_4(0)$ 与某些已知常数的非平凡近似关系，或发现 $G_4(0)$ 满足某个新的代数恒等式。

**论文标题：** "Integer relation detection for higher-dimensional lattice Green functions: new identities and conjectures"

**投稿目标：**
1. **Experimental Mathematics** — 首选（该期刊专门接收计算驱动的发现）
2. **J. Phys. A: Math. Theor.** (如果结果物理意义明确)

#### 🔴 悲观情景：全面 null result

**论文标题：** "High-precision computation and systematic closed-form search for lattice Green functions in four and five dimensions"

**核心贡献：**
- 4D/5D LGF 的前所未有精度数值（2000+ 位）
- 系统排除特定闭合形式类别的证据
- 方法论贡献：PSLQ 在 lattice physics 中的系统应用

**投稿目标：**
1. **J. Phys. A: Math. Theor.** — 仍然可以投（高精度数值 + 方法论）
2. **Computer Physics Communications** — 偏重计算方法
3. **Experimental Mathematics** — null result 如果足够系统也可以接收

---

## 9. 投稿策略

### 9.1 J. Phys. A: Mathematical and Theoretical（首选）

**出版商：** IOP Publishing

**格式要求：**
- LaTeX 模板：使用 IOP 的 `iopart` 文档类
  ```latex
  \documentclass[12pt]{iopart}
  ```
- 下载地址：`https://publishingsupport.iopscience.iop.org/`
- 参考文献格式：数字引用 `[1]`，按引用顺序排列
- 摘要：≤ 150 词，单段
- 关键词：3-10 个
- 图表嵌入正文中
- 投稿系统：ScholarOne

**优势：**
- LGF 研究的传统阵地（Joyce, Guttmann, Koutschan 都发在这里）
- 审稿人可能就是领域专家
- 接收 mathematical physics 交叉论文

**注意事项：**
- 强调物理 motivation 和数学严谨性
- 如果只是 conjecture，要明确标注

### 9.2 Experimental Mathematics（Taylor & Francis）

**格式要求：**
- LaTeX 投稿，标准 article 格式
- 使用 `amsmath`, `amssymb` 包
- 参考文献：author-date 或数字格式（查看最近论文确认）
- 投稿系统：Taylor & Francis 在线系统
- 代码/数据最好提供 supplementary material

**优势：**
- 专门接收 computational/experimental 方法驱动的发现
- PSLQ 相关工作的天然归宿（Bailey, Borwein 都在此发表）
- 接收 well-supported conjectures（不要求严格证明）
- 影响因子 0.9（不高，但领域内受尊重）

**注意事项：**
- 强调方法论的系统性
- 代码可复现性很重要
- Null results 如果系统且有意义也可接收

### 9.3 投稿优先级和策略

```
发现闭合形式（proven）:
  → J. Phys. A (Letter) → PRL → full paper in J. Phys. A

发现闭合形式（conjecture, 2000+ 位验证）:
  → Experimental Mathematics → J. Phys. A

Partial results + 高精度数值:
  → J. Phys. A → Experimental Mathematics

Null result + 方法论:
  → J. Phys. A → Computer Physics Communications → Experimental Mathematics
```

**时间线注意：** arXiv preprint 应该在投稿同时或之前发布，确保优先权。

---

## 10. 立即行动清单（Phase 1 第一周）

### Day 1-2: 关键论文获取

- [ ] 下载 Glasser & Guttmann 1994 (arXiv: `cond-mat/9408097`) — **最关键**
- [ ] 下载 Guttmann 2009 (DOI: `10.1088/1751-8113/42/23/232001`) — **最关键**
- [ ] 下载 Joyce 1994 (DOI: `10.1098/rspa.1994.0072`)
- [ ] 下载 Joyce 2002 (DOI: `10.1088/0305-4470/35/46/307`)
- [ ] 下载 Koutschan 2013 (arXiv: `1108.2164`)
- [ ] 下载 Bailey et al. 2008 (arXiv: `0801.0891`)
- [ ] 检查 Lattice Sums Then and Now 是否有电子版

### Day 2-3: 精读 + 笔记

- [ ] 精读 Guttmann 2009：**提取 4D SC lattice LGF 的具体 ODE**
  - 写出 ODE 的精确形式
  - 理解 Calabi-Yau 性质的含义
  - 记下 Taylor 系数的递推关系（如果论文给出）
- [ ] 精读 Glasser & Guttmann 1994：**提取 4D 的 Kampé de Fériet 表示和已知数值**
  - 记录 $G_4(0)$ 的已知精度
  - 理解 Kampé de Fériet → 级数的展开

### Day 3-4: 代码环境搭建

- [ ] 确认 Python 环境：`python3 -c "import mpmath; print(mpmath.__version__)"`
- [ ] 安装 gmpy2：`pip install gmpy2`（如果没有的话）
- [ ] 创建项目目录结构：
  ```
  lgf-research/
  ├── src/
  │   ├── lgf_compute.py     # 高精度 LGF 计算
  │   ├── pslq_search.py     # PSLQ 搜索框架
  │   ├── constants.py       # 特殊常数的高精度值
  │   └── utils.py           # 工具函数
  ├── data/
  │   ├── numerical/         # 高精度数值结果
  │   └── pslq_logs/         # PSLQ 搜索日志
  ├── notes/
  │   ├── literature/        # 文献笔记
  │   └── theory/            # 理论推导
  └── paper/                 # 论文 LaTeX
  ```
- [ ] 写一个快速 benchmark：计算 $G_3^{SC}(0)$ 到 100 位
  ```python
  from mpmath import mp, quad, besseli, exp, inf
  mp.dps = 120
  G3 = quad(lambda t: exp(-3*t) * besseli(0,t)**3, [0, inf])
  print(G3)
  # 应该得到 1.5163860591903...
  ```

### Day 4-5: 理论推导

- [ ] 独立推导 Bessel integral 表示：
  $$G_d(0) = \int_0^{\infty} e^{-dt} [I_0(t)]^d dt$$
  从 Fourier 积分出发，利用 $I_0(t) = \frac{1}{\pi}\int_0^{\pi} e^{t\cos\theta} d\theta$
- [ ] 对 4D 情况写出 3 重积分（解析积掉一维）的具体形式
- [ ] 从文献中提取或自己推导 4D SC 的 Taylor 系数公式

### Day 5-7: 初步数值实验

- [ ] $G_3^{SC}(0)$ Bessel method → 500 位（计时）
- [ ] $G_4^{SC}(0)$ Bessel method → 100 位（计时，评估 2000 位可行性）
- [ ] 如果 Guttmann ODE 已提取 → 实现 ODE 递推法 → 100 位
- [ ] **Week 1 结束时的判断：** 最优计算路径是什么？2000 位需要多久？

---

## 附录 A: 关键数值参考

（从文献中收集，作为 benchmark）

| 量 | 已知数值 | 来源 |
|----|---------|------|
| $G_3^{SC}(0)$ | 1.516386059190396... | Joyce 1994 闭合形式 |
| $G_4^{SC}(0)$ | 1.239465... | Glasser-Guttmann 1994 |
| $G_5^{SC}(0)$ | 1.156528... | 文献待确认 |
| $P_3^{SC}$ (return prob) | 0.340537... | 经典结果 |
| $P_4^{SC}$ | 0.193206... | 经典结果 |

注意：上述低精度数值需要在 Phase 2 中大幅扩展。

## 附录 B: PSLQ 判断标准速查

1. **Relation found:** $\min \|H_j\| / \max \|H_j\|$ 突然下降 > $10^{100}$
2. **精度要求：** 如果 basis 有 M 个元素，最大系数 ≤ C，需要精度 > $M \cdot \log_{10}(C) + 50$ 位
3. **Null result 的含义：** 如果 PSLQ 在精度 D 下对 M 维 basis 返回 null，则不存在系数 $|a_i| \leq 10^{D/M - \epsilon}$ 的整数关系
4. **可信度：** 小系数（< 100）的关系在 1000+ 位下发现 → 几乎确定是真的

---

*最后更新：2026-03-18*
*下次 review：Phase 1 结束时（~Week 2）*
