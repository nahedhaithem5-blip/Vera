import streamlit as st
import PyPDF2
from docx import Document
from collections import Counter

# Page Configuration
st.set_page_config(page_title="Vera | Intelligent Critical Analysis", layout="wide")

# Function to extract text from files
def extract_text(file):
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        return " ".join([page.extract_text() for page in reader.pages])
    else:
        doc = Document(file)
        return " ".join([p.text for p in doc.paragraphs])

# Sidebar Controls
st.sidebar.header("⚙️ System Control")
language = st.sidebar.radio("Analysis Language:", ["English", "Arabic"])
user_doc_type = st.sidebar.selectbox("Document Type:", ["Auto-Detect", "Academic Research", "Creative Writing", "General Report"])

st.title("🔍 Vera: Critical Document Intelligence")
uploaded_file = st.file_uploader("Upload document for analysis", type=['pdf', 'docx'])

if uploaded_file:
    text = extract_text(uploaded_file)
    words = text.split()
    
    # Auto-detection Logic
    doc_type = user_doc_type
    if doc_type == "Auto-Detect":
        if any(word in text for word in ["بحث", "دراسة", "منهجية"]): doc_type = "Academic Research"
        elif any(word in text for word in ["فصل", "حوار", "شخصية"]): doc_type = "Creative Writing"
        else: doc_type = "General Report"
    
    st.subheader(f"Analysis Profile: {doc_type}")
    
    # Critical Insight Engine
    with st.expander("🧐 Deep Critical Analysis", expanded=True):
        st.write("### 🧠 Critical Insights")
        
        # Linguistic Analysis
        sentence_count = max(text.count('.') + text.count('!') + text.count('?'), 1)
        avg_sentence_len = len(words) / sentence_count
        
        # Tone/Sentiment Logic
        pos_markers = ['ابتسم', 'قوي', 'نجاح', 'حب', 'إبداع']
        neg_markers = ['حزن', 'ألم', 'خوف', 'فشل', 'صعب']
        tone = "Emotional & Narrative" if sum(text.count(w) for w in pos_markers + neg_markers) > 5 else "Formal & Objective"
        
        st.write(f"- **Writing Style:** {'Complex/Formal' if avg_sentence_len > 15 else 'Direct/Punchy'}")
        st.write(f"- **Tone Interpretation:** {tone}")
        st.write(f"- **Critical Observation:** This document exhibits a focus on {'thematic development' if doc_type == 'Creative Writing' else 'data-driven information'}.")
        
    # Statistical Overview
    col1, col2, col3 = st.columns(3)
    col1.metric("Word Count", len(words))
    col2.metric("Unique Vocabulary", f"{len(set(words))/len(words):.1%}")
    col3.metric("Reading Time", f"{len(words)//200} min")

    # Content Display
    with st.expander("📝 Document Content"):
        st.markdown(" ".join(text.split()))

# Image of natural language processing text analysis pipeline
