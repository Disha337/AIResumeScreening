import streamlit as st
from auth.authentication import login_user, register_user

st.set_page_config(page_title="AI Resume Screening", layout="wide")

# Load CSS
with open("ui/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 AI Resume Screening - Login/Register")

    tab1, tab2 = st.tabs(["🔑 Login", "🆕 Register"])

    with tab1:
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            if login_user(username, password):
                st.session_state.logged_in = True
                st.session_state.user = username
                st.success("✅ Login successful!")
                st.rerun()
            else:
                st.error("❌ Invalid username or password")

    with tab2:
        new_username = st.text_input("New Username", key="reg_user")
        new_password = st.text_input("New Password", type="password", key="reg_pass")
        if st.button("Register"):
            success, msg = register_user(new_username, new_password)
            if success:
                st.success(msg)
            else:
                st.error(msg)

else:
    st.sidebar.success(f"Welcome {st.session_state.user} 👋")
    st.sidebar.page_link("pages/1_Upload_and_Description.py", label="📂 Upload & JD")
    st.sidebar.page_link("pages/2_Ranking_Results.py", label="📊 Ranking")
    st.sidebar.page_link("pages/3_Analytics.py", label="📈 Analytics")

    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()

    st.markdown("<h1>🚀 AI Resume Screening Dashboard</h1>", unsafe_allow_html=True)
    st.write("Select a page from the sidebar to continue.")
