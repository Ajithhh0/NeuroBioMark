# NeuroBioMark

NeuroBioMark is a research project aimed at developing an explainable AI web application for ALS (Amyotrophic Lateral Sclerosis) diagnosis and biomarker visualization.  
The project combines machine learning, pathology image analysis, and transparent AI explainability methods.

## Features
- AI-assisted analysis for ALS detection and cognitive stratification  
- Visual explanations (Grad-CAM / Layer-CAM) to enhance clinical interpretability  
- Simple, multipage web interface for research and demonstration  
- Fully containerized for reproducible deployment with Docker  

## Folder Structure
```
neurobiomark_web/
│
├── home.py              # Main Streamlit app
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker setup
└── pages/               # (Optional) extra pages like About, Model, etc.
```

## Setup Instructions

### Run Locally (without Docker)
1. Clone the repository:
   ```bash
   git clone https://github.com/Ajithhh0/NeuroBioMark.git
   cd NeuroBioMark
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   streamlit run home.py
   ```
5. Open your browser at http://localhost:8501

### Run with Docker
1. Build the Docker image:
   ```bash
   docker build -t neurobiomark .
   ```
2. Run the container:
   ```bash
   docker run -p 8501:8501 neurobiomark
   ```
3. Visit the app at http://localhost:8501

## Updating the Repository
When making changes:
```bash
git add .
git commit -m "Updated web app"
git push
```

To pull updates on another machine:
```bash
git pull
```

## Research Context
This project contributes to the NeuroBioMark initiative led by  
Heriot-Watt University and collaborators, exploring explainable deep learning approaches for medical diagnosis.

## Author
Ajith Nair  

