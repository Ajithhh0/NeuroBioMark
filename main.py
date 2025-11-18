import streamlit as st
import base64

st.set_page_config(page_title="NeuroBioMark", layout="wide")

# ---- GLOBAL CSS (MUST BE FIRST) ----
st.markdown("""
<style>
/* Hide Streamlit UI */
header {visibility: hidden !important;}
footer {visibility: hidden !important;}
#MainMenu {visibility: hidden !important;}

.block-container {padding-top: 0 !important;}
[data-testid="stSidebar"] {display: none !important;}

/* STEP 1 — Prevent the blue flash */
html, body,
[data-testid="stAppViewContainer"] {
    background-color: #000000 !important;
}

/* STEP 2 — Allow page background images to show */
.stApp {
    background-color: transparent !important;
    background-image: none !important;
}

/* STEP 3 — STRONG OVERRIDE (wins after render) */
html body .stApp {
    background-color: transparent !important;
}
</style>

""", unsafe_allow_html=True)

# ---- Import pages AFTER CSS ----
from nbm_pages.home import render as home_render
from nbm_pages.background import render as background_render
from nbm_pages.research import render as research_render
from nbm_pages.team import render as team_render
from nbm_pages.components.nav_buttons import nav_buttons


def load_background():
    with open("Resources/brainbg.jpg", "rb") as f:
        return base64.b64encode(f.read()).decode()

encoded_bg = load_background()

# st.write("BG length:", len(encoded_bg))


# ---- Read the current page from URL ----
params = st.query_params
current_page = params.get("page", "Home")

st.session_state.active_page = current_page

# ---- Render NAVBAR ----
nav_buttons()

# ---- Load Selected Page (PASS encoded_bg) ----
if current_page == "Home":
    home_render(encoded_bg)
elif current_page == "Background":
    background_render(encoded_bg)
elif current_page == "Research":
    research_render(encoded_bg)
elif current_page == "Team":
    team_render(encoded_bg)
else:
    home_render(encoded_bg)   # default fallback
