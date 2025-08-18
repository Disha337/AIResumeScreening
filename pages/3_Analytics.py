import streamlit as st
import matplotlib.pyplot as plt



st.markdown(
    """
    <style>
    .stApp {
        background-image: url("ui/background.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .header {
        color: #00ffe0;
        font-size: 48px;
        font-weight: bold;
        text-shadow: 2px 2px 5px #000000;
    }
    .subheader {
        color: #ff00ff;
        font-size: 28px;
        font-weight: bold;
        text-shadow: 1px 1px 3px #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.set_page_config(page_title="Analytics", layout="wide")

st.markdown("<h2>📈 Resume Screening Analytics</h2>", unsafe_allow_html=True)

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("⚠️ Please login first.")
else:
    if "resume_names" in st.session_state and "scores" in st.session_state:
        fig, ax = plt.subplots()
        ax.bar(st.session_state["resume_names"], st.session_state["scores"])
        ax.set_title("Resume Matching Scores (AI)")
        ax.set_ylabel("Similarity Score")
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.info("ℹ️ Run ranking first to see analytics.")
