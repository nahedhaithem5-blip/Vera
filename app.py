import streamlit as st
import PyPDF2
from docx import Document
from collections import Counter

st.set_page_config(page_title="Vera | Total Analysis", layout="wide")

# Function to analyze document nature
def detect_document_type(text):
    if "بحث" in text or "دراسة" in text or "منهجية" in text: return "Academic Research"
    if "فصل" in text or "حوار" in text or "بطل" in text: return "Creative Writing"
    return "General Report"

def extract_text(file):
    # (نفس دالة الاستخراج السابقة)
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        return " ".join([page.extract_text() for page in reader.pages])
    else:
        doc = Document(file)
        return " ".join([p.text for p in doc.paragraphs])

st.title("🔍 Vera: Intelligent Global Analyzer")

uploaded_file = st.file_uploader("Upload your document")

if uploaded_file:
    text = extract_text(uploaded_file)
    words = text.split()
    doc_type = detect_document_type(text)
    
    # 1. لوحة الإحصائيات الشاملة
    st.write(f"### 📊 Report for: {doc_type}")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Word Count", len(words))
    col2.metric("Lexical Density", f"{len(set(words))/len(words):.2%}")
    col3.metric("Avg Sentence Length", f"{len(words)/max(text.count('.'), 1):.1f}")
    col4.metric("Reading Time", f"{len(words)//200} min")

    # 2. التحليل التفصيلي (الاحترافي)
    with st.expander("📈 Comprehensive Analytical Report", expanded=True):
        st.write("#### Linguistic Complexity")
        st.info("High lexical density indicates professional/academic content.")
        
        st.write("#### Key Themes")
        filtered = [w for w in words if len(w) > 5]
        for word, count in Counter(filtered).most_common(5):
            st.write(f"**{word}**: {count} mentions")
            st.progress(min(count/10, 1.0))

    # 3. محتوى النص (هادئ ومنظم)
    with st.expander("📝 Document Full Text"):
        st.markdown(" ".join(text.split()))
