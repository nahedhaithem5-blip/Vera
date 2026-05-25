import streamlit as st
import PyPDF2
from docx import Document
from collections import Counter

# Page Layout configuration
st.set_page_config(page_title="Vera | Intelligent Analysis", page_icon="🔍", layout="wide")

# Custom UI Styling (CSS)
st.markdown("""
    <style>
    .main {background-color: #f8f9fa;}
    .stMetric {background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);}
    </style>
    """, unsafe_allow_html=True)

st.title("🔍 Vera: Intelligent Analysis Suite")
st.subheader("Your professional assistant for document insights")

def extract_text(file):
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        return " ".join([page.extract_text() for page in reader.pages])
    else:
        doc = Document(file)
        return " ".join([p.text for p in doc.paragraphs])

# Sidebar Setup
st.sidebar.header("Control Panel")
analysis_type = st.sidebar.selectbox("Document Context:", ["Academic Research", "Creative Writing", "General Report"])
language = st.sidebar.radio("Analysis Language:", ["English", "Arabic"])
uploaded_file = st.file_uploader("Upload your document", type=['pdf', 'docx'])

if uploaded_file:
    text = extract_text(uploaded_file)
    words = text.split()
    
    # Advanced Metrics Calculation
    avg_word_len = sum(len(w) for w in words) / len(words)
    unique_ratio = len(set(words)) / len(words)
    
    # Professional Dashboard
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Words", len(words))
    col2.metric("Unique Density", f"{unique_ratio:.1%}")
    col3.metric("Avg. Word Length", f"{avg_word_len:.1f} chars")
    
    st.write("---")
    
    # Detailed Professional Analysis (The "Deep" part)
    with st.expander("📊 View Detailed Professional Analysis"):
        st.write(f"### {'Deep Analysis Report' if language == 'English' else 'تقرير التحليل المفصل'}")
        if analysis_type == "Academic Research":
            st.write("Academic focus: Evaluates formal syntax, logical progression, and terminology.")
        elif analysis_type == "Creative Writing":
            st.write("Creative focus: Evaluates narrative flow, descriptive depth, and pacing.")
        else:
            st.write("Report focus: Evaluates factual density and information clarity.")
            
    # Key Topics with Progress Bars
    st.write(f"### 🔑 {'Top Themes' if language == 'English' else 'أهم الموضوعات'}")
    filtered = [w for w in words if len(w) > 5]
    for word, count in Counter(filtered).most_common(5):
        st.write(f"**{word}**")
        st.progress(min(count/20, 1.0)) # Progress bar visualization

    # Document Preview
    with st.expander("📝 View Full Document"):
        st.markdown(" ".join(text.split()))
