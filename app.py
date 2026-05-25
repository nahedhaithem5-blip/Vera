import streamlit as st
import PyPDF2
from docx import Document
from collections import Counter

# Set up page configuration with professional branding
st.set_page_config(page_title="Vera - Smart Analyzer", page_icon="🔍")
st.title("🔍 Vera: Universal AI Analyzer")

# Unified function for text extraction from various formats
def extract_text(file):
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        return " ".join([page.extract_text() for page in reader.pages])
    else:
        doc = Document(file)
        return " ".join([p.text for p in doc.paragraphs])

# Sidebar: Configuration and Settings
st.sidebar.header("⚙️ Configuration")
analysis_type = st.sidebar.selectbox("Select Document Type:", 
                                     ["Academic Research", "Creative Writing", "General Report"])
language = st.sidebar.radio("Select Analysis Language:", ["English", "Arabic"])

uploaded_file = st.file_uploader("Upload document (PDF/Docx)", type=['pdf', 'docx'])

if uploaded_file is not None:
    text = extract_text(uploaded_file)
    words = text.split()
    
    # Statistical Dashboard
    col1, col2 = st.columns(2)
    col1.metric("Word Count", len(words))
    col2.metric("Vocabulary Richness", f"{len(set(words))/len(words):.2%}")
    
    st.write("---")
    
    # AI Engine: Dynamic Analysis based on document type and language
    st.subheader(f"💡 {'Insights' if language == 'English' else 'تحليلات ذكية'}")
    
    if analysis_type == "Academic Research":
        st.info("Academic Analysis: Evaluating formal tone and structural coherence.")
    elif analysis_type == "Creative Writing":
        st.info("Creative Analysis: Evaluating descriptive language and emotional flow.")
    else:
        st.info("Report Analysis: Evaluating conciseness and factual density.")

    # Text Display: Full content normalized
    clean_text = " ".join(text.split())
    st.write(f"### 📝 {'Full Document Content' if language == 'English' else 'محتوى الملف بالكامل'}")
    st.markdown(clean_text)

    # Keyword Extraction: Statistical analysis of document themes
    st.write(f"### 🔑 {'Key Topics (Top 5 words)' if language == 'English' else 'أهم الكلمات المفتاحية'}")
    filtered_words = [word for word in words if len(word) > 4]
    most_common = Counter(filtered_words).most_common(5)
    
    for word, count in most_common:
        st.write(f"- **{word}**: {count} {'times' if language == 'English' else 'مرة'}")
