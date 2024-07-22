from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Cheshi Emmanuel"
PAGE_ICON = ":wave:"
NAME = "Cheshi Emmanuel"
DESCRIPTION = """
Data Analyst, Data Scientist, Digital Skills Trainer/Instructor, Machine Learning Engineer.
"""
EMAIL = "emmychesh@yahoo.com"
SOCIAL_MEDIA = {
    "Facebook": "https://facebook.com/emmanuel.cheshi",
    "LinkedIn": "https://www.linkedin.com/in/emmanuel-cheshi-b50abb154/",
    "GitHub": "https://github.com/EmmyChesh",
    "Twitter": "https://twitter.com/emmychesh17",
}
PROJECTS = {
    "🏆 Power BI Dashboards - Various Analysis": "https://youtu.be/Sb0A9i6d320",
    "🏆 Text To Speech Web-App and Language Converter": "https://emmychesh-text-to-speech-trans.streamlit.app",
    "🏆 Car Price Predictor Web App": "https://emmycheshpredictorapp.streamlit.app",
    "🏆 Diamond Price Predictor Web App": "https://emmychesh-diamonds.streamlit.app",
    "🏆 Image Attendance Register": "https://pythonandvba.com/mytoolbelt/",
    "🏆 Lip Reading Deep Learning App": "https://emmychesh-diamonds.streamlit.app"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=250)
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
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Five years' experience extracting actionable insights from data
- ✔️ Three years' experience creating and deploying robust Machine Learning Models
- ✔️ Three years as a data science instructor facilitating comprehensive learning experiences
- ✔️ Hands-on experience and knowledge in Python, Excel, Power BI
- ✔️ Good understanding of statistical principles and analysis
- ✔️ Excellent team player and strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")

skills = {
    "Python Programming Language": 90,
    "Data Processing/Wrangling (Pandas, Numpy)": 85,
    "Data Visualization (PowerBI, MS Excel, Matplotlib, Seaborn)": 80,
    "Modeling (Logistic Regression, Linear Regression, Decision Trees, Random Forest)": 75,
    "Machine Learning (Scikit-Learn)": 80,
    "Model Deployment (Streamlit, Heroku, Docker)": 70,
    "Data Analysis (Excel, Power BI, SPSS, Python, Jupyter)": 85,
    "Databases (MySQL)": 70,
}

for skill, proficiency in skills.items():
    st.write(skill)
    st.progress(proficiency)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1 ---
with st.expander("🚧 **Lead Data Scientist | BlueHouse Technologies** (Sept. 2023 - Present)"):
    st.write(
        """
        - ► Lead Data Scientist at Bluehouse Technologies, driving data-driven initiatives.
        - ► Lead projects and develop strategies to achieve business goals.
        - ► Optimize machine learning models for maximum effectiveness.
        - ► Manage data quality and communicate insights to stakeholders.
        - ► Stay abreast of industry trends and collaborate across teams.
        - ► Ensure ethical standards in data usage.
        - ► Mentor junior data scientists to foster growth and excellence.
        - ► Leverage data as a strategic asset for innovation and efficiency.
        - ► Guide the company towards sustainable growth.
        """
    )

# --- JOB 2 ---
with st.expander("🚧 **Full Stack Data Science Facilitator | 10alytics Edtech Hub** (Jul. 2023 - Nov. 2023)"):
    st.write(
        """
        - ► Instructed and guided fellows through the end-to-end data science process.
        - ► Emphasized meticulous data collection and preprocessing using Python.
        - ► Provided comprehensive training on exploratory data analysis and predictive model development.
        - ► Facilitated seamless model deployment, integration, and performance monitoring while fostering a data-driven culture and communicating technical concepts to non-technical stakeholders.
        """
    )

# --- JOB 3 ---
with st.expander("🚧 **Data Science Instructor | PICTDA (Plateau State Information and Communication Technology Development Agency)** (Sept. 2022 - Sept. 2023)"):
    st.write(
        """
        - ► Designing and updating data science courses to ensure relevance and effectiveness in line with industry trends and standards.
        - ► Teaching data science concepts, methodologies, and tools to learners, providing guidance throughout their learning journey.
        - ► Offering personalized guidance and support to individuals, including assistance with projects, career advice, and professional development.
        - ► Facilitating practical exercises, workshops, and projects to reinforce theoretical concepts and develop practical skills in data analysis, machine learning, and other relevant areas.
        - ► Fostering a supportive learning environment by organizing meetups, networking events, and collaborations within the data science community, both locally and globally.
        """
    )

# --- JOB 4 ---
with st.expander("🚧 **Data Analyst | CYPA Africa And Equity International Initiative** (Feb. 2023 - Feb. 2023)"):
    st.write(
        """
        - ► Gathered data from various sources related to the 2023 General Elections.
        - ► Analysed the collected data to derive meaningful insights and identify trends.
        - ► Created visual representations of the analysed data to make it more accessible and understandable.
        - ► Provided real-time updates and results of the election process.
        - ► Prepared and presented a comprehensive report detailing the findings and insights derived from the data analysis process.
        """
    )

# --- JOB 5 ---
with st.expander("🚧 **Researcher | CAFOD UK | Jos Plateau State Nigeria** (Mar. 2020 - May. 2022)"):
    st.write(
        """
        - ► Conducted qualitative research focusing on peace-building efforts among the two major religious faiths in Jos-North Local Government, Plateau State, Nigeria.
        - ► Investigated the underlying causes and dynamics of religious conflicts between the dominant religions in the area.
        - ► Gathered primary data through interviews, focus group discussions, and observations within the community.
        - ► Analysed qualitative data to identify common themes, perceptions, and attitudes related to peace-building initiatives.
        - ► Generated recommendations based on research findings to support peace-building interventions and foster interfaith harmony in the region.
        """
    )

# --- JOB 6 ---
with st.expander("🚧 **Data Analyst | CAFOD UK | Jos Plateau State Nigeria** (Mar. 2020 - May. 2022)"):
    st.write(
        """
        - ► Analysed qualitative research findings obtained from field data collected during case studies.
        - ► Ensured alignment of the analysis with specific research questions and objectives.
        - ► Employed qualitative analytical tools such as Transcriptor and Atlas.ti to organize, code, and interpret data.
        - ► Conducted thematic analysis to identify patterns, themes, and insights within the qualitative data.
        - ► Prepared reports summarizing the analysis findings and provided interpretations relevant to the research objectives.
        """
    )

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
