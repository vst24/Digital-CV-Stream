from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV |  Vishal Singh Thakur"
PAGE_ICON = ":wave:"
NAME = "Vishal Singh Thakur"
DESCRIPTION = """
Data Scientist | Data Analyst | Civil Engineer | KPMG Virtual Intern |Mastering Data for Insights | Project Management Specialist|
"""
EMAIL = "vishalth3558@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/vishal-singh-thakur-5781b1224",
    "GitHub": "https://github.com/vst24",
    "Portfolio Link": "https://mavenanalytics.io/profile/Vishal-Singh-Thakur/172559753"
    
}
PROJECTS = {
    "🏆 Sales Dashboard -Enhancing Sales Transparency and Efficiency through Data-Driven Insights ": "https://mavenanalytics.io/project/8774", 

}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Education")
st.write(
    """
- ✔️ Applied AI Solutions Development (Postgraduate, Diploma) - George Brown College (3.62/4.0)
- ✔️ Project Management (Postgraduate, Diploma)- Georgian College(4.0/4.0)
- ✔️ Civil Engineering (Bachelor of Technology)- Chitkara University(7.06/10)
- ✔️ Data Analytics (Bootcamp)- Masterschool
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL.
- 👩‍💻 Packages: Scikit-learn, Tensorflow, Keras, Pytorch, nltk, OpenCV, Pandas, Numpy, Seaborn, Plotly, Matplotlib,beautifulSoup, SciPy.
- 📊 Data Visulization: : Tableau,Tableau prep Builder, PowerBI, MS Excel,Seaborn,Matplotlib,Plotly
- 📚 Machine learning and statistical modeling: Neural Networks, Convolutional Neural Networks (CNN), Recurrent Neural Networks(RNN), XGBoost, Random Forest, Support Vector Machine (SVM), Principal Component Analysis (PCA), Clustering(K-Means), Gaussian Mixture Model (GMM), Decision Tree, Logistic Regression, Linear Regression, K-Nearest Neighbors(KNN), Naïve Bayes, Stochastic Gradient Descent (SGD), Markov Models, LightGBM.
- 🗄️ Databases: Postgres, MySQL.
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Analyst Intern (Remote) | KPMG Virtual Internship**")
st.write("2023/04 – 2023/05")
st.write(
    """
- ► Assessed data quality and completeness, ensuring accurate and reliable analysis for better
decision-making, such as identifying and rectifying an average of 15% data inconsistencies
in monthly reports.
- ► Utilized Excel and Tableau to build dynamic dashboards, effectively tracking metrics and
visualizing key insights for stakeholders, resulting in a 20% increase in data accessibility
for cross-functional teams.
- ► Developed skills in data manipulation, cleaning, and transformation techniques, enhancing
data integrity and analysis accuracy, which reduced data processing time by 30% and
improved data accuracy by reducing errors by 25%.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Consultant | Matri Shakti Stone Crusher**")
st.write("2019/06 – 2021/09")
st.write(
    """
- ► Created real-time data visualization dashboards using Power BI to enhance plant
operation transparency and responsiveness to critical issues.
- ► Leveraged data analysis techniques to optimize equipment performance and minimize
downtime, resulting in a 15% increase in overall plant efficiency during the project
duration.
- ► Conducted comprehensive feasibility studies and devised strategic project plans, resulting
in successful equipment installations.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Site Engineer | Jandu Construction Company**")
st.write("2017/06 – 2019/05")
st.write(
    """
- ► Conducted monthly inspections for 6 construction projects, ensuring safety compliance.
- ► Coordinated 6 contractors and 4 subcontractors concurrently.
- ► Managed budgets, achieving 10% cost savings on average.
- ► Maintained on-time project completion, often finishing 2 weeks ahead.
- ► Reduced material waste by 15% through expertise in construction methods.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")