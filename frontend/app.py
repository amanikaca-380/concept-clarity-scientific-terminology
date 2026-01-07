import streamlit as st
import streamlit as st

st.set_page_config(
    page_title="Concept Clarity",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
/* Hide sidebar */
[data-testid="stSidebar"] {
    display: none;
}

/* App background */
.stApp {
    background: linear-gradient(135deg, #eef2ff, #f8fafc);
}

/* Main container spacing */
.block-container {
    padding-top: 3rem;
}

/* Hero card */
.hero-card {
    background-color: #ffffff;
    padding: 2rem;
    border-radius: 16px;
    box-shadow: 0px 12px 30px rgba(99,102,241,0.15);
    text-align: center;
}

/* Title */
.hero-title {
    font-size: 2.5rem;
    font-weight: 700;
    color: #3730a3;
    margin-bottom: 0.5rem;
}

/* Subtitle */
.hero-subtitle {
    font-size: 1.05rem;
    color: #475569;
    margin-bottom: 2rem;
}

/* Text-style navbar buttons */
.nav-button button {
    background: none !important;
    color: #3730a3 !important;
    border: none !important;
    box-shadow: none !important;
    font-size: 1rem !important;
    font-weight: 500 !important;
    padding: 0 !important;
    margin: 0 !important;
    cursor: pointer;
}

/* Hover effect */
.nav-button button:hover {
    text-decoration: underline;
    color: #4f46e5 !important;
}

</style>
""", unsafe_allow_html=True)

# ---------- TOP NAV BAR ----------

nav_left, nav_spacer, nav_login, nav_signup ,nav_guest= st.columns([4, 3, 1, 1,1])

with nav_left:
    st.markdown(
        "<h3 style='margin:0; color:#3730a3;'>SciClarify</h3>",
        unsafe_allow_html=True
    )

with nav_login:
    st.markdown('<div class="nav-button">', unsafe_allow_html=True)
    if st.button("Login"):
        st.switch_page("pages/login.py")
    
with nav_signup:
    st.markdown('<div class="nav-button">', unsafe_allow_html=True)
    if st.button("Sign Up"):
        st.switch_page("pages/signup.py")

with nav_guest:   
    st.markdown('<div class="nav-button">', unsafe_allow_html=True)
    if st.button("Continue as Guest"):
        st.session_state.clear()
        st.switch_page("pages/home.py")


# Small trust line
st.markdown(
    "<h4 style='color:#64748b; font-size:0.9rem; align: center;'>Built to simplify learning • Powered by AI</p>",
    unsafe_allow_html=True
)

# Main headline
st.markdown(
    "<h1 style='font-size:3rem; font-weight:800; align: center;'>Understand Scientific Terms, Instantly</h1>",
    unsafe_allow_html=True
)

# Supporting text
st.markdown(
    "<p style='font-size:1.15rem; color:#475569;'>"
    "Enter any scientific term and get a clear, simple explanation "
    "designed for students, educators, and curious learners."
    "</p>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("###  Simple explanations")
    st.write("Beginner-friendly explanations without heavy jargon.")

with f2:
    st.markdown("### AI-powered")
    st.write("Powered by pretrained AI models for better understanding.")

with f3:
    st.markdown("### Learning-focused")
    st.write("Built for students, educators, and lifelong learners.")


# Initialize session states
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "landing"

st.markdown("<br>", unsafe_allow_html=True)

