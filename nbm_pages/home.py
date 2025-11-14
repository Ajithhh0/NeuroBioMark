import streamlit as st
from PIL import Image

def render():

    # Only page-specific CSS (gradient)
    st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #0CCDD6, #0E1B3A);
}
</style>
""", unsafe_allow_html=True)

    # Layout: logo + title
    col_logo, _ = st.columns([1, 3])
    with col_logo:
        logo = Image.open("Resources/NBMLogoNobg_cropped.png")
        st.image(logo, width=150)

    # Title + Content
    st.markdown("## **NeuroBioMark**")

    st.write("""
Welcome to NeuroBioMark, your comprehensive platform for exploring 
the intersection of neuroscience and biometrics.

Our mission is to provide researchers, clinicians, and enthusiasts 
with insights, tools, and resources to advance the understanding of 
neurological biomarkers and their applications in diagnosis, 
treatment, and research.
""")
