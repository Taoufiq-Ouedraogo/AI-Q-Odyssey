import os
import streamlit as st
from pages.utils import utils_page

utils_page.set_st_page2("Option Pricing Methods")

st.title("Option Pricing Methods")


st.image('pages/img/option_price_comp.png', width=100, use_container_width=True)


st.markdown(r"""
### Option Value: Intrinsic & Time Value

An option's price consists of two main components:

$$\textbf{Option Value = Intrinsic Value + Time Value}$$

- **Intrinsic Value**: The option's immediate exercise value, i.e., the difference between the underlying price and strike price (if positive).
- **Time Value**: The additional value attributed to the time remaining until expiration.
  - This represents the probability of the option becoming more valuable before expiry.
  - The more time left, the higher the time value.

---
            


### Option Pricing Methods

When pricing options, we assume the **No-Arbitrage Principle** and **Risk-Neutrality**. The core idea is to:

1. Model the evolution of the underlying asset.
2. Compute the expected payoff at expiration.
3. Discount the expected payoff using the risk-free rate.

Option pricing methods fall into two broad categories:

#### 1. **Analytic Methods** (Closed-form solutions)
These use mathematical formulas for direct pricing.

- **Black-Scholes Model**: Assumes log-normal stock price movement.
- **CEV, Heston, Merton Models**: Introduce stochastic volatility or jumps.
- **Fourier & Laplace Transforms**: Alternative closed-form solutions.

#### 2. **Numerical Methods** (Approximations)
Used when closed-form solutions are unavailable (e.g., American options).

- **Tree-based Methods**: Binomial & Trinomial Trees.
- **Finite Difference Methods**: PDE-based pricing.
- **Monte Carlo Simulation**: Uses random sampling to approximate the price.

---

### 1. Binomial & Trinomial Trees

These methods discretize price movements into steps:

- **Binomial Tree**: At each step, price moves up or down by a fixed factor.
- **Trinomial Tree**: Allows up, down, and unchanged moves.

The stock price evolution follows:

$$ S_{t+\Delta t} = S_t \times u \quad \text{or} \quad S_t \times d $$

where:
- $u = e^{\sigma\sqrt{\Delta t}}$ (up move)
- $d = e^{-\sigma\sqrt{\Delta t}}$ (down move)
- $p = \frac{e^{r\Delta t} - d}{u - d}$ (risk-neutral probability)

---

### 2. Geometric Brownian Motion (GBM)

Stock prices are often modeled as:

$$ dS_t = \mu S_t dt + \sigma S_t dW_t $$

where:
- $\mu$ = drift (expected return)
- $\sigma$ = volatility
- $W_t$ = Wiener process

GBM is the foundation of the **Black-Scholes model**.

---

### 3. Black-Scholes Model

A fundamental model for pricing European options:

$$ C = S_0 N(d_1) - Ke^{-rt} N(d_2) $$

where:
- $d_1 = \frac{\ln(S_0/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$
- $d_2 = d_1 - \sigma\sqrt{T}$

$ N(d)$ is the cumulative normal distribution function.

---

### 4. Stochastic Volatility & Jump Models

#### **Constant Elasticity of Variance (CEV) Model**

The volatility scales with stock price:

$$ dS_t = \mu S_t dt + \sigma S_t^{\beta} dW_t $$

where $ \beta$ controls elasticity.

#### **Heston Model (Stochastic Volatility)**

Introduces stochastic variance:

$$ dS_t = \mu S_t dt + \sqrt{v_t} S_t dW_t^S $$
$$ dv_t = \kappa(\theta - v_t)dt + \sigma_v \sqrt{v_t} dW_t^v $$

where \( v_t \) is variance, mean-reverting to \( \theta \).

#### **Merton Jump-Diffusion Model**

Adds jump processes:

$$ dS_t = (\mu - \lambda k) S_t dt + \sigma S_t dW_t + J S_t dq_t $$

where jumps \( J \sim LogNormal(m, s) \) occur randomly.

---

### 5. Monte Carlo Simulation

Used for complex payoffs:

1. Simulate thousands of stock price paths using:

   $$ S_{t+\Delta t} = S_t e^{(r - \frac{1}{2}\sigma^2)\Delta t + \sigma\sqrt{\Delta t}Z} $$

2. Compute the option payoff for each path.
3. Discount the expected payoff to present value.

Monte Carlo is powerful but computationally expensive.

---

### Summary

| Method | Type | Best For |
|--------|------|----------|
| Binomial/Trinomial Trees | Numerical | American options, early exercise |
| Black-Scholes | Analytic | European options, simple assumptions |
| CEV, Heston, Merton | Advanced | Stochastic volatility, jumps |
| Monte Carlo | Numerical | Complex payoffs, path-dependent options |

Each method has strengths, and choosing the right one depends on the option type and market conditions.
""")


