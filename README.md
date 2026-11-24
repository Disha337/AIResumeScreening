# AI Resume Screening & Candidate Ranking System

## Overview
This project is an offline resume screening and candidate ranking system designed to assist recruiters in comparing multiple resumes against a given job description. The system is implemented as a **Streamlit** web application and focuses on practical, interpretable NLP techniques rather than heavy deep-learning models.

The application allows users to upload PDF resumes, input a job description, and automatically rank candidates based on textual similarity. The goal is to demonstrate end-to-end system design, including document parsing, feature extraction, similarity computation, result visualization, and basic user authentication.

The entire system runs offline, making it lightweight and easy to deploy without external APIs or large model downloads.

---

## Problem Statement
Manual resume screening is time-consuming and often inconsistent when dealing with a large number of candidates. Recruiters must repeatedly compare resumes against job requirements, which can lead to subjective decisions and inefficiency.

This project addresses the problem by:
- Automatically extracting textual information from resumes
- Quantifying relevance between resumes and a job description
- Producing a ranked list of candidates with clear similarity scores

---

## System Architecture
The application follows a modular structure to separate concerns and improve maintainability:

- **Authentication Module (`auth/`)**  
  Handles user login and registration using a lightweight, file-based approach.

- **Core Processing Modules (`modules/`)**  
  Responsible for:
  - PDF text extraction  
  - Text preprocessing  
  - TF-IDF vectorization  
  - Cosine similarity computation  

- **Application Pages (`pages/`)**  
  Streamlit pages for:
  - Resume upload and job description input  
  - Ranking result display  
  - Analytical visualizations  

- **User Interface (`ui/`)**  
  Custom CSS styling to enhance usability and readability.

- **Main Application (`app.py`)**  
  Controls session state, navigation, and page routing.

This structure reflects a system-oriented approach rather than a single-script implementation.

---

## Technical Approach

### Resume Processing
- Resumes are uploaded in PDF format  
- Text is extracted using PDF parsing utilities  
- Extracted text is cleaned and prepared for vectorization  

### Feature Extraction
- **TF-IDF (Term Frequency–Inverse Document Frequency)** is used to convert text into numerical feature vectors  
- Benefits:
  - Interpretability  
  - Low computational overhead  
  - Suitable for smaller datasets  

### Similarity & Ranking
- **Cosine similarity** is computed between:
  - Each resume vector  
  - The job description vector  
- Similarity scores are converted into percentage match values  
- Candidates are ranked in descending order of relevance  
- The top-ranked candidate is highlighted for clarity  

---

## Why TF-IDF?
TF-IDF was intentionally chosen instead of deep learning models because:
- It works reliably in offline environments  
- Avoids dependency on large pretrained models  
- Produces explainable results, important in screening systems  
- Sufficient for demonstrating core NLP and ranking concepts  

---

## Features
- User login and registration  
- Upload and process multiple PDF resumes  
- Input custom job descriptions  
- Rank candidates using TF-IDF + cosine similarity  
- Display results as percentage relevance scores  
- Highlight the top candidate  
- Visualize ranking results using basic charts  
- Fully offline execution  

---

## Technologies Used
- Python  
- Streamlit (UI and application flow)  
- Scikit-learn (TF-IDF vectorization, cosine similarity)  
- Pandas (data handling)  
- PDF parsing libraries  
- HTML/CSS (custom UI styling)  

---

## How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/Disha337/AIResumeScreening.git
2. **Navigate to the project directory**
   cd AIResumeScreening
3. **Install dependencies**
   pip install -r requirements.txt
4. **Run the application**
   streamlit run app.py

---
## Project Scope & Limitations
- Designed for small to medium-scale resume screening
- Uses textual similarity only (no semantic embeddings or learning-based ranking)
- Authentication is lightweight and intended for demonstration purposes
- Not intended as a production-ready hiring system

## Learning Outcomes
Through this project, you gain hands-on experience in:
- Building an end-to-end NLP-based application
- Designing modular Python code
- Applying interpretable text similarity techniques
- Developing interactive data applications with Streamlit
- Translating a real-world problem into a working software system
