import streamlit as st
from services.azure_openai import analyze_complexity

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="AI Complexity Analyzer",
    page_icon="🤖",
    layout="wide"
)

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

custom_css = """
<style>

.main {
    background-color: #0e1117;
}

.block-container {
    padding-top: 2rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

h1, h2, h3 {
    color: white;
}

label {
    color: white !important;
    font-weight: 500;
}

.stTextInput input,
.stTextArea textarea,
.stSelectbox div,
.stMultiSelect div,
.stNumberInput input {
    border-radius: 10px !important;
}

.result-box {
    background-color: #1c1f26;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #2d3139;
    color: white;
    margin-top: 20px;
}

/* ---------------- MOBILE RESPONSIVE ---------------- */

@media (max-width: 768px) {

    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        padding-top: 1rem !important;
    }

    h1 {
        font-size: 28px !important;
        text-align: center;
    }

    h2 {
        font-size: 22px !important;
    }

    h3 {
        font-size: 18px !important;
    }

    .stButton button {
        width: 100%;
        height: 50px;
        border-radius: 12px;
        font-size: 16px;
    }

    .result-box {
        padding: 18px !important;
        font-size: 15px !important;
    }

    .stTextInput input,
    .stTextArea textarea,
    .stSelectbox div,
    .stMultiSelect div,
    .stNumberInput input {
        font-size: 16px !important;
    }

}

</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.title("🤖 AI Complexity Analyzer")

st.markdown(
    "Enterprise AI Transformation & Business Complexity Assessment Platform"
)

st.divider()

# -------------------------------------------------
# COMPANY INFORMATION
# -------------------------------------------------

st.subheader("🏢 Company Information")

col1, col2 = st.columns([1,1], gap="large")

with col1:
    company_name = st.text_input("Company Name")

with col2:
    industry = st.selectbox(
        "Industry Domain",
        [
            "Insurance",
            "Banking",
            "Healthcare",
            "Retail",
            "Manufacturing",
            "Technology"
        ]
    )

company_address = st.text_area(
    "Company Address",
    height=100
)

st.divider()

# -------------------------------------------------
# APPLICATION INFORMATION
# -------------------------------------------------

st.subheader("⚙️ Application Information")

col3, col4 = st.columns([1,1], gap="large")

with col3:
    application_type = st.selectbox(
        "Application Type",
        [
            "Customer Facing",
            "Internal Tool",
            "Analytics Platform",
            "Workflow System",
            "AI Assistant"
        ]
    )

with col4:
    architecture_type = st.selectbox(
        "Architecture Type",
        [
            "Monolith",
            "Microservices",
            "Serverless",
            "Hybrid"
        ]
    )

st.divider()

# -------------------------------------------------
# AI & AUTOMATION
# -------------------------------------------------

st.subheader("🧠 AI & Automation")

ai_capabilities = st.multiselect(
    "AI Capabilities Used",
    [
        "LLM",
        "Chatbot",
        "Predictive Analytics",
        "NLP",
        "Recommendation Engine",
        "RAG",
        "Computer Vision"
    ]
)

col5, col6 = st.columns([1,1], gap="large")

with col5:
    human_approval = st.selectbox(
        "Human Approval Required",
        ["Yes", "No", "Partial"]
    )

with col6:
    workflow_type = st.selectbox(
        "Workflow Type",
        [
            "Manual",
            "Semi-Automated",
            "Fully Automated"
        ]
    )

st.divider()

# -------------------------------------------------
# INTEGRATION & COMPLIANCE
# -------------------------------------------------

st.subheader("🔗 Integration & Compliance")

col7, col8 = st.columns([1,1], gap="large")

with col7:
    api_integrations = st.number_input(
        "API Integrations Count",
        min_value=0,
        max_value=500,
        value=5
    )

with col8:
    integrated_systems = st.number_input(
        "Number of Integrated Systems",
        min_value=1,
        max_value=100,
        value=3
    )

col9, col10 = st.columns([1,1], gap="large")

with col9:
    realtime_processing = st.selectbox(
        "Real-time Processing Required",
        ["Yes", "No"]
    )

with col10:
    compliance = st.multiselect(
        "Compliance Requirement",
        [
            "HIPAA",
            "GDPR",
            "PCI-DSS",
            "SOC2",
            "ISO27001"
        ]
    )

st.divider()

# -------------------------------------------------
# ANALYZE BUTTON
# -------------------------------------------------

analyze = st.button("🚀 Analyze Complexity")

# -------------------------------------------------
# ANALYSIS SECTION
# -------------------------------------------------

if analyze:

    user_input = f"""
    Company Name: {company_name}

    Company Address: {company_address}

    Industry Domain: {industry}

    Application Type: {application_type}

    Architecture Type: {architecture_type}

    AI Capabilities Used: {', '.join(ai_capabilities)}

    Human Approval Required: {human_approval}

    Workflow Type: {workflow_type}

    API Integrations Count: {api_integrations}

    Real-time Processing Required: {realtime_processing}

    Number of Integrated Systems: {integrated_systems}

    Compliance Requirement: {', '.join(compliance)}
    """

    with st.spinner("Analyzing enterprise complexity..."):

        response = analyze_complexity(user_input)

    st.subheader("📊 Analysis Results")

    st.markdown(
        f"""
        <div class="result-box">
        {response}
        </div>
        """,
        unsafe_allow_html=True
    )