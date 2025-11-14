import streamlit as st

st.set_page_config(page_title="NeuroBioMark", layout="wide")

# GLOBAL CSS MUST COME FIRST — fixes navbar code block & removes deploy
st.markdown("""
<style>
header {visibility: hidden !important;}
footer {visibility: hidden !important;}
#MainMenu {visibility: hidden !important;}
.block-container {padding-top: 0 !important;}
</style>
""", unsafe_allow_html=True)

# --- IMPORT AFTER CSS ---
from nbm_pages.home import render as home_render
from nbm_pages.page2 import render as page2_render
from nbm_pages.page3 import render as page3_render
from nbm_pages.page4 import render as page4_render
from nbm_pages.components.nav_buttons import nav_buttons

# Hide Streamlit sidebar
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
</style>
""", unsafe_allow_html=True)

# --- READ QUERY PARAMS PROPERLY ---
params = st.query_params
page = params.get("page", "Home")

# Store active page in session
st.session_state.active_page = page

# Navbar — now safe to render
nav_buttons()

# --- PAGE ROUTING ---
if page == "Home":
    home_render()
elif page == "Page2":
    page2_render()
elif page == "Page3":
    page3_render()
elif page == "Page4":
    page4_render()
else:
    home_render()
