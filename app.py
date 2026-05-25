import streamlit as st
import PyPDF2
from docx import Document
from collections import Counter

st.set_page_config(page_title="Vera | Global Analyzer", layout="wide")

def extract_text(file):
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        return " ".join([page.extract_text() for page in reader.pages])
    else:
        doc = Document(file)
        return " ".join([p.text for p in doc.paragraphs])

# Sidebar: Controls
st.sidebar.header("⚙️ System Controls")
language = st.sidebar.radio("Language:", ["English", "Arabic"])
user_doc_type = st.sidebar.selectbox("Document Context:", ["Academic Research", "Creative Writing", "General Report", "Auto-Detect"])

uploaded_file = st.file_uploader("Upload your document")

if uploaded_file:
    text = extract_text(uploaded_file)
    words = text.split()
    
    # Logic: Auto-detection if selected
    doc_type = user_doc_type
    if doc_type == "Auto-Detect":
        if "بحث" in text or "دراسة" in text: doc_type = "Academic Research"
        elif "فصل" in text or "شخصية" in text: doc_type = "Creative Writing"
        else: doc_type = "General Report"
    
    # Metrics
    st.write(f"### 📊 Report: {doc_type} | {'Language: ' + language}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Words", len(words))
    col2.metric("Unique Density", f"{len(set(words))/len(words):.2%}")
    col3.metric("Reading Time", f"{len(words)//200} min")

    # Detailed Professional Analysis
    with st.expander("📈 Comprehensive Analytical Report", expanded=True):
        st.write("#### Linguistic Complexity")
        st.info("Analysis of vocabulary richness and sentence structure density.")
        
        st.write("#### Key Themes")
        filtered = [w for w in words if len(w) > 5]
        for word, count in Counter(filtered).most_common(5):
            st.write(f"**{word}**: {count} mentions")
            st.progress(min(count/10, 1.0))

    with st.expander("📝 Full Document Content"):
        st.markdown(" ".join(text.split()))
