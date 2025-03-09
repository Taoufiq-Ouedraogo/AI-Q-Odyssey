import os
import streamlit as st
from pages.utils import utils_page


utils_page.set_st_page2("Option Pricing Tool")

st.title(f"Option Pricing Tool")


# BinomialTree = S0, K, T, r, sigma=None, u=None, d=None, N=1, opttype="C"
# TrinomialTree = S0, K, T, r, sigma=None, u=None, N=1, opttype="C")
# GBM = S0, K, T, r, sigma, N, M, opttype