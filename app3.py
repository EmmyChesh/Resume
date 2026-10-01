
from pathlib import Path
import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Cheshi Emmanuel | Data • AI • Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# PATHS
# =========================================================
BASE_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = BASE_DIR / "assets"
RESUME_FILE = ASSETS_DIR / "CV.pdf"
PROFILE_PIC = ASSETS_DIR / "profile-pic.png"
PROJECT_IMAGES_DIR = ASSETS_DIR / "project_images"

# =========================================================
# PERSONAL / BRAND DATA
# =========================================================
NAME = "Cheshi Emmanuel"
ROLE = "Data Scientist • Machine Learning Engineer • Analytics Instructor"
TAGLINE = "Data → Intelligence → Impact"
INTRO = (
    "I turn complex data into useful decisions, intelligent products, and "
    "practical machine-learning solutions."
)
EMAIL = "emmychesh@yahoo.com"

SOCIALS = {
    "LinkedIn": "https://www.linkedin.com/in/emmanuel-cheshi-b50abb154/",
    "GitHub": "https://github.com/EmmyChesh",
    "X / Twitter": "https://twitter.com/emmychesh17",
    "Facebook": "https://facebook.com/emmanuel.cheshi",
}

HIGHLIGHTS = [
    ("5+", "Years in data & research"),
    ("3+", "Years building ML solutions"),
    ("3+", "Years teaching analytics"),
    ("6", "Featured portfolio projects"),
]

CAPABILITIES = {
    "Data Intelligence": [
        "Python", "SQL", "Power BI", "Excel", "SPSS",
        "Exploratory Data Analysis", "Statistical Analysis"
    ],
    "Machine Learning": [
        "Scikit-learn", "Classification", "Regression",
        "Decision Trees", "Random Forest", "Feature Engineering"
    ],
    "AI & Applied Computing": [
        "Computer Vision", "NLP", "Deep Learning",
        "Face Recognition", "Speech / Language Applications"
    ],
    "Deployment & Workflow": [
        "Streamlit", "Docker", "Heroku", "Jupyter",
        "Pandas", "NumPy", "MySQL"
    ],
}

PROJECTS = [
    {
        "title": "Analytical Dashboards",
        "category": "Data Intelligence",
        "description": (
            "A collection of interactive analytics dashboards designed to turn "
            "raw business data into clear, decision-ready insights."
        ),
        "image": "power_bi_dashboards.png",
        "link": "https://github.com/EmmyChesh/Analytical-Dashboards",
        "stack": ["Power BI", "Analytics", "Visualization"],
    },
    {
        "title": "Text-to-Speech & Language Converter",
        "category": "Applied AI",
        "description": (
            "A web application that converts text to speech and supports "
            "language transformation through an accessible Streamlit interface."
        ),
        "image": "text_to_speech.png",
        "link": "https://emmychesh-text-to-speech-trans.streamlit.app",
        "stack": ["NLP", "Speech", "Streamlit"],
    },
    {
        "title": "Car Price Predictor",
        "category": "Machine Learning",
        "description": (
            "An end-to-end predictive application that estimates vehicle prices "
            "from user-provided features through a deployed ML workflow."
        ),
        "image": "car_price_predictor.jpg",
        "link": "https://emmycheshpredictorapp.streamlit.app",
        "stack": ["Python", "ML", "Deployment"],
    },
    {
        "title": "Diamond Price Predictor",
        "category": "Machine Learning",
        "description": (
            "A regression-based application for estimating diamond prices from "
            "key characteristics, wrapped in a simple interactive interface."
        ),
        "image": "diamond_price_predictor.jpg",
        "link": "https://emmychesh-diamonds.streamlit.app",
        "stack": ["Regression", "Scikit-learn", "Streamlit"],
    },
    {
        "title": "Image Attendance & Security System",
        "category": "Computer Vision",
        "description": (
            "A face-recognition based attendance and security workflow designed "
            "to identify people and automate register creation."
        ),
        "image": "image_attendance_register.jpeg",
        "link": "https://github.com/EmmyChesh/Image-Attendance-and-Security-System",
        "stack": ["OpenCV", "Face Recognition", "Python"],
    },
    {
        "title": "Lip Reading Deep Learning App",
        "category": "Deep Learning",
        "description": (
            "A deep-learning project exploring visual speech recognition by "
            "interpreting lip movement from video."
        ),
        "image": "lip_reading.jpg",
        "link": "https://github.com/EmmyChesh/Lip-Reading-Deep-Learning-Model/tree/main/app",
        "stack": ["Deep Learning", "Computer Vision", "Video"],
    },
]

EXPERIENCE = [
    {
        "role": "Data Analyst",
        "company": "Elint Systems Limited",
        "period": "November 2024 – Present",
        "bullets": [
            "Analyze operational datasets across oil & gas, energy, and aviation to support strategic reporting and operational monitoring.",
            "Design and deploy interactive Power BI dashboards tracking 20+ KPIs for leadership decision-making.",
            "Develop predictive analytical models for forecasting and trend analysis.",
            "Automate recurring analytical reports with Python and Power BI, reducing manual reporting time by 40%.",
            "Implement structured data-validation processes to strengthen data accuracy and integrity.",
        ],
    },
    {
        "role": "Data Analysis Instructor",
        "company": "Corestream Nigeria",
        "period": "June 2024 – December 2025",
        "bullets": [
            "Delivered practical training in Excel, Power BI, SQL, and Python.",
            "Led hands-on analytics sessions using real datasets and end-to-end dashboard projects.",
            "Evaluated learner performance and provided targeted feedback for skill development.",
        ],
    },
    {
        "role": "Data Science / Analysis Instructor",
        "company": "Abuja Data School",
        "period": "September 2024 – August 2025",
        "bullets": [
            "Trained 100+ aspiring data professionals across Excel, Power BI, SQL, Python, and SPSS.",
            "Designed industry-focused curricula using real-world datasets and case studies.",
            "Supervised capstone projects across data cleaning, machine learning, and dashboard development.",
        ],
    },
    {
        "role": "Data Analytics Mentor",
        "company": "Tech Sisi",
        "period": "July 2024 – January 2025",
        "bullets": [
            "Mentored 50+ early-career data professionals in Python, SQL, Power BI, and machine learning.",
            "Guided mentees through portfolio projects from raw data to final analytical presentation.",
            "Developed structured learning frameworks to improve practical analytics capability.",
        ],
    },
    {
        "role": "Lead Data Scientist",
        "company": "BlueHouse Technologies",
        "period": "January 2024 – December 2024",
        "bullets": [
            "Led machine-learning initiatives across forecasting, customer behavior, and operational optimization.",
            "Built and improved data pipelines and preprocessing workflows.",
            "Mentored junior data scientists and analysts through code reviews and best practices.",
            "Translated analytical findings into product and business strategy.",
        ],
    },
    {
        "role": "Full Stack Data Science Facilitator",
        "company": "10Alytics Ed-Tech Hub",
        "period": "July 2023 – November 2023",
        "bullets": [
            "Taught the complete data-science lifecycle from acquisition and preprocessing to deployment.",
            "Delivered practical sessions using Pandas, NumPy, Scikit-learn, and Matplotlib.",
            "Supervised capstone projects involving predictive modeling and analytics dashboards.",
        ],
    },
    {
        "role": "Data Science Instructor",
        "company": "Code Plateau Hub",
        "period": "September 2022 – January 2024",
        "bullets": [
            "Delivered structured courses on Python, machine learning, and data-science fundamentals.",
            "Mentored learners through real-world capstone projects.",
            "Introduced deep-learning concepts and ML best practices.",
        ],
    },
    {
        "role": "Data Analyst",
        "company": "CYPA Africa & Equity International Initiative",
        "period": "February 2023 – March 2023",
        "bullets": [
            "Analyzed real-time electoral data during Nigeria's 2023 General Elections.",
            "Cleaned, validated, and managed datasets used for public reporting.",
            "Produced concise visual reports for electoral observers and stakeholders.",
        ],
    },
    {
        "role": "Researcher & Data Analyst",
        "company": "CAFOD UK",
        "period": "March 2020 – May 2022",
        "bullets": [
            "Conducted qualitative and quantitative research on conflict and peacebuilding in Plateau State.",
            "Used Atlas.ti to analyze interview transcripts and field data.",
            "Produced research reports and policy recommendations for community interventions.",
        ],
    },
]

# =========================================================
# STYLING
# =========================================================
st.markdown(
    """
    <style>
    /* ---------- Google font ---------- */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');

    :root {
        --bg: #060a12;
        --panel: rgba(13, 20, 33, 0.88);
        --panel-2: rgba(17, 27, 44, 0.72);
        --text: #f7f9fc;
        --muted: #a7b0c0;
        --cyan: #22d3ee;
        --cyan-2: #67e8f9;
        --gold: #f5c451;
        --border: rgba(255,255,255,0.10);
        --soft: rgba(34,211,238,0.08);
    }

    html { scroll-behavior: smooth; }

    .stApp {
        background:
            radial-gradient(circle at 12% 8%, rgba(34,211,238,0.11), transparent 28%),
            radial-gradient(circle at 88% 14%, rgba(245,196,81,0.08), transparent 22%),
            linear-gradient(180deg, #050810 0%, #08111f 55%, #060a12 100%);
        color: var(--text);
        font-family: 'Inter', sans-serif;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 1.1rem;
        padding-bottom: 4rem;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    #MainMenu, footer {
        visibility: hidden;
    }

    h1, h2, h3 {
        font-family: 'Space Grotesk', sans-serif !important;
        letter-spacing: -0.03em;
    }

    p, li, label, div {
        font-family: 'Inter', sans-serif;
    }

    a { text-decoration: none !important; }

    /* ---------- Top nav ---------- */
    .top-nav {
        position: sticky;
        top: 0.5rem;
        z-index: 999;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
        padding: 0.75rem 1rem;
        margin-bottom: 2.6rem;
        border: 1px solid var(--border);
        border-radius: 999px;
        background: rgba(6,10,18,0.80);
        backdrop-filter: blur(18px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.22);
    }

    .brand-mark {
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        color: white;
        white-space: nowrap;
    }

    .brand-mark span { color: var(--cyan); }

    .nav-links {
        display: flex;
        gap: 1.15rem;
        align-items: center;
        flex-wrap: wrap;
        justify-content: flex-end;
    }

    .nav-links a {
        color: #cbd5e1 !important;
        font-size: 0.90rem;
        font-weight: 600;
    }

    .nav-links a:hover {
        color: var(--cyan-2) !important;
    }

    /* ---------- Hero ---------- */
    .eyebrow {
        display: inline-flex;
        gap: 0.45rem;
        align-items: center;
        padding: 0.38rem 0.72rem;
        border: 1px solid rgba(34,211,238,0.28);
        border-radius: 999px;
        background: rgba(34,211,238,0.07);
        color: var(--cyan-2);
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }

    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(3.1rem, 7vw, 6.3rem);
        line-height: 0.95;
        font-weight: 700;
        letter-spacing: -0.065em;
        margin: 0;
        color: #fff;
    }

    .hero-title .accent {
        background: linear-gradient(90deg, var(--cyan), var(--cyan-2), var(--gold));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-role {
        margin-top: 1.3rem;
        color: #d8e0eb;
        font-weight: 600;
        font-size: 1.03rem;
    }

    .hero-copy {
        max-width: 710px;
        color: var(--muted);
        font-size: 1.08rem;
        line-height: 1.8;
        margin-top: 0.9rem;
    }

    .tagline {
        font-family: 'Space Grotesk', sans-serif;
        color: var(--gold);
        font-weight: 700;
        letter-spacing: 0.02em;
        margin-top: 1rem;
    }

    .hero-photo-wrap {
        position: relative;
        border-radius: 28px;
        padding: 8px;
        background: linear-gradient(145deg, rgba(34,211,238,.72), rgba(245,196,81,.42), rgba(255,255,255,.06));
        box-shadow: 0 30px 80px rgba(0,0,0,0.45);
    }

    /* Streamlit image inside right hero column */
    div[data-testid="stImage"] img {
        border-radius: 22px;
    }

    /* ---------- Buttons ---------- */
    .cta-row {
        display: flex;
        flex-wrap: wrap;
        gap: .75rem;
        margin: 1.6rem 0 .7rem;
    }

    .cta-primary, .cta-secondary {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: .78rem 1.05rem;
        border-radius: 12px;
        font-weight: 700;
        transition: transform .18s ease, border-color .18s ease, background .18s ease;
    }

    .cta-primary {
        color: #041017 !important;
        background: linear-gradient(90deg, var(--cyan), var(--cyan-2));
        border: 1px solid transparent;
    }

    .cta-secondary {
        color: white !important;
        border: 1px solid var(--border);
        background: rgba(255,255,255,.03);
    }

    .cta-primary:hover, .cta-secondary:hover {
        transform: translateY(-2px);
        border-color: rgba(34,211,238,.45);
    }

    /* Native buttons */
    div.stDownloadButton > button {
        border-radius: 12px;
        font-weight: 700;
        border: 1px solid rgba(34,211,238,.35);
        background: rgba(34,211,238,.08);
        color: #eafcff;
    }

    /* ---------- Section rhythm ---------- */
    .section-anchor {
        display: block;
        position: relative;
        top: -90px;
        visibility: hidden;
    }

    .section-kicker {
        color: var(--cyan);
        font-size: .78rem;
        font-weight: 800;
        letter-spacing: .13em;
        text-transform: uppercase;
        margin-bottom: .35rem;
    }

    .section-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(2rem, 4vw, 3.2rem);
        font-weight: 700;
        color: white;
        margin: 0 0 .65rem 0;
    }

    .section-copy {
        color: var(--muted);
        max-width: 760px;
        line-height: 1.75;
        margin-bottom: 1.4rem;
    }

    .section-gap {
        height: 4.5rem;
    }

    /* ---------- Metric cards ---------- */
    .metric-card {
        padding: 1.2rem 1rem;
        min-height: 132px;
        border: 1px solid var(--border);
        border-radius: 18px;
        background: linear-gradient(180deg, rgba(255,255,255,.045), rgba(255,255,255,.018));
    }

    .metric-number {
        font-family: 'Space Grotesk', sans-serif;
        color: white;
        font-size: 2.2rem;
        font-weight: 700;
    }

    .metric-label {
        color: var(--muted);
        font-size: .88rem;
        line-height: 1.45;
        margin-top: .25rem;
    }

    /* ---------- Capability cards ---------- */
    .capability-card {
        border: 1px solid var(--border);
        background: var(--panel-2);
        border-radius: 18px;
        padding: 1.15rem;
        min-height: 205px;
    }

    .capability-card h3 {
        font-size: 1.05rem;
        color: white;
        margin: 0 0 .7rem 0;
    }

    .chip {
        display: inline-block;
        margin: .22rem .18rem .22rem 0;
        padding: .35rem .55rem;
        border-radius: 999px;
        border: 1px solid rgba(255,255,255,.09);
        background: rgba(255,255,255,.035);
        color: #cbd5e1;
        font-size: .78rem;
    }

    /* ---------- Project cards ---------- */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-color: rgba(255,255,255,.10) !important;
        border-radius: 20px !important;
        background: rgba(12,19,31,.72);
        box-shadow: 0 18px 45px rgba(0,0,0,.16);
    }

    .project-category {
        color: var(--cyan);
        font-weight: 800;
        font-size: .74rem;
        letter-spacing: .10em;
        text-transform: uppercase;
        margin-bottom: .4rem;
    }

    .project-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.25rem;
        font-weight: 700;
        color: white;
        margin: .1rem 0 .55rem;
    }

    .project-copy {
        color: var(--muted);
        font-size: .90rem;
        line-height: 1.65;
        min-height: 88px;
    }

    .project-link {
        display: inline-block;
        margin-top: .8rem;
        color: var(--cyan-2) !important;
        font-size: .88rem;
        font-weight: 700;
    }

    /* ---------- Experience ---------- */
    .experience-card {
        position: relative;
        padding: 1.1rem 1.1rem 1.1rem 1.3rem;
        border-left: 2px solid rgba(34,211,238,.42);
        background: rgba(255,255,255,.02);
        border-radius: 0 16px 16px 0;
        margin-bottom: .9rem;
    }

    .experience-role {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.08rem;
        font-weight: 700;
        color: white;
    }

    .experience-company {
        color: var(--cyan-2);
        font-weight: 700;
        margin-top: .18rem;
    }

    .experience-period {
        color: var(--gold);
        font-size: .82rem;
        margin: .25rem 0 .65rem;
    }

    .experience-card li {
        color: var(--muted);
        line-height: 1.6;
        margin-bottom: .28rem;
    }

    /* ---------- Contact ---------- */
    .contact-panel {
        border: 1px solid rgba(34,211,238,.22);
        background:
            radial-gradient(circle at 90% 20%, rgba(34,211,238,.12), transparent 28%),
            rgba(10,17,28,.92);
        border-radius: 24px;
        padding: 2rem;
    }

    .contact-panel h2 {
        color: white;
        font-size: clamp(2rem, 4vw, 3rem);
        margin: 0 0 .7rem;
    }

    .social-row {
        display: flex;
        gap: .75rem;
        flex-wrap: wrap;
        margin-top: 1rem;
    }

    .social-pill {
        padding: .5rem .72rem;
        border-radius: 999px;
        background: rgba(255,255,255,.04);
        border: 1px solid var(--border);
        color: #dbe5f1 !important;
        font-size: .82rem;
        font-weight: 700;
    }

    .social-pill:hover {
        border-color: rgba(34,211,238,.42);
        color: var(--cyan-2) !important;
    }

    .footer-note {
        color: #718096;
        text-align: center;
        font-size: .80rem;
        margin-top: 2rem;
    }

    @media (max-width: 820px) {
        .top-nav {
            border-radius: 18px;
            align-items: flex-start;
            flex-direction: column;
        }

        .nav-links {
            justify-content: flex-start;
            gap: .75rem;
        }

        .hero-title {
            font-size: 3.25rem;
        }

        .project-copy {
            min-height: auto;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# HELPERS
# =========================================================
def anchor(name: str):
    st.markdown(f'<span id="{name}" class="section-anchor"></span>', unsafe_allow_html=True)


def section_heading(kicker: str, title: str, copy: str = ""):
    st.markdown(
        f"""
        <div class="section-kicker">{kicker}</div>
        <div class="section-title">{title}</div>
        <div class="section-copy">{copy}</div>
        """,
        unsafe_allow_html=True,
    )


def render_chips(items):
    chips = "".join(f'<span class="chip">{item}</span>' for item in items)
    st.markdown(chips, unsafe_allow_html=True)


def render_project(project):
    with st.container(border=True):
        image_path = PROJECT_IMAGES_DIR / project["image"]
        if image_path.exists():
            st.image(str(image_path), use_container_width=True)
        else:
            st.markdown(
                """
                <div style="
                    min-height:180px;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    border-radius:16px;
                    border:1px dashed rgba(255,255,255,.12);
                    background:rgba(255,255,255,.02);
                    color:#64748b;
                    margin-bottom:.8rem;">
                    Project image
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            f"""
            <div class="project-category">{project['category']}</div>
            <div class="project-title">{project['title']}</div>
            <div class="project-copy">{project['description']}</div>
            """,
            unsafe_allow_html=True,
        )
        render_chips(project["stack"])
        st.markdown(
            f'<a class="project-link" href="{project["link"]}" target="_blank">View project ↗</a>',
            unsafe_allow_html=True,
        )


# =========================================================
# NAVIGATION
# =========================================================
st.markdown(
    """
    <div class="top-nav">
        <div class="brand-mark">CE<span>.</span></div>
        <div class="nav-links">
            <a href="#about">About</a>
            <a href="#capabilities">Capabilities</a>
            <a href="#work">Selected Work</a>
            <a href="#journey">Journey</a>
            <a href="#lab">AI Lab</a>
            <a href="#contact">Contact</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# HERO
# =========================================================
hero_left, hero_right = st.columns([1.55, 0.75], gap="large")

with hero_left:
    st.markdown('<div class="eyebrow">● Data • AI • Machine Learning</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <h1 class="hero-title">
            Building <span class="accent">intelligent systems</span><br>
            from data.
        </h1>
        <div class="hero-role">{ROLE}</div>
        <div class="hero-copy">
            {INTRO}
        </div>
        <div class="tagline">{TAGLINE}</div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="cta-row">
            <a class="cta-primary" href="#work">Explore my work ↓</a>
            <a class="cta-secondary" href="mailto:{EMAIL}">Let's connect ↗</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if RESUME_FILE.exists():
        st.download_button(
            "Download résumé",
            data=RESUME_FILE.read_bytes(),
            file_name=RESUME_FILE.name,
            mime="application/pdf",
        )

with hero_right:
    if PROFILE_PIC.exists():
        st.markdown('<div class="hero-photo-wrap">', unsafe_allow_html=True)
        st.image(str(PROFILE_PIC), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown(
            """
            <div class="hero-photo-wrap">
                <div style="
                    min-height:420px;
                    border-radius:22px;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    font-family:'Space Grotesk',sans-serif;
                    font-size:5rem;
                    font-weight:700;
                    background:linear-gradient(145deg,#0d1726,#111d30);
                    color:#67e8f9;">CE</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<div class="section-gap"></div>', unsafe_allow_html=True)

# =========================================================
# ABOUT / PROOF
# =========================================================
anchor("about")
section_heading(
    "Who I am",
    "The person behind the models.",
    "My work sits at the intersection of analytics, machine learning, research, "
    "and practical problem-solving. I enjoy turning technical complexity into "
    "clear decisions, usable products, and learning experiences."
)

metric_cols = st.columns(4)
for col, (number, label) in zip(metric_cols, HIGHLIGHTS):
    with col:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-number">{number}</div>
                <div class="metric-label">{label}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<div class="section-gap"></div>', unsafe_allow_html=True)

# =========================================================
# CAPABILITIES
# =========================================================
anchor("capabilities")
section_heading(
    "Capabilities",
    "What I bring to the table.",
    "Instead of a wall of tools, I group my skills by the kind of value they create."
)

cap_cols = st.columns(4)
for col, (title, items) in zip(cap_cols, CAPABILITIES.items()):
    with col:
        chips = "".join(f'<span class="chip">{item}</span>' for item in items)
        st.markdown(
            f"""
            <div class="capability-card">
                <h3>{title}</h3>
                {chips}
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<div class="section-gap"></div>', unsafe_allow_html=True)

# =========================================================
# SELECTED WORK
# =========================================================
anchor("work")
section_heading(
    "Selected work",
    "Projects with a purpose.",
    "A selection of analytics, machine-learning, speech, and computer-vision projects."
)

for row_start in range(0, len(PROJECTS), 2):
    cols = st.columns(2, gap="large")
    for col, project in zip(cols, PROJECTS[row_start:row_start + 2]):
        with col:
            render_project(project)
    st.write("")

st.markdown('<div class="section-gap"></div>', unsafe_allow_html=True)

# =========================================================
# JOURNEY
# =========================================================
anchor("journey")
section_heading(
    "Career journey",
    "Research → Analytics → Data Science → AI.",
    "The progression behind my work: research discipline, analytical thinking, "
    "machine learning, teaching, and technical leadership."
)

for exp in EXPERIENCE:
    bullets = "".join(f"<li>{item}</li>" for item in exp["bullets"])
    st.markdown(
        f"""
        <div class="experience-card">
            <div class="experience-role">{exp['role']}</div>
            <div class="experience-company">{exp['company']}</div>
            <div class="experience-period">{exp['period']}</div>
            <ul>{bullets}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="section-gap"></div>', unsafe_allow_html=True)

# =========================================================
# AI LAB
# =========================================================
anchor("lab")
section_heading(
    "Cheshi AI Lab",
    "Where curiosity becomes prototypes.",
    "A dedicated space for experiments that go beyond conventional portfolio projects."
)

lab1, lab2, lab3 = st.columns(3, gap="large")
lab_items = [
    (
        "Computer Vision",
        "Detection, recognition, visual intelligence, and real-time automation."
    ),
    (
        "Responsible & Explainable AI",
        "Exploring models that are not only accurate, but interpretable and trustworthy."
    ),
    (
        "Autonomous Systems",
        "An exploration area for applying data and AI to drones, UTM, and intelligent mobility."
    ),
]

for col, (title, copy) in zip([lab1, lab2, lab3], lab_items):
    with col:
        st.markdown(
            f"""
            <div class="capability-card">
                <div class="project-category">Exploration</div>
                <h3>{title}</h3>
                <div class="project-copy">{copy}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<div class="section-gap"></div>', unsafe_allow_html=True)

# =========================================================
# CONTACT
# =========================================================
anchor("contact")
social_html = "".join(
    f'<a class="social-pill" href="{url}" target="_blank">{name} ↗</a>'
    for name, url in SOCIALS.items()
)

st.markdown(
    f"""
    <div class="contact-panel">
        <div class="section-kicker">Let's build something useful</div>
        <h2>Have a problem worth solving?</h2>
        <div class="section-copy">
            I'm open to conversations around data, analytics, machine learning,
            AI applications, training, research, and collaborative technical projects.
        </div>
        <div class="cta-row">
            <a class="cta-primary" href="mailto:{EMAIL}">Email me ↗</a>
            <a class="cta-secondary" href="{SOCIALS['LinkedIn']}" target="_blank">Connect on LinkedIn ↗</a>
        </div>
        <div class="social-row">
            {social_html}
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f'<div class="footer-note">© Cheshi Emmanuel · {TAGLINE}</div>',
    unsafe_allow_html=True,
)
