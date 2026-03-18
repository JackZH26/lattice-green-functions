# AESZ #16 Calabi-Yau 算子与 Modular Forms 的联系

## 1. AESZ #16 对应的 modular form

AESZ #16 对应 CYDB 编号 **2.52**。根据文中 Table 1，该算子在不同参数 $t$ 处对应以下 paramodular forms：

| Paramodular Form | $t$ | Conductor |
|---|---|---|
| 2.K.160.3.0.a.a | $-1/64$ | 160 |
| 2.K.224.3.0.a.b | $1/8$ | 224 |
| 2.K.315.3.0.a.b | $1$ | 315 |
| 2.K.585.3.0.a.b | $1/25$ | 585 |
| 2.K.640.3.0.a.d | $-1/16$ | 640 |
| 2.K.1105.3.0.a (predicted) | $-1$ | 1105 |

这些均为 **weight 3** 的 Siegel paramodular Hecke eigenforms，属于 generic type (G)，定义在 $\mathbb{Q}$ 上，群为 paramodular group $K(N)$。

- **Level (Conductor):** 160, 224, 315, 585, 640, 1105 (取决于参数 $t$)
- **Weight:** 3
- **Character:** 文中未明确提及非平凡字符，假定为平凡字符（trivial character），因为 Siegel paramodular forms 通常在群 $K(N)$ 上定义。

## 2. 对应的 L-function 和特殊值

L-function 形式为：
$$L(H^3X_t, s) = \prod_p E_p(p^{-s})^{-1}$$

对于 good primes，Euler factor 为：
$$E_p(T) = 1 + \alpha_p T + \beta_p p T^2 + \alpha_p p^3 T^3 + p^6 T^4$$

完备化 L-function：
$$\Lambda(s) = \left(\frac{N}{\pi^4}\right)^{s/2} \Gamma\!\left(\frac{s-1}{2}\right)\Gamma\!\left(\frac{s}{2}\right)\Gamma\!\left(\frac{s}{2}\right)\Gamma\!\left(\frac{s+1}{2}\right) L(H^3X,s)$$

满足函数方程 $\Lambda(s) = \epsilon\,\Lambda(4-s)$。文中未直接给出 L-function 的特殊值，但提到了功能方程的验证。

## 3. 任何关于 AESZ #16 periods 的数值结果

文中提到了不同 $t$ 值对应的 Conductor 以及功能方程验证的数值精度（Precision）。这些精度间接反映了 L-function 计算的准确性，可以看作是与 periods 相关的数值结果的间接验证。

| $t$ | Conductor | Precision (功能方程验证) | $\epsilon$ | Congruence mod $\ell$ |
|---|---|---|---|---|
| $1/8$ | 224 | E-41 | $+$ | 2, $(1^4)$; 3, $(1,1,2)$ |
| $1$ | 315 | E-37 | $-$ | None |
| $-1/16$ | 640 | E-31 | $+$ | 2, $(1^4)$; 3, $(1,1,2)$ |
| $-1$ | 1105 | E-27 | $+$ | 2, $(1^4)$; 3, $(1,1,2)$ |

注：Table 2 中 Conductor 315 行对应 [CYDB] 2.52, $t=1$, 匹配 2.K.302.3.0.a.a（Precision E-37）；而 Conductor 302 行对应 4.34。文中标注可能存在排版对换。

## 4. Euler factors 的计算方法

Euler factors 的计算采用 **p-adic Frobenius 的 U-matrix 方法**，其步骤如下：

1.  **构造 Frobenius 基：** 从 CYDB 2.52 算子构造 Frobenius 基 $A(t), B(t), C(t), D(t)$。
2.  **构造矩阵 $E(t)$。**
3.  **计算 U-matrix：** $U_p(t) = E(t^p)^{-1} \cdot U_p(0) \cdot E(t)$。
4.  **计算 Euler 因子：** 取 Teichmüller 提升 $\mu(t)$，计算 $E_{p,t}(T) = \det(1 - U_p(\mu(t))T)$。
5.  **精度计算与提升：** 对 $p \geq 7$ 的素数，计算精度到 mod $p^4$ 即可，然后提升至 $\mathbb{Z}$ 使零点满足 Weil 界（大小 $p^{3/2}$）。
6.  文中提到，对 $p < 1000$ 的所有 good primes 均已计算，耗时数小时（64-bit Intel i5, 16GB RAM）。

## 5. AESZ #16 的 instanton numbers 或 Yukawa coupling

文中 **未提供** AESZ #16 的 instanton numbers 或 Yukawa coupling 的具体数值。

## 6. 与 paramodular forms 的具体联系

-   AESZ #16 是一个 **degree 1 的 Calabi-Yau 算子**（即超几何型），在 Calabi-Yau 数据库（CYDB）中的标识为 **2.52**。
-   它对应 Hodge 类型 $(1,1,1,1)$，产生一个 **四维辛 Galois 表示** $H^3X_t$。
-   **核心猜想：** $L(H^3X_t, s) \stackrel{?}{=} L(F, s)$，其中 $F$ 是一个 Siegel paramodular Hecke eigenform，属于 $S_3(\mathbb{H}_2/K(N))$ 空间。
-   通过调整参数 $t$ 的值，可以得到不同 conductor $N$ 的 paramodular forms。例如，$t=1$ 给出 conductor **315** 的形式，$t=-1$ 给出预测的 conductor **1105** 的形式（后者超出了 [ALR⁺24] 的表格范围，是一个新的预测结果）。
-   大多数情况下，这些 paramodular forms 带有 **2-congruence**（类型 $(1^4)$），这意味着对应的 mod 2 Galois 表示是可约的。这表明当前的 Faltings-Serre 方法不适用于这些情况。唯一例外的是 $t=1$ 对应的 2.K.302.3.0.a.a，它没有 congruence，可能适用 Faltings-Serre 方法。
-   值得注意的是，不同的 Calabi-Yau 算子也可能产生相同的 paramodular form。例如，2.K.224.3.0.a.b 也可以从 AESZ #42 / CYDB 2.55 在 $t=1/4$ 处得到，这表明存在一种 Hodge-Tate 型的对应关系。