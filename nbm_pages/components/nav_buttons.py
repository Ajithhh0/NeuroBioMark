import streamlit as st
import base64


def nav_buttons():
    current = st.session_state.get("active_page", "Home")

    with open("Resources/NBMLogoNobg_cropped.png", "rb") as f:
        logo_data = base64.b64encode(f.read()).decode()

    def cls(page):
        return "nav-btn active" if current == page else "nav-btn"

    html = f"""
<style>
.nav-wrapper {{
    position: sticky;
    top: 0;
    z-index: 9999;
    height: 70px;
    width: 100%;
    background: rgba(0,0,0,0.2);
    backdrop-filter: blur(12px);
}}
.nav-container {{
    max-width: 1400px;
    margin: 0 auto;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 40px;
}}

.nav-logo {{
    height: 48px;
    margin-left: 10px;
}}
.nav-btn {{
    font-size: 17px;
    font-weight: 500;
    padding: 5px 22px;
    border-radius: 40px;
    text-decoration: none;
    color: white;
    border: 2px solid rgba(0,243,255,0.3);
    background: rgba(0,243,255,0.07);
    transition: all 0.25s ease;
}}

.nav-btn:hover: {{
    background: #00f3ff;
    color: black;
    box-shadow: 0 0 12px #00f3ff;
    border-color: #00f3ff;
}}
.active {{
    background: #00f3ff !important;
    color: black !important;
    border-color: #00f3ff !important;
    box-shadow: 0 0 14px #00f3ff !important;
    font-weight: 600;
}}

</style>

<div class="nav-wrapper">
  <div class="nav-container">

<img class="nav-logo" src="data:image/png;base64,{logo_data}">


<div class="nav-links">
<a class="{cls("Home")}" href="?page=Home" target="_self">Home</a>
<a class="{cls("Background")}" href="?page=Background" target="_self">Background</a>
<a class="{cls("Research")}" href="?page=Research" target="_self">Research</a>
<a class="{cls("Team")}" href="?page=Team" target="_self">Team</a>


</div>

</div>
</div>
"""

    st.markdown(html, unsafe_allow_html=True)