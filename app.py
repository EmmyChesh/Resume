from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
project_images_dir = current_dir / "assets" / "project_images"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Cheshi Emmanuel"
PAGE_ICON = ":wave:"
NAME = "Cheshi Emmanuel"
DESCRIPTION = """
Data Analyst, Data Scientist, Digital Skills Trainer/Instructor, Machine Learning Engineer
"""
EMAIL = "emmychesh@yahoo.com"
SOCIAL_MEDIA = {
    "Facebook": "https://facebook.com/emmanuel.cheshi",
    "LinkedIn": "https://www.linkedin.com/in/emmanuel-cheshi-b50abb154/",
    "GitHub": "https://github.com/EmmyChesh",
    "Twitter": "https://twitter.com/emmychesh17",
}
PROJECTS = {
    "🏆 Analytical Dashboards - Various Analysis": "https://github.com/EmmyChesh/Analytical-Dashboards",
    "🏆 Text To Speech Web-App and Language Converter": "https://emmychesh-text-to-speech-trans.streamlit.app",
    "🏆 Car Price Predictor Web App": "https://emmycheshpredictorapp.streamlit.app",
    "🏆 Diamond Price Predictor Web App": "https://emmychesh-diamonds.streamlit.app",
    "🏆 Image Attendance and Security System Register": "https://github.com/EmmyChesh/Image-Attendance-and-Security-System",
    "🏆 Lip Reading Deep Learning App": "https://github.com/EmmyChesh/Lip-Reading-Deep-Learning-Model/tree/main/app"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- SIDEBAR NAVIGATION ---
st.sidebar.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        font-size: 20px;
        font-weight: bold;
    }
    .sidebar .sidebar-content .stRadio>div {
        margin-top: 10px;
    }
    .sidebar .sidebar-content .stRadio>div>label {
        display: block;
        padding: 10px;
        border-radius: 5px;
        border: 2px solid transparent;
        background-color: #f0f0f0;
        color: #333;
        cursor: pointer;
    }
    .sidebar .sidebar-content .stRadio>div>label:hover {
        background-color: #e0e0e0;
    }
    .sidebar .sidebar-content .stRadio>div>label.stRadioActive {
        background-color: #007bff;
        color: #fff;
        border-color: #007bff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("Resume Sections")
section = st.sidebar.radio(
    "Go to",
    ["Introduction", "Experience & Qualifications", "Skills", "Work History", "Projects & Accomplishments"]
)

# --- HERO SECTION ---
if section == "Introduction":
    st.image(profile_pic, width=150, use_column_width=True)
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write(f"📫 {EMAIL}")
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

    st.write('\n')
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; width: 300px;">
            <a href="https://facebook.com/emmanuel.cheshi" target="_blank" style="text-decoration: none; color: inherit;">
                <img src="https://img.icons8.com/color/50/000000/facebook.png" width="40"/>
            </a>
            <a href="https://www.linkedin.com/in/emmanuel-cheshi-b50abb154/" target="_blank" style="text-decoration: none; color: inherit;">
                <img src="https://img.icons8.com/color/50/000000/linkedin.png" width="40"/>
            </a>
            <a href="https://github.com/EmmyChesh" target="_blank" style="text-decoration: none; color: inherit;">
                <img src="https://img.icons8.com/color/50/000000/github.png" width="40"/>
            </a>
            <a href="https://twitter.com/emmychesh17" target="_blank" style="text-decoration: none; color: inherit;">
                <img src="https://img.icons8.com/color/50/000000/twitter.png" width="40"/>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# --- EXPERIENCE & QUALIFICATIONS ---
elif section == "Experience & Qualifications":
    st.subheader("Experience & Qualifications")
    st.write(
        """
    - ✔️ 5+ years of experience extracting actionable insights from data
    - ✔️ 3+ years of experience creating and deploying robust Machine Learning models
    - ✔️ 3+ years as a data science/analytics instructor, facilitating comprehensive learning experiences
    - ✔️ Hands-on experience with Python, Excel, Power BI, SQL
    - ✔️ Strong understanding of statistical principles and analysis
    - ✔️ Excellent team player with a strong sense of initiative
    """
    )

# --- SKILLS ---
elif section == "Skills":
    st.subheader("Skills")
    skills = [
        ("👨‍💻 Programming", "Python"),
        ("🔄 Data Processing/Wrangling", "Pandas, Numpy"),
        ("📊 Data Visualization", "Power BI, MS Excel, Matplotlib, Seaborn"),
        ("📚 Modeling", "Logistic Regression, Linear Regression, Decision Trees, Random Forest"),
        ("🤖 Machine Learning", "Scikit-Learn"),
        ("🚀 Model Deployment", "Streamlit, Heroku, Docker"),
        ("📈 Data Analysis", "Excel, SQL, Power BI, SPSS, Python, Jupyter"),
        ("🗄️ Databases", "MySQL"),
    ]

    st.markdown("<div style='line-height: 1.2;'>", unsafe_allow_html=True)
    for skill, details in skills:
        st.write(f"<p>- {skill}: {details}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- WORK HISTORY ---
elif section == "Work History":
    st.subheader("Work History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**Lead Data Scientist | BlueHouse Technologies**")
    st.write("Sept. 2023 - Present")
    st.write(
        """
   - ► Drive data-driven initiatives and lead projects to achieve business goals at Bluehouse Technologies.
- ► Optimize machine learning models and ensure data quality for maximum effectiveness.
- ► Communicate insights to stakeholders and collaborate across teams while staying updated with industry trends.
- ► Promote and ensure ethical standards in data usage and mentor junior data scientists.
- ► Leverage data as a strategic asset to guide the company towards sustainable growth and innovation.
    """
    )

     # --- JOB 1
    st.write("🚧", "**Data Analytics Instructor | The CoreStream Nigeria**")
    st.write("Jun. 2024 - Present")
    st.write(
        """
   - ► Design and deliver comprehensive courses in Excel, Power BI, SQL, and Python to equip students with essential data analytics skills.
- ► Develop and optimize training materials, ensuring data accuracy and clarity in instructional content.
- ► Stay updated with industry trends, integrating relevant advancements into the curriculum to keep courses current.
- ► Promote ethical data usage and best practices, fostering a strong foundation for responsible analytics.
- ► Mentor students, helping them develop analytical thinking and technical skills to achieve their career goals in data analytics.
    """
    )

    # --- JOB 2
    st.write('\n')
    st.write("🚧", "**Full Stack Data Science Facilitator | 10alytics Edtech Hub**")
    st.write("Jul. 2023 - Nov. 2023")
    st.write(
        """
    - ► Instructed and guided fellows through the end-to-end data science process.
    - ► Emphasized meticulous data collection and preprocessing using Python.
    - ► Provided comprehensive training on exploratory data analysis and predictive model development.
    - ► Facilitated seamless model deployment, integration, and performance monitoring while fostering a data-driven culture and communicating technical concepts to non-technical stakeholders.
    """
    )

    # --- JOB 3
    st.write('\n')
    st.write("🚧", "**Data Science Instructor | PICTDA (Plateau State Information and Communication Technology Development Agency)**")
    st.write("Sept. 2022 - Sept. 2023")
    st.write(
        """
    - ► Designing and updating data science courses to ensure relevance and effectiveness in line with industry trends and standards.
    - ► Teaching data science concepts, methodologies, and tools to learners, providing guidance throughout their learning journey.
    - ► Offering personalized guidance and support to individuals, including assistance with projects, career advice, and professional development.
    - ► Facilitating practical exercises, workshops, and projects to reinforce theoretical concepts and develop practical skills in data analysis, machine learning, and other relevant areas.
    - ► Fostering a supportive learning environment by organizing meetups, networking events, and collaborations within the data science community, both locally and globally.
    """
    )

    # --- JOB 4
    st.write('\n')
    st.write("🚧", "**Data Analyst | CYPA Africa And Equity International Initiative**")
    st.write("Feb. 2023 - Feb. 2023")
    st.write(
        """
    - ► Gathered data from various sources related to the 2023 General Elections.
    - ► Analysed the collected data to derive meaningful insights and identify trends.
    - ► Created visual representations of the analysed data to make it more accessible and understandable.
    - ► Provided real-time updates and results of the election process.
    - ► Prepared and presented a comprehensive report detailing the findings and insights derived from the data analysis process.
    """
    )

    # --- JOB 5
    st.write('\n')
    st.write("🚧", "**Researcher | CAFOD UK | Jos Plateau State Nigeria**")
    st.write("Mar. 2020 - May. 2022")
    st.write(
        """
    - ► Conducted qualitative research focusing on peace-building efforts among the two major religious faiths in Jos-North Local Government, Plateau State, Nigeria.
    - ► Investigated the underlying causes and dynamics of religious conflicts between the dominant religions in the area.
    - ► Gathered primary data through interviews, focus group discussions, and field observations to understand the perspectives of local communities.
    - ► Analyzed qualitative data using thematic analysis to identify key themes and patterns related to the causes and impacts of the conflicts.
    - ► Developed actionable recommendations for implementing peace-building interventions to promote interfaith harmony and reconciliation.
    """
    )

    # --- JOB 6
    st.write('\n')
    st.write("🚧", "**Data Analyst | CAFOD UK | Jos Plateau State Nigeria**")
    st.write("Mar. 2020 - May. 2022")
    st.write(
        """
    - ► Analyzed qualitative research findings using Transcriptor and Atlas.ti software.
    - ► Conducted thematic analysis to identify patterns and insights in the data related to peace-building efforts.
    - ► Developed comprehensive reports summarizing research findings and providing recommendations for peace-building strategies.
    """
    )

# --- PROJECTS & ACCOMPLISHMENTS ---
elif section == "Projects & Accomplishments":
    st.subheader("Projects & Accomplishments")
    st.write("---")
    project_images = {
        "🏆 Analytical Dashboards - Various Analysis": "power_bi_dashboards.png",
        "🏆 Text To Speech Web-App and Language Converter": "text_to_speech.png",
        "🏆 Car Price Predictor Web App": "car_price_predictor.jpg",
        "🏆 Diamond Price Predictor Web App": "diamond_price_predictor.jpg",
        "🏆 Image Attendance and Security System Register": "image_attendance_register.jpeg",
        "🏆 Lip Reading Deep Learning App": "lip_reading.jpg",
    }

    for project, details in PROJECTS.items():
        project_image = project_images_dir / project_images[project]
        st.write(f"### {project}")
        st.image(Image.open(project_image), width=300)
        st.write(f"[Link to project]({details})")

# --- PERSONALIZED MESSAGE ---
st.write('\n')
st.write("---")
st.write("Thank you for visiting my digital resume. Feel free to explore my projects and reach out to me through my social media channels!")
