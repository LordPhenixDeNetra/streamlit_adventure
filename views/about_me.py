import streamlit as st

from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    # st.text_input("First Name")
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile_image.png", width=230)
with col2:
    st.title("Moussa THIOR - LPDN", anchor=False)
    st.write("Senior Data Analyst, assisting by supporting data-driven decision-making")

    if st.button("📧 Contact Me"):
        show_contact_form()

# st.divider()
"---"

# --- EXPERIENCE AND QUALIFICATIONS ---

st.write("\n")
st.subheader("Experience and Qualifications", anchor=False)
st.write(
    """
    - 7 Years experience extracting actionable insights from data
    - Strong hands-on experience and knowledge in Python and Excel
    - Good understanding of statistical principles and their respective applications
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# --- SKILLS ---

st.write("\n")
st.subheader("Skills")
st.write(
    """
    - Programming: Python (Scikit-learn, Pandas), SQL, VBA
    - Data Visualization: PowerBi, MS Excel, Plotly
    - Modeling: Logistic regression, linear regression, decision trees
    - Databases: Postgres, MongoDB, MySQL
    """
)



