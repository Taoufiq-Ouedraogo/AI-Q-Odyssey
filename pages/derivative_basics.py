import streamlit as st
from pages.utils import utils_page

utils_page.set_st_page2("Basics of Derivatives")
st.title("📘 Basics of Derivatives")

st.markdown("""
### 📌 What are Derivatives?
**Derivatives** are financial instruments whose value is derived from an underlying asset (stocks, bonds, commodities, interest rates, or currencies).

- Can be traded on **Exchanges** or **Over-The-Counter (OTC)**
- Example: A **Mortgage-Backed Security (MBS)** is a type of derivative backed by a pool of home loans.
""")


st.image('pages/img/why_use_dervivatives.png', width=350, use_container_width=True)


st.markdown("### 🔹 Types of Derivatives")
st.write("- **Forward Contracts**")
st.write("- **Futures Contracts**")
st.write("- **Options**")
st.write("- **Swaps**")


# 📌 Table 1: Long & Short Positions
st.markdown("### 🔄 Long & Short Positions")
position_data = {
    "Position": ["📥 Long Position (Buyer)", "📤 Short Position (Seller)"],
    "Meaning": [
        "- Buying or holding a derivative contract\n- Benefits from rising asset price",
        "- Selling or writing a derivative contract\n- Benefits from falling asset price"
    ]
}
st.table(position_data)



# 📌 Table 2: Key Components of Derivatives
st.markdown("### ⚙️ Key Components of Derivatives")
components_data = {
    "Component": ["Underlying Asset", "Maturity (Expiration Date)", "Strike Price"],
    "Meaning": [
        "- The asset upon which a derivative is based\n- Price fluctuations determine the derivative's value",
        "- The date when the contract is settled",
        "- The pre-agreed price at which the holder can buy/sell the asset (applies to Options)"
    ]
}
st.table(components_data)



# 📌 Expander for Forward Contracts
with st.expander("📜 **Forward Contracts**"):
    st.markdown("""
    **Forward Contracts** are customized agreements where two parties agree to buy/sell an asset at a fixed price in the future.
    
    **Characteristics:**
    - 🔹 **Over-The-Counter (OTC)**: Privately negotiated, flexible terms
    - 📜 **Customizable**: Asset, quantity, and settlement date are tailored
    - ⚠️ **Higher Credit Risk**: No margin requirements, increasing default risk

    **Benefits:**
    - ✅ **Risk Management**: Locks in future prices, reducing uncertainty
    - 📈 **For Buyers (Long)**: Protection against price increases
    - 📉 **For Sellers (Short)**: Guarantees a fixed selling price, mitigating losses
    """)



# 📌 Expander for Future Contracts
with st.expander("📜 **Futures Contracts**"):
    st.markdown("""
    **Futures Contracts** are standardized agreements to buy/sell an asset at a fixed price in the future, traded on regulated exchanges.
    
    **Characteristics:**
    - 📏 **Standardized**: Terms (underlying, quantity, maturity) are fixed by the exchange
    - 💹 **Exchange-Traded**: No direct negotiation between parties
    - 🔒 **Lower Credit Risk**: Backed by clearinghouses, reducing counterparty risk
    - 💧 **Greater Liquidity**: Actively traded in high volumes
    """)



# 📌 Expander for Options
with st.expander("📜 **Options**"):
    st.markdown("""
    **Options** are financial contracts that grant the holder the right, but not the obligation, to buy or sell an asset at a predetermined price (Strike Price) before or on the expiration date.

    **Types of Options:**
    - 🟢 **Call Option**: Right to buy the underlying asset at the strike price
    - 🔴 **Put Option**: Right to sell the underlying asset at the strike price

    **Characteristics:**
    - 🔄 **Traded on Exchanges**: More regulated than OTC contracts
    - 📊 **Used for Hedging, Speculation, Leverage, and Arbitrage**
    - 🔍 **More Complex**: Various combinations of strikes and maturities

    **Comparison Table:**
    """)
    
    # Table: Call vs Put Options
    options_data = {
        "Feature": ["Right to", "Objective", "Best for"],
        "Call Option": ["Buy", "Profit from price increase", "Bullish traders"],
        "Put Option": ["Sell", "Profit from price drop", "Bearish traders"]
    }
    st.table(options_data)



# 📌 Expander for Swaps
with st.expander("📜 **Swaps**"):
    st.markdown("""
    **Swaps** are financial contracts in which two parties exchange cash flows or liabilities based on a predetermined agreement.

    **Common Types of Swaps:**
    - 🔄 **Interest Rate Swaps**: Exchange fixed interest rate payments for floating rate payments
    - 💱 **Currency Swaps**: Exchange cash flows in different currencies
    - 📈 **Commodity Swaps**: Exchange fixed price for variable price in commodities like oil or gold
    - 🏛️ **Credit Default Swaps (CDS)**: Used to hedge against credit risk

    **Why Use Swaps?**
    - ✅ **Risk Management**: Adjust exposure to interest rates or currencies
    - 📊 **Cost Reduction**: Obtain better borrowing terms
    - 🔁 **Flexibility**: Tailored to financial needs through OTC agreements
    """)



st.markdown("---")
st.info("✅ This section provides a structured introduction to **Derivatives, Forwards, and Futures** with interactive elements.")

