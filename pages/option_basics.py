import os
import streamlit as st
from pages.utils import utils_page


utils_page.set_st_page2("Basics of Options")
st.title(f"Basics of Options")






st.markdown("## 📊 **Effect on Options Pricing**")



# Custom HTML and CSS for styling
st.markdown("""
    <style>
    .table-container {
        background-color: #f9f9fb;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
        border: 1px solid #ececec;
    }
    .table-container h3 {
        color: #000;
        font-size: 25px;
        font-weight: 600;
        text-align: center;
    }
    .table-container table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px;
        border-radius: 10px;
        overflow: hidden;
    }
    .table-container th, .table-container td {
        padding: 15px;
        text-align: center;
        border: 1px solid #ececec;
    }
    .table-container th {
        background-color: #2a7ae2;
        color: white;
        font-size: 16px;
    }
    .table-container td {
        background-color: #ffffff;
        font-size: 14px;
        color: #000;
    }
    .table-container tr:nth-child(odd) {
        background-color: #f7f7f7;
    }
    .table-container tr:hover {
        background-color: #e0e0e0;
    }
    .table-container .emoji {
        font-size: 18px;
    }
    .factor-desc {
        font-size: 16px;
        color: #333;
        line-height: 1.6;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)


# HTML table with stylized data
st.markdown("""
    <div class="table-container">
        <h3>📈 Impact of Various Factors on Call and Put Option Values</h3>
        <table>
            <tr>
                <th>⬆️ Increasing Factors</th>
                <th>Call Option Price</th>
                <th>Put Option Price</th>
            </tr>
            <tr>
                <td>Increase in underlying asset’s value</td>
                <td><span class="emoji">📈</span></td>
                <td><span class="emoji">📉</span></td>
            </tr>
            <tr>
                <td>Increase in underlying asset's volatility</td>
                <td><span class="emoji">📈</span></td>
                <td><span class="emoji">📈</span></td>
            </tr>
            <tr>
                <td>Increase in strike price</td>
                <td><span class="emoji">📉</span></td>
                <td><span class="emoji">📈</span></td>
            </tr>
            <tr>
                <td>Increase in time to expiration</td>
                <td><span class="emoji">📈</span></td>
                <td><span class="emoji">📈</span></td>
            </tr>
            <tr>
                <td>Increase in interest rates</td>
                <td><span class="emoji">📈</span></td>
                <td><span class="emoji">📉</span></td>
            </tr>
            <tr>
                <td>Increase in dividends paid</td>
                <td><span class="emoji">📉</span></td>
                <td><span class="emoji">📈</span></td>
            </tr>
        </table>
    </div>
""", unsafe_allow_html=True)