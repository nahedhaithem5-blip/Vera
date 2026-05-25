import streamlit as st
import PyPDF2
from docx import Document

# إعداد الصفحة
st.set_page_config(page_title="Vera - Analysis", page_icon="🔍")
st.title("🔍 Vera: AI Academic Assistant")

# دوال القراءة
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

# رفع الملف
uploaded_file = st.file_uploader("📂 Upload your document", type=['pdf', 'docx'])

if uploaded_file is not None:
    # قراءة الملف
    if uploaded_file.type == "application/pdf":
        text = read_pdf(uploaded_file)
    else:
        text = read_docx(uploaded_file)
    
    st.success("✅ File processed successfully!")
    
    # حساب الإحصائيات
    words = text.split() 
    word_count = len(words)
    unique_words = len(set(words))
    
    # عرض الإحصائيات (Dashboard)
    col1, col2 = st.columns(2)
    col1.metric("Total Words", word_count)
    col2.metric("Unique Words", unique_words)
    
    st.write("---")
    st.write("### 📝 Text Preview:")
    clean_text = text.replace('\n', ' ')
    st.markdown(clean_text[:1000] + "...")
