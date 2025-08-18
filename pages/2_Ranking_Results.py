import streamlit as st
import pandas as pd
from modules.ranking import rank_resumes



st.set_page_config(page_title="Ranking", layout="wide")

st.markdown("<h2>📊 Resume Ranking (AI - SBERT)</h2>", unsafe_allow_html=True)

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("⚠️ Please login first.")
else:
    if "job_description" in st.session_state and "resumes" in st.session_state:
        scores = rank_resumes(st.session_state["job_description"], st.session_state["resumes"])
        st.session_state["scores"] = scores
        results = pd.DataFrame({"Resume": st.session_state["resume_names"], "Score": scores})
        results = results.sort_values(by="Score", ascending=False)
        st.dataframe(results, use_container_width=True)
    else:
        st.warning("⚠️ Please upload resumes & job description first on the Upload page.")
