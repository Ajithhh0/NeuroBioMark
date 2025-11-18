import streamlit as st

def render(encoded):

    # Spacer under navbar
    st.markdown("<div style='height:70px'></div>", unsafe_allow_html=True)

    # ---- BACKGROUND + STYLES ----
    st.markdown(
        f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{encoded}");
    background-size: 70% auto;
    background-position: center;
    background-repeat: no-repeat;
}}

.bg-box {{
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    padding: 40px 50px;
    border-radius: 16px;
    width: 90%;
    margin: 40px auto;
    color: white;
    box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.35);
    font-size: 16px;
    line-height: 1.6;
}}

.section-title {{
    font-size: 22px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 10px;
    color: #00eaff;
}}
</style>
""",
        unsafe_allow_html=True,
    )

    # ---- ALL CONTENT IN ONE DEDENTED HTML BLOCK (NO LEADING SPACES) ----
    html = """
<h2 style='color:white; font-weight:700; text-align:center;'>Background</h2>

<div class="bg-box">

<div class="section-title">What Are Neurological Biomarkers?</div>
Neurological biomarkers are measurable indicators that reflect changes 
in brain structure, function, or physiology. They can be derived from:
<ul>
    <li>Brain imaging (MRI, CT, PET)</li>
    <li>Signals (EEG, EMG)</li>
    <li>Biological samples (blood, CSF)</li>
    <li>Digital features (speech, gait, facial analysis)</li>
    <li>Tongue images and other emerging modalities</li>
</ul>
These biomarkers enable earlier and more objective detection of 
neurological conditions.

<div class="section-title">Why Biomarkers Matter</div>
Neurodegenerative diseases such as ALS, Alzheimer’s, Parkinson’s, 
and FTD present major diagnostic challenges:
<ul>
    <li><b>Late Diagnosis</b> — Symptoms appear only after major neuron loss.</li>
    <li><b>No Definitive Tests</b> — Diagnosis often relies on clinical judgement.</li>
    <li><b>Hidden Symptoms</b> — Cognitive or behavioural changes may go unnoticed.</li>
</ul>
Biomarkers help detect these changes earlier and with better accuracy.

<div class="section-title">Challenges & Opportunity</div>
AI enables extraction of subtle, clinically relevant patterns from:
<ul>
    <li>Voice</li>
    <li>Movement</li>
    <li>Physiological signals</li>
    <li>Tongue images</li>
</ul>

Despite this potential, challenges include:
<ul>
    <li>Limited interpretability</li>
    <li>Small or inconsistent datasets</li>
    <li>Need for clinical validation</li>
    <li>Ethical and privacy concerns</li>
</ul>

NeuroBioMark aims to advance digital biomarker research and support 
earlier, more reliable diagnostic tools.

</div>
"""

    st.markdown(html, unsafe_allow_html=True)
