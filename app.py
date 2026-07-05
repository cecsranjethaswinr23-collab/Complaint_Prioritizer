import re
import joblib  # or pickle / torch depending on your file type
import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Compliant Prioritizer",
    page_icon="🎫",
    layout="centered"
)

# ABOUt sidebar
st.sidebar.title("About")
# sidebar markdown 1
st.sidebar.markdown("""
### 🎯 WHAT IT DOES:
This is a Machine Learning application recognizes seven categories of the Banking Complaints of the 
customers using Natural Language Processing ,ML model and Transformers, it recognizes the problem faced by the consumer
by looking at the compliant and categorize it and it finds the emotion and severity of the problem
based on the context of the compliant. By evaluating the category, emotions and severity of the problem 
in the consumer's complaint we can prioritize the complaint ticket and resolve the problem for the consumers, which shows the 
reliablity of the services provided and helps in customer retention for the banks.
""")
# sidebar markdown 2
st.sidebar.markdown("""
#### 🫠 WHAT IT IS TRAINED ON:
This model specifically trained on Seven categories of complaint tickets like Banking Services, Credit Card, Consumer Loan, 
Credit Reporting, Debt collection, Mortgage and Student Loan 

""")
st.sidebar.subheader("🛠️ Tech Stack")
tech_stack = [
    "Python",
    "Pandas",
    "Scikit-Learn",
    "Spacy",
    "Transformers",
    "Streamlit",
]
for tech in tech_stack:
    st.sidebar.markdown(f"- **{tech}**")

st.sidebar.subheader("🔗 Source Code")
st.sidebar.link_button("💻 Go to GitHub Repository", "https://github.com/cecsranjethaswinr23-collab/Complaint_Prioritizer_NLP", use_container_width=True)

st.sidebar.markdown("### 👨‍💻 Developed By")
st.sidebar.markdown("**Ranjeth Aswin Ravindran**")
st.sidebar.caption("Data Scientist")

# Email bar
st.sidebar.markdown("""
📧 **Contact:** cecsranjethaswinr23@gmail.com
""")

st.title("Complaint Prioritizer 🎫")
st.markdown(""" The application recognizes the severity of your problem and categorize it. The complaints with high risk for the consumers
will be recognized by the application and prioritize the tickets for immediate resolving of the problem for better consumer services...
""")

st.write("---")