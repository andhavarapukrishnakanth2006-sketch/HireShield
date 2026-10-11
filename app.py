import streamlit as st
import joblib
import re

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="HireShield | AI Job Security",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# PREMIUM GLOBAL CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

:root {
    --bg: #030712;
    --panel: #0a1222;
    --panel2: #0d172a;
    --line: rgba(148,163,184,.14);
    --text: #f8fafc;
    --muted: #8b9ab0;
    --cyan: #22d3ee;
    --blue: #3b82f6;
    --green: #22c55e;
    --yellow: #f59e0b;
    --red: #ef4444;
}

html,
body,
[class*="css"] {
    font-family: "Inter", sans-serif !important;
}

.stApp {
    background:
        radial-gradient(
            circle at 5% 0%,
            rgba(37,99,235,.15),
            transparent 25%
        ),
        radial-gradient(
            circle at 95% 10%,
            rgba(34,211,238,.08),
            transparent 25%
        ),
        linear-gradient(
            135deg,
            #020617 0%,
            #07101f 50%,
            #020617 100%
        );
    color: var(--text);
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

#MainMenu,
header,
footer {
    visibility: hidden;
}

/* ============================================================
   HERO
============================================================ */

.hero {
    position: relative;
    overflow: hidden;

    padding: 48px 55px;

    border-radius: 30px;

    border: 1px solid rgba(56,189,248,.20);

    background:
        radial-gradient(
            circle at 85% 20%,
            rgba(34,211,238,.13),
            transparent 30%
        ),
        radial-gradient(
            circle at 10% 100%,
            rgba(37,99,235,.22),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #081226,
            #0a1730,
            #050b18
        );

    box-shadow:
        0 30px 90px rgba(0,0,0,.40);
}

.hero-brand {
    display: flex;
    align-items: center;
    gap: 15px;
}

.logo {
    width: 58px;
    height: 58px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 17px;

    font-size: 29px;

    background:
        linear-gradient(
            135deg,
            #2563eb,
            #06b6d4
        );

    box-shadow:
        0 12px 35px rgba(37,99,235,.4);
}

.brand-name {
    font-size: 27px;
    font-weight: 900;
    letter-spacing: -1px;
}

.brand-sub {
    color: #67e8f9;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2.3px;
    margin-top: 3px;
}

.online {
    float: right;

    color: #86efac;

    font-size: 11px;
    font-weight: 800;
    letter-spacing: .5px;
}

.hero-content {
    margin-top: 55px;
    max-width: 850px;
}

.eyebrow {
    color: #22d3ee;
    font-size: 11px;
    font-weight: 900;
    letter-spacing: 3px;
}

.hero-title {
    margin-top: 15px;

    font-size: clamp(52px, 6vw, 76px);
    line-height: 1;
    font-weight: 900;

    letter-spacing: -4px;
}

.hero-title span {
    background:
        linear-gradient(
            90deg,
            #38bdf8,
            #22d3ee,
            #60a5fa
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-description {
    max-width: 760px;

    margin-top: 22px;

    color: #a4b1c4;

    font-size: 16px;
    line-height: 1.75;
}

.hero-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 9px;

    margin-top: 25px;
}

.pill {
    padding: 9px 14px;

    border-radius: 50px;

    background: rgba(255,255,255,.045);

    border: 1px solid rgba(255,255,255,.08);

    color: #cbd5e1;

    font-size: 11px;
    font-weight: 700;
}

/* ============================================================
   SECTION HEADINGS
============================================================ */

.section {
    margin-top: 50px;
    margin-bottom: 20px;
}

.section-label {
    color: #22d3ee;

    font-size: 10px;
    font-weight: 900;

    letter-spacing: 2.7px;
}

.section-title {
    margin-top: 7px;

    color: #f8fafc;

    font-size: 34px;
    line-height: 1.15;

    font-weight: 900;

    letter-spacing: -1px;
}

.section-description {
    margin-top: 7px;

    color: #718096;

    font-size: 14px;
    line-height: 1.6;
}

/* ============================================================
   PREMIUM CAPABILITY CARDS
============================================================ */

.capability {
    position: relative;

    min-height: 215px;

    padding: 28px;

    border-radius: 22px;

    border: 1px solid rgba(148,163,184,.13);

    background:
        linear-gradient(
            145deg,
            rgba(13,23,42,.96),
            rgba(7,14,28,.96)
        );

    box-shadow:
        0 15px 45px rgba(0,0,0,.20);

    transition:
        transform .2s ease,
        border-color .2s ease;
}

.capability:hover {
    transform: translateY(-4px);

    border-color:
        rgba(56,189,248,.35);

    box-shadow:
        0 20px 55px rgba(0,0,0,.28),
        0 0 35px rgba(37,99,235,.08);
}

.capability-number {
    color: #334155;

    font-size: 11px;
    font-weight: 900;

    letter-spacing: 2px;
}

.capability-icon {
    margin-top: 20px;

    width: 48px;
    height: 48px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 14px;

    background: rgba(56,189,248,.08);

    border: 1px solid rgba(56,189,248,.14);

    font-size: 23px;
}

.capability-title {
    margin-top: 17px;

    color: #f8fafc;

    font-size: 19px;
    font-weight: 850;
}

.capability-text {
    margin-top: 8px;

    color: #7f8da3;

    font-size: 13px;
    line-height: 1.7;
}

/* ============================================================
   SCANNER
============================================================ */

.scanner {
    padding: 32px;

    border-radius: 28px;

    border: 1px solid rgba(56,189,248,.14);

    background:
        linear-gradient(
            145deg,
            #0b1528,
            #060d1a
        );

    box-shadow:
        0 25px 70px rgba(0,0,0,.28);
}

.scanner-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.scanner-title {
    color: #f8fafc;

    font-size: 22px;
    font-weight: 900;
}

.scanner-status {
    color: #4ade80;

    font-size: 10px;
    font-weight: 800;

    letter-spacing: 1.5px;
}

.scanner-description {
    color: #64748b;

    font-size: 13px;

    margin-top: 5px;
}

/* ============================================================
   INPUT HEADER
============================================================ */

.input-header {
    display: flex;
    justify-content: space-between;

    margin-top: 25px;
    margin-bottom: 8px;
}

.input-title {
    color: #cbd5e1;

    font-size: 12px;
    font-weight: 800;

    letter-spacing: 1px;
}

.input-hint {
    color: #475569;

    font-size: 10px;
}

/* ============================================================
   TEXT AREA
============================================================ */

textarea {
    background: #030817 !important;

    color: #e2e8f0 !important;

    border:
        1px solid #1e304d !important;

    border-radius:
        16px !important;

    font-family:
        "Inter", sans-serif !important;

    font-size:
        14px !important;

    line-height:
        1.8 !important;
}

textarea:focus {
    border-color:
        #22d3ee !important;

    box-shadow:
        0 0 0 1px rgba(34,211,238,.18) !important;
}

/* ============================================================
   BUTTONS
============================================================ */

.stButton > button {
    min-height: 46px !important;

    border-radius: 12px !important;

    font-family:
        "Inter", sans-serif !important;

    font-size: 12px !important;

    font-weight: 750 !important;

    background:
        rgba(255,255,255,.035) !important;

    color: #cbd5e1 !important;

    border:
        1px solid rgba(148,163,184,.16) !important;
}

.stButton > button:hover {
    color: white !important;

    border-color:
        rgba(56,189,248,.45) !important;

    background:
        rgba(56,189,248,.07) !important;
}

/* ============================================================
   MAIN SCAN BUTTON
============================================================ */

.scan-button .stButton > button {
    height: 64px !important;

    font-size: 16px !important;

    font-weight: 850 !important;

    letter-spacing: 1px !important;

    background:
        linear-gradient(
            135deg,
            #2563eb,
            #0891b2
        ) !important;

    color: white !important;

    border: none !important;

    box-shadow:
        0 15px 40px rgba(37,99,235,.28) !important;
}

.scan-button .stButton > button:hover {
    transform: translateY(-2px);

    background:
        linear-gradient(
            135deg,
            #1d4ed8,
            #0e7490
        ) !important;

    box-shadow:
        0 20px 50px rgba(37,99,235,.38) !important;
}

/* ============================================================
   RESULT
============================================================ */

.result {
    margin-top: 30px;

    padding: 40px;

    border-radius: 28px;

    background:
        radial-gradient(
            circle at 85% 10%,
            rgba(239,68,68,.13),
            transparent 30%
        ),
        linear-gradient(
            145deg,
            #180b12,
            #0e070c
        );

    border:
        1px solid rgba(239,68,68,.30);

    box-shadow:
        0 25px 65px rgba(0,0,0,.3);
}

.result.medium {
    background:
        radial-gradient(
            circle at 85% 10%,
            rgba(245,158,11,.13),
            transparent 30%
        ),
        linear-gradient(
            145deg,
            #181207,
            #100b05
        );

    border-color:
        rgba(245,158,11,.30);
}

.result.low {
    background:
        radial-gradient(
            circle at 85% 10%,
            rgba(34,197,94,.13),
            transparent 30%
        ),
        linear-gradient(
            145deg,
            #08170f,
            #06100b
        );

    border-color:
        rgba(34,197,94,.30);
}

.result-level {
    font-size: 11px;

    font-weight: 900;

    letter-spacing: 3px;
}

.result-title {
    margin-top: 8px;

    color: #f8fafc;

    font-size: 31px;

    font-weight: 900;

    letter-spacing: -.8px;
}

.result-description {
    margin-top: 8px;

    color: #94a3b8;

    font-size: 14px;

    line-height: 1.6;
}

.risk-number {
    margin-top: 25px;

    font-size: 72px;

    line-height: 1;

    font-weight: 900;

    letter-spacing: -4px;
}

.risk-label {
    margin-top: 8px;

    color: #64748b;

    font-size: 10px;

    font-weight: 900;

    letter-spacing: 2.5px;
}

/* ============================================================
   METRICS
============================================================ */

.metric {
    min-height: 140px;

    padding: 24px;

    border-radius: 19px;

    border: 1px solid rgba(148,163,184,.13);

    background:
        linear-gradient(
            145deg,
            #0d172b,
            #080f1d
        );

    box-shadow:
        0 12px 35px rgba(0,0,0,.18);
}

.metric-label {
    color: #64748b;

    font-size: 10px;

    font-weight: 850;

    letter-spacing: 1.5px;

    text-transform: uppercase;
}

.metric-value {
    margin-top: 10px;

    color: #f8fafc;

    font-size: 32px;

    line-height: 1.1;

    font-weight: 900;

    letter-spacing: -1px;
}

.metric-description {
    margin-top: 6px;

    color: #64748b;

    font-size: 11px;
}

/* ============================================================
   THREAT INTELLIGENCE
============================================================ */

.threat-panel {
    padding: 28px;

    border-radius: 24px;

    border:
        1px solid rgba(239,68,68,.18);

    background:
        linear-gradient(
            145deg,
            #0f111d,
            #080c16
        );
}

.threat-header {
    color: #f8fafc;

    font-size: 19px;

    font-weight: 900;

    margin-bottom: 17px;
}

.tag {
    display: inline-block;

    padding: 10px 14px;

    margin: 4px;

    border-radius: 10px;

    color: #fca5a5;

    font-size: 11px;

    font-weight: 750;

    background:
        rgba(239,68,68,.07);

    border:
        1px solid rgba(239,68,68,.18);
}

/* ============================================================
   RECOMMENDATION
============================================================ */

.recommendation {
    margin-top: 20px;

    padding: 28px;

    border-radius: 24px;

    border:
        1px solid rgba(56,189,248,.18);

    background:
        radial-gradient(
            circle at 90% 0%,
            rgba(56,189,248,.10),
            transparent 30%
        ),
        #091323;
}

.recommendation-label {
    color: #38bdf8;

    font-size: 10px;

    font-weight: 900;

    letter-spacing: 2px;
}

.recommendation-title {
    margin-top: 9px;

    color: #f8fafc;

    font-size: 20px;

    font-weight: 900;
}

.recommendation-text {
    margin-top: 8px;

    color: #8190a6;

    font-size: 13px;

    line-height: 1.75;
}

/* ============================================================
   HOW IT WORKS
============================================================ */

.pipeline {
    position: relative;

    padding: 35px;

    border-radius: 28px;

    border:
        1px solid rgba(148,163,184,.13);

    background:
        linear-gradient(
            145deg,
            #0b1425,
            #060d19
        );
}

.pipeline-card {
    position: relative;

    min-height: 190px;

    padding: 25px;

    border-radius: 20px;

    border:
        1px solid rgba(56,189,248,.12);

    background:
        rgba(255,255,255,.025);
}

.pipeline-number {
    color: #22d3ee;

    font-size: 10px;

    font-weight: 900;

    letter-spacing: 2px;
}

.pipeline-icon {
    margin-top: 17px;

    font-size: 30px;
}

.pipeline-title {
    margin-top: 13px;

    color: #f8fafc;

    font-size: 19px;

    font-weight: 850;
}

.pipeline-text {
    margin-top: 7px;

    color: #718096;

    font-size: 12px;

    line-height: 1.65;
}

/* ============================================================
   FOOTER
============================================================ */

.footer {
    margin-top: 50px;

    padding-top: 24px;

    border-top:
        1px solid rgba(148,163,184,.09);

    color: #475569;

    text-align: center;

    font-size: 10px;

    line-height: 1.7;
}

/* ============================================================
   MOBILE
============================================================ */

@media (max-width: 768px) {

    .hero {
        padding: 32px;
    }

    .hero-title {
        font-size: 45px;
        letter-spacing: -2px;
    }

    .section-title {
        font-size: 28px;
    }

    .scanner {
        padding: 22px;
    }

    .result {
        padding: 27px;
    }

    .risk-number {
        font-size: 52px;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load("models/job_detector.pkl")


model = load_model()


# ============================================================
# SESSION STATE
# ============================================================

if "job_input" not in st.session_state:
    st.session_state.job_input = ""


# ============================================================
# HERO
# ============================================================

st.html("""
<div class="hero">

    <div class="online">
        ● SYSTEM ONLINE
    </div>

    <div class="hero-brand">

        <div class="logo">
            🛡️
        </div>

        <div>

            <div class="brand-name">
                HireShield
            </div>

            <div class="brand-sub">
                AI JOB SECURITY ENGINE
            </div>

        </div>

    </div>

    <div class="hero-content">

        <div class="eyebrow">
            INTELLIGENT FRAUD DETECTION
        </div>

        <div class="hero-title">
            Detect fake jobs.<br>
            <span>Protect your career.</span>
        </div>

        <div class="hero-description">
            HireShield analyzes job postings using Natural Language
            Processing and Machine Learning to identify suspicious
            patterns and estimate potential fraud risk before you apply.
        </div>

        <div class="hero-pills">

            <div class="pill">🤖 AI Analysis</div>
            <div class="pill">🔎 Threat Detection</div>
            <div class="pill">📊 Risk Scoring</div>
            <div class="pill">⚡ Instant Screening</div>

        </div>

    </div>

</div>
""")


# ============================================================
# CORE CAPABILITIES
# ============================================================

st.html("""
<div class="section">

    <div class="section-label">
        CORE CAPABILITIES
    </div>

    <div class="section-title">
        Smart Protection Layer
    </div>

    <div class="section-description">
        Four intelligent layers working together to screen suspicious job postings.
    </div>

</div>
""")


c1, c2, c3, c4 = st.columns(4)


with c1:
    st.html("""
    <div class="capability">

        <div class="capability-number">
            01 / NLP
        </div>

        <div class="capability-icon">
            🧠
        </div>

        <div class="capability-title">
            NLP Analysis
        </div>

        <div class="capability-text">
            Examines the language and structure of a job posting
            using TF-IDF based text analysis.
        </div>

    </div>
    """)


with c2:
    st.html("""
    <div class="capability">

        <div class="capability-number">
            02 / RISK
        </div>

        <div class="capability-icon">
            🎯
        </div>

        <div class="capability-title">
            Risk Scoring
        </div>

        <div class="capability-text">
            Generates an estimated fraud-risk probability
            from the trained machine-learning model.
        </div>

    </div>
    """)


with c3:
    st.html("""
    <div class="capability">

        <div class="capability-number">
            03 / THREAT
        </div>

        <div class="capability-icon">
            🚨
        </div>

        <div class="capability-title">
            Threat Indicators
        </div>

        <div class="capability-text">
            Detects suspicious patterns involving fees,
            urgency, guaranteed income and sensitive information.
        </div>

    </div>
    """)


with c4:
    st.html("""
    <div class="capability">

        <div class="capability-number">
            04 / SCREEN
        </div>

        <div class="capability-icon">
            ⚡
        </div>

        <div class="capability-title">
            Instant Screening
        </div>

        <div class="capability-text">
            Converts the analysis into an understandable
            security assessment within seconds.
        </div>

    </div>
    """)


# ============================================================
# SECURITY SCANNER
# ============================================================

st.html("""
<div class="section">

    <div class="section-label">
        SECURITY SCANNER
    </div>

    <div class="section-title">
        Analyze a Job Posting
    </div>

    <div class="section-description">
        Submit a job advertisement and let HireShield evaluate its potential risk.
    </div>

</div>
""")


st.html("""
<div class="scanner">

    <div class="scanner-top">

        <div>

            <div class="scanner-title">
                🔐 Job Posting Analyzer
            </div>

            <div class="scanner-description">
                AI-assisted screening workspace
            </div>

        </div>

        <div class="scanner-status">
            ● READY TO SCAN
        </div>

    </div>

</div>
""")


# ============================================================
# EXAMPLE BUTTONS
# ============================================================

b1, b2, b3 = st.columns([1, 1, 3])


with b1:

    if st.button(
        "✓  Load Safe Example",
        use_container_width=True
    ):

        st.session_state.job_input = """Software Developer

We are looking for a Software Developer to join our engineering team.

Requirements:
Bachelor's degree in Computer Science or related field.
Knowledge of Python, SQL and software development.
Good communication and problem-solving skills.

Responsibilities:
Develop and maintain software applications.
Work with the engineering team to design and test features.
Participate in code reviews and technical discussions.

Benefits:
Competitive salary, health insurance and professional development opportunities.

Interested candidates can apply through our official company careers portal."""

        st.rerun()


with b2:

    if st.button(
        "⚠  Load Scam Example",
        use_container_width=True
    ):

        st.session_state.job_input = """URGENT WORK FROM HOME JOB!!!
Earn ₹50,000 every week with NO EXPERIENCE required.
Limited positions available. Immediate joining.
Pay a registration fee of ₹999 to confirm your position.
Send your bank account details and contact us through WhatsApp immediately.
Guaranteed income. Easy money. Start today!!!"""

        st.rerun()


# ============================================================
# INPUT HEADER
# ============================================================

st.html("""
<div class="input-header">

    <div class="input-title">
        JOB POSTING CONTENT
    </div>

    <div class="input-hint">
        Paste complete advertisement
    </div>

</div>
""")


# ============================================================
# TEXT AREA
# ============================================================

job_text = st.text_area(
    "Job Posting",
    key="job_input",
    height=330,
    placeholder="""Paste the complete job posting here...

Example:

Job Title: Software Developer

Company: ABC Technologies
Location: Hyderabad
Description:
We are looking for a Python developer...
Requirements:
Python, SQL, problem-solving...
Responsibilities:...
Benefits:...
""",
    label_visibility="collapsed"
)


# ============================================================
# SCAN BUTTON
# ============================================================

st.markdown(
    '<div class="scan-button">',
    unsafe_allow_html=True
)

scan = st.button(
    "🛡️   SCAN JOB POSTING",
    use_container_width=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# ANALYSIS
# ============================================================

if scan:

    if not job_text.strip():

        st.warning(
            "Please paste a job posting before scanning."
        )

    else:

        prediction = model.predict([job_text])[0]

        probabilities = model.predict_proba([job_text])[0]

        fraud_risk = probabilities[1] * 100

        model_confidence = max(probabilities) * 100


        # ====================================================
        # TEXT STATISTICS
        # ====================================================

        word_count = len(job_text.split())

        character_count = len(job_text)

        urls = re.findall(
            r"https?://[^\s]+|www\.[^\s]+",
            job_text,
            flags=re.IGNORECASE
        )

        url_count = len(urls)


        # ====================================================
        # SUSPICIOUS KEYWORDS
        # ====================================================

        suspicious_keywords = [
            "pay",
            "payment",
            "registration fee",
            "deposit",
            "urgent",
            "immediately",
            "guaranteed income",
            "easy money",
            "work from home",
            "no experience",
            "whatsapp",
            "telegram",
            "bank account",
            "credit card"
        ]

        detected_keywords = []

        lower_text = job_text.lower()

        for keyword in suspicious_keywords:

            if keyword in lower_text:

                detected_keywords.append(keyword)

        warning_count = len(detected_keywords)


        # ====================================================
        # RISK LEVEL
        # ====================================================

        if fraud_risk >= 60:

            risk_level = "HIGH RISK"

            result_class = "result"

            risk_color = "#ef4444"

            result_title = "Potentially Fraudulent Job Posting"

            result_description = (
                "The posting contains patterns associated "
                "with potentially fraudulent job advertisements."
            )

            recommendation_title = (
                "DO NOT PROCEED WITHOUT VERIFICATION"
            )

            recommendation_text = (
                "Do not pay registration or processing fees. "
                "Avoid sharing banking information or sensitive "
                "personal information. Verify the employer through "
                "an official company website or trusted platform."
            )

        elif fraud_risk >= 30:

            risk_level = "MEDIUM RISK"

            result_class = "result medium"

            risk_color = "#f59e0b"

            result_title = "Suspicious Job Posting"

            result_description = (
                "The posting contains patterns that require "
                "additional verification before applying."
            )

            recommendation_title = (
                "VERIFY BEFORE APPLYING"
            )

            recommendation_text = (
                "Verify the company, recruiter, job details "
                "and application process before sharing personal information."
            )

        else:

            risk_level = "LOW RISK"

            result_class = "result low"

            risk_color = "#22c55e"

            result_title = "Likely Genuine Job Posting"

            result_description = (
                "The model found relatively few indicators "
                "associated with fraudulent job postings."
            )

            recommendation_title = (
                "STANDARD SAFETY CHECK"
            )

            recommendation_text = (
                "Continue to verify the employer independently "
                "and avoid sharing sensitive information unnecessarily."
            )


        # ====================================================
        # RESULT
        # ====================================================

        st.html(f"""
        <div class="{result_class}">

            <div class="result-level"
                 style="color:{risk_color};">

                {risk_level}

            </div>

            <div class="result-title">

                {result_title}

            </div>

            <div class="result-description">

                {result_description}

            </div>

            <div class="risk">

                <div class="risk-number"
                     style="color:{risk_color};">

                    {fraud_risk:.2f}%

                </div>

                <div class="risk-label">
                    FRAUD RISK
                </div>

            </div>

            <div style="
                margin-top:25px;
                width:100%;
                height:10px;
                background:#1e293b;
                border-radius:20px;
                overflow:hidden;
            ">

                <div style="
                    width:{fraud_risk}%;
                    height:100%;
                    background:{risk_color};
                    border-radius:20px;
                "></div>

            </div>

        </div>
        """)


        # ====================================================
        # METRICS
        # ====================================================

        st.markdown("<br>", unsafe_allow_html=True)

        m1, m2, m3, m4 = st.columns(4)


        with m1:

            st.html(f"""
            <div class="metric">

                <div class="metric-label">
                    Fraud Risk
                </div>

                <div class="metric-value">
                    {fraud_risk:.2f}%
                </div>

                <div class="metric-description">
                    Estimated probability
                </div>

            </div>
            """)


        with m2:

            st.html(f"""
            <div class="metric">

                <div class="metric-label">
                    Model Confidence
                </div>

                <div class="metric-value">
                    {model_confidence:.2f}%
                </div>

                <div class="metric-description">
                    Prediction confidence
                </div>

            </div>
            """)


        with m3:

            st.html(f"""
            <div class="metric">

                <div class="metric-label">
                    Warning Indicators
                </div>

                <div class="metric-value">
                    {warning_count}
                </div>

                <div class="metric-description">
                    Suspicious patterns
                </div>

            </div>
            """)


        with m4:

            st.html(f"""
            <div class="metric">

                <div class="metric-label">
                    URLs Detected
                </div>

                <div class="metric-value">
                    {url_count}
                </div>

                <div class="metric-description">
                    Links found
                </div>

            </div>
            """)


        # ====================================================
        # THREAT INTELLIGENCE
        # ====================================================

        st.html("""
        <div class="section">

            <div class="section-label">
                THREAT INTELLIGENCE
            </div>

            <div class="section-title">
                Suspicious Indicators
            </div>

            <div class="section-description">
                Signals detected inside the submitted job advertisement.
            </div>

        </div>
        """)


        if detected_keywords:

            tags = ""

            for keyword in detected_keywords:

                tags += f"""
                <span class="tag">
                    🔴 {keyword}
                </span>
                """

            st.html(f"""
            <div class="threat-panel">

                <div class="threat-header">
                    🚨 Detected Warning Signals
                </div>

                {tags}

            </div>
            """)

        else:

            st.success(
                "No suspicious keywords from the current indicator list were detected."
            )


        # ====================================================
        # ADDITIONAL METRICS
        # ====================================================

        st.markdown("<br>", unsafe_allow_html=True)

        x1, x2, x3 = st.columns(3)


        with x1:

            st.html(f"""
            <div class="metric">

                <div class="metric-label">
                    Word Count
                </div>

                <div class="metric-value">
                    {word_count}
                </div>

                <div class="metric-description">
                    Words analyzed
                </div>

            </div>
            """)


        with x2:

            st.html(f"""
            <div class="metric">

                <div class="metric-label">
                    Characters
                </div>

                <div class="metric-value">
                    {character_count}
                </div>

                <div class="metric-description">
                    Characters analyzed
                </div>

            </div>
            """)


        with x3:

            st.html(f"""
            <div class="metric">

                <div class="metric-label">
                    Risk Classification
                </div>

                <div class="metric-value"
                     style="color:{risk_color};">

                    {risk_level.split()[0]}

                </div>

                <div class="metric-description">
                    Current threat level
                </div>

            </div>
            """)


        # ====================================================
        # RECOMMENDATION
        # ====================================================

        st.html(f"""
        <div class="recommendation">

            <div class="recommendation-label">
                🛡️ SECURITY RECOMMENDATION
            </div>

            <div class="recommendation-title">
                {recommendation_title}
            </div>

            <div class="recommendation-text">
                {recommendation_text}
            </div>

        </div>
        """)


# ============================================================
# HOW IT WORKS
# ============================================================

st.html("""
<div class="section">

    <div class="section-label">
        HOW IT WORKS
    </div>

    <div class="section-title">
        Three Layers of Protection
    </div>

    <div class="section-description">
        From raw job-posting text to an understandable security assessment.
    </div>

</div>
""")


st.html("""
<div class="pipeline">
</div>
""")


p1, p2, p3 = st.columns(3)


with p1:

    st.html("""
    <div class="pipeline-card">

        <div class="pipeline-number">
            01 / INGEST
        </div>

        <div class="pipeline-icon">
            📄
        </div>

        <div class="pipeline-title">
            Read the Posting
        </div>

        <div class="pipeline-text">
            HireShield receives the job advertisement
            and prepares its content for analysis.
        </div>

    </div>
    """)


with p2:

    st.html("""
    <div class="pipeline-card">

        <div class="pipeline-number">
            02 / ANALYZE
        </div>

        <div class="pipeline-icon">
            🧠
        </div>

        <div class="pipeline-title">
            Detect Patterns
        </div>

        <div class="pipeline-text">
            The NLP model analyzes language while
            the security layer checks suspicious indicators.
        </div>

    </div>
    """)


with p3:

    st.html("""
    <div class="pipeline-card">

        <div class="pipeline-number">
            03 / PROTECT
        </div>

        <div class="pipeline-icon">
            🛡️
        </div>

        <div class="pipeline-title">
            Understand the Risk
        </div>

        <div class="pipeline-text">
            The final report provides risk scoring,
            warning signals and safety recommendations.
        </div>

    </div>
    """)


# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="footer">

    🛡️ <b>HireShield</b> · AI Job Security Engine

    <br>

    AI-assisted screening · Always verify employers independently

</div>
""")