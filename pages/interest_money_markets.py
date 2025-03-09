import streamlit as st
from pages.utils import utils_page

# Set the page title and metadata
utils_page.set_st_page2("Interest & Money Markets")
st.title("📘 **Interest & Money Markets**")

# Adding custom CSS to style the page
st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
        font-family: 'Helvetica', sans-serif;
    }
    h1 {
        color: #2a7ae2;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #2a7ae2;
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 5px;
    }
    .stSlider>div>div>input {
        background-color: #f4f7f6;
        border-radius: 10px;
    }
    .stTextInput>div>div>input {
        background-color: #f4f7f6;
        border-radius: 10px;
    }
    .stMarkdown {
        color: #333;
        font-size: 18px;
        margin-bottom: 20px;
    }
    .formula {
        font-size: 26px;
        font-weight: bold;
        color: #4a4a4a;
        margin: 20px 0;
    }
    .variable-list {
        font-size: 18px;
        color: #555;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# Displaying the formulas with a bit more styling
st.markdown('<p class="formula">Compound Interest without Contributions:</p>', unsafe_allow_html=True)
st.latex(r"""
    A = \left(P + C \cdot n \cdot t \right) \left( 1 + \frac{r}{n} \right)^{nt}
""")

st.markdown('<p class="formula">Compound Interest with Contributions:</p>', unsafe_allow_html=True)
st.latex(r"""
    A = \left(P + C \cdot n \cdot t \right) \left( 1 + \frac{r}{n} \right)^{nt}
""")



st.markdown('<p class="formula">Simple Interest without Contributions:</p>', unsafe_allow_html=True)
st.latex(r"""
    SI= P \cdot \left( 1 + r \cdot t \right)  
""")

st.markdown('<p class="formula">Simple Interest with Contributions:</p>', unsafe_allow_html=True)
st.latex(r"""
    SI= P \cdot \left( 1 + r \cdot t \right) + C \cdot n \cdot t
""")

# Explanation of the variables in a nicely formatted list
st.markdown('<p class="formula">Variables in the Formulas:</p>', unsafe_allow_html=True)
st.markdown("""
    <ul class="variable-list">
        <li><strong> P </strong> = Principal (Initial Investment)</li>
        <li><strong> C </strong> = Periodic Contribution (Monthly)</li>
        <li><strong> r   </strong> = Annual Interest Rate (as a decimal)</li>
        <li><strong>  n   </strong> = Number of times the interest is compounded per year</li>
        <li><strong>  t  </strong> = Time (in years)</li>
    </ul>
""", unsafe_allow_html=True)

# Optional: Add some extra tips or explanation about compound vs simple interest
st.markdown("""
    <br><br>
    💡 **Tip**: Compound interest is often referred to as 'interest on interest', which means that you earn interest on the initial investment and also on the interest that accumulates each period. On the other hand, simple interest is only calculated on the principal amount throughout the investment period. Compound interest usually results in a higher return over time, especially with longer time horizons and more frequent compounding periods. 🚀
""", unsafe_allow_html=True)