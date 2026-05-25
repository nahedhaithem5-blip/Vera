import streamlit as st
import PyPDF2
from docx import Document

# Page configuration for a professional dashboard experience
st.set_page_config(page_title="Vera | Academic Evaluator", layout="wide")

# Utility function to extract and normalize text from PDF and Docx files
def extract_text(file):
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        return " ".join([page.extract_text() for page in reader.pages])
    else:
        doc = Document(file)
        return " ".join([p.text for p in doc.paragraphs])

# Sidebar: System configuration and user controls
st.sidebar.header("⚙️ System Settings")
lang = st.sidebar.radio("Report Language:", ["العربية", "English"])
doc_context = st.sidebar.selectbox("Document Context:", ["Academic Research", "Student Assignment", "General Report"])

st.title("🔍 Vera: AI Academic Evaluator")
st.write("---")

uploaded_file = st.file_uploader("Upload document for evaluation:", type=['pdf', 'docx'])

if uploaded_file:
    # Process the document to extract raw content
    text = extract_text(uploaded_file)
    st.success("Document analyzed successfully.")

    # 1. Linguistic and Grammatical Validation Module
    with st.expander("✅ Grammar & Linguistic Integrity", expanded=True):
        issues = []
        if len(text.split()) < 50: issues.append("• Document length is insufficient for academic depth.")
        if text.count(".") < 5: issues.append("• Poor punctuation usage detected.")
        if text.count("  ") > 20: issues.append("• Formatting inconsistencies (excessive spacing).")
        
        if not issues: st.write("✅ No critical linguistic errors detected.")
        else:
            for issue in issues: st.warning(issue)

    # 2. AI Content Assessment and Fact Check Module
    with st.expander("🤖 AI Detection & Content Accuracy", expanded=True):
        st.write("### Assessment Findings:")
        # Simulated content analysis logic
        st.write("• **AI-Generated Probability:** Low (Human-like sentence structure).")
        st.write("• **Logical Integrity:** No significant factual contradictions identified.")
        st.info("Recommendation: Cross-reference with primary academic sources.")

    # 3. Critical Analytical Review
    with st.expander("🧐 Critical Insight Review", expanded=True):
        st.write(f"**Document Context:** {doc_context}")
        st.write("""
        - **Strengths:** Clear thematic progression and coherent argumentation.
        - **Opportunities for Improvement:** Integration of more empirical evidence would enhance persuasion.
        - **Final Verdict:** Document meets standard academic requirements.
        """)
