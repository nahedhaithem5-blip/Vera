import streamlit as st
import PyPDF2
from docx import Document

st.title("🔍 Vera: AI Academic Assistant")

def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def read_docx(file):
    doc = Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text
    return text

uploaded_file = st.file_uploader("📂 Upload your research paper", type=['pdf', 'docx'])

if uploaded_file is not None:
    # تحديد نوع الملف وقراءته
    if uploaded_file.type == "application/pdf":
        text = read_pdf(uploaded_file)
    else:
        text = read_docx(uploaded_file)
    
    st.success("✅ File processed!")
    st.write("---")
    st.write("### Preview of extracted text:")
    st.text(text[:500] + "...") # هيعرض أول 500 حرف بس عشان الشاشة متزحمش
