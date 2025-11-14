import streamlit as st

def nav_buttons():
    current = st.session_state.get("active_page", "Home")

    st.markdown(
        f"""
<style>
.nav-wrapper {{
    position: sticky;
    top: 0;
    z-index: 9999;
    padding: 12px 0;
}}

.nav-container {{
    display: flex;
    gap: 35px;
    align-items: center;
}}

.nav-btn {{
    background: transparent;
    color: white;
    font-size: 18px;
    padding: 6px 6px;
    cursor: pointer;
    text-decoration: none;
    position: relative;
}}

/* Hover underline animation */
.nav-btn::after {{
    content: "";
    position: absolute;
    bottom: -3px;
    left: 0;
    width: 0%;
    height: 2px;
    background: white;
    transition: width 0.25s ease-out;
}}

.nav-btn:hover::after {{
    width: 100%;
}}

/* Active button: cyan text, NO underline */
.active {{
    color: #00f3ff !important;
    font-weight: 700;
}}

.active::after {{
    width: 0 !important;
    height: 0 !important;
}}
</style>

<div class="nav-wrapper">
    <div class="nav-container">
        <a class="nav-btn {'active' if current=='Home' else ''}" href="/?page=Home" target="_self">Home</a>
        <a class="nav-btn {'active' if current=='Page2' else ''}" href="/?page=Page2" target="_self">Button 2</a>
        <a class="nav-btn {'active' if current=='Page3' else ''}" href="/?page=Page3" target="_self">Button 3</a>
        <a class="nav-btn {'active' if current=='Page4' else ''}" href="/?page=Page4" target="_self">Button 4</a>
    </div>
</div>
""",
        unsafe_allow_html=True,
    )
