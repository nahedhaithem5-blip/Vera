import streamlit as st
import PyPDF2
from docx import Document

st.set_page_config(page_title="Vera - Smart Analyzer", page_icon="🔍")
st.title("🔍 Vera: Universal AI Analyzer")

# دالة القراءة الموحدة
def extract_text(file):
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        return " ".join([page.extract_text() for page in reader.pages])
    else:
        doc = Document(file)
        return " ".join([p.text for p in doc.paragraphs])

# Sidebar للاختيار الذكي
analysis_type = st.sidebar.selectbox("Select Document Type:", 
                                     ["Academic Research", "Creative Writing", "General Report"])

uploaded_file = st.file_uploader("Upload any document (PDF/Docx)", type=['pdf', 'docx'])

if uploaded_file is not None:
    text = extract_text(uploaded_file)
    words = text.split()
    
    # Dashboard الإحصائيات
    col1, col2 = st.columns(2)
    col1.metric("Word Count", len(words))
    col2.metric("Vocabulary Richness", f"{len(set(words))/len(words):.2%}")
    
    st.write("---")
    
    # "عقل" Vera الذكي
    if analysis_type == "Academic Research":
        st.subheader("🎓 Academic Insights")
        st.info("Analyzing for: Formal tone, Clarity, and Structure.")
        # هنا هنضيف مستقبلاً كود فحص الاقتباس
        
    elif analysis_type == "Creative Writing":
        st.subheader("🎨 Creative Insights")
        st.info("Analyzing for: Descriptive language, Emotion, and Flow.")
        
    else:
        st.subheader("📊 Report Insights")
        st.info("Analyzing for: Conciseness and Key Facts.")

    st.write("### Text Preview:")
    st.markdown(text[:1000] + "...")
