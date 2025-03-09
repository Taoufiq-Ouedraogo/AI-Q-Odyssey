import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from pages.utils import utils_page

utils_page.set_st_page2("Compound Interest Tool")
st.title("💸 Compound Interest vs. Simple Interest")

# Adding custom CSS to style the page
st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
        font-family: 'Arial', sans-serif;
    }
    h1 {
        color: #2a7ae2;
    }
    h2 {
        color: #3a3a3a;
    }
    .stButton>button {
        background-color: #2a7ae2;
        color: white;
        font-size: 16px;
        font-weight: bold;
    }
    .stSlider>div>div>input {
        background-color: #f1f3f6;
        border-radius: 10px;
    }
    .stTextInput>div>div>input {
        background-color: #f1f3f6;
        border-radius: 10px;
    }
    .stMarkdown {
        color: #333;
        font-size: 18px;
    }
    .stDataFrame {
        background-color: #f7f7f7;
        border-radius: 10px;
    }
    .kpi-card {
        background-color: #f7f7f7;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        font-size: 24px;
    }
    .kpi-title {
        font-size: 20px;
        color: #4a4a4a;
    }
    .kpi-value {
        font-size: 28px;
        font-weight: bold;
    }

    /* Custom CSS for col2 */
    .col2 {
        background-color: #f0f8ff;  /* Light blue color for col2 */
        padding: 20px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Create a two-column layout: plot on the left and input parameters on the right
col1, col2 = st.columns([4, 1])  # Adjusted the ratio for a smaller col2

# Input parameters part goes into the second column
with col2:
    st.markdown('<div class="col2">', unsafe_allow_html=True)  # Apply custom CSS for col2
    # Input Parameters from User
    S_0 = st.number_input("Initial Investment (S₀) in USD:", min_value=1.0, value=2000.0)
    # Slider for Annual Interest Rate
    r = st.slider("Annual Interest Rate (r) in %:", min_value=0.0, max_value=100.0, value=7.0, step=0.1)

    n = st.number_input("Number of Years (n):", min_value=1, value=20)
    P = st.number_input("Monthly Contribution (P) in USD:", min_value=0.0, value=200.0)

    # Compounding Frequency Selection
    compounding_options = {
        "Yearly": 1,
        "Semi-Annually": 2,
        "Quarterly": 4,
        "Monthly": 12,
        "Weekly": 52,
        "Daily": 365
    }
    T = st.selectbox("Compounding Frequency (T):", options=list(compounding_options.keys()), index=3)

    # Convert compounding frequency to corresponding number
    T_value = compounding_options[T]

    # Convert interest rate from percentage to decimal
    r = r / 100
    st.markdown('</div>', unsafe_allow_html=True)  # End custom CSS for col2


# Plotting and calculation part goes into the first column
with col1:
    # Calculate Compound Interest and Simple Interest and prepare data for charting
    time = np.arange(0, n + 1, 1)  # Time from 0 to n years

    # Compound Interest Growth with Contributions
    A_with_contrib = (S_0 + P * 12 * time) * (1 + r / T_value) ** (T_value * time)

    # Simple Interest Growth (just initial + monthly contributions)
    A_simple = S_0 * (1 + r * time) + P * 12 * time  # Corrected formula for Simple Interest growth

    # Total Contributions (without interest)
    total_contributions = P * 12 * time  # Monthly contributions over the years
    total_contributions += S_0

    # Show the final amount
    final_amount_CI = A_with_contrib[-1]
    final_amount_SI = A_simple[-1]
    final_amount_ending_balance = final_amount_CI + final_amount_SI  # Ending balance combining both

    # Plotting the compound interest growth, simple interest, and total contributions over time using Plotly
    fig = go.Figure()

    # Bar plot for Compound Interest Growth at each year (green)
    fig.add_trace(go.Bar(x=time, y=A_with_contrib, name="Compound Interest Growth", marker_color='green', opacity=0.5))

    # Line plot for Compound Interest Growth with Contributions (green)
    fig.add_trace(go.Scatter(x=time, y=A_with_contrib, mode='lines+markers', name="Compound Interest Growth", line=dict(color='green', width=2)))

    # Bar plot for Simple Interest Growth at each year (red)
    fig.add_trace(go.Bar(x=time, y=A_simple, name="Simple Interest Growth", marker_color='red', opacity=0.5))

    # Line plot for Simple Interest Growth (red)
    fig.add_trace(go.Scatter(x=time, y=A_simple, mode='lines+markers', name="Simple Interest Growth", line=dict(color='red', width=2)))

    # Bar plot for Total Contributions (blue)
    fig.add_trace(go.Bar(x=time, y=total_contributions, name="Total Contributions", marker_color='blue', opacity=0.5))

    # Line plot for Total Contributions (blue)
    fig.add_trace(go.Scatter(x=time, y=total_contributions, mode='lines+markers', name="Total Contributions", line=dict(color='blue', width=2, dash='dash')))

    # Enhancing the Layout of the Plot
    fig.update_layout(
        title=f"Compound vs. Simple Interest Growth over {n} years with {T} Compounding",
        xaxis_title="Years",
        yaxis_title="Amount (USD)",
        template="plotly_dark",
        plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
        showlegend=True,
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
        # Increase size of the plot
        width=1500,  # Set width
        height=600  # Set height
    )

    # Show the Plotly graph
    st.plotly_chart(fig)

# KPI Cards for Simple Interest, Compound Interest, and Ending Balance
col1_kpi, col2_kpi, col3_kpi = st.columns(3)

with col1_kpi:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Simple Interest</div>
        <div class="kpi-value">${final_amount_SI:,.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with col2_kpi:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Compound Interest</div>
        <div class="kpi-value">${final_amount_CI:,.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with col3_kpi:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Ending Balance</div>
        <div class="kpi-value">${final_amount_ending_balance:,.2f}</div>
    </div>
    """, unsafe_allow_html=True)

# Displaying a table of the results for each year with a visually appealing table
df = pd.DataFrame({
    "Year": time,
    "Compound Interest (USD)": A_with_contrib,
    "Simple Interest (USD)": A_simple,
    "Total Contributions (USD)": total_contributions
})

st.markdown("<br><br>", unsafe_allow_html=True)

st.subheader("📊 Yearly Breakdown")
st.dataframe(df, use_container_width=True)

# Additional suggestions or information (for a more engaging user experience)
st.markdown("""
    <br><br>
    💡 **Tip**: Regular monthly contributions can significantly boost your investment over time, especially with a long compounding period! 🚀
""", unsafe_allow_html=True)