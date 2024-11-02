import streamlit as st
import codecs

# Set page configuration
st.set_page_config(page_title="Shubham Yadav - Portfolio", layout="wide")

# Load the HTML content
def load_html(file_path):
    with codecs.open(file_path, 'r', 'utf-8') as f:
        html_content = f.read()
    return html_content

# Display HTML content
html_file_path = "index.html"
html_content = load_html(html_file_path)
st.markdown(html_content, unsafe_allow_html=True)

# Link to CSS
st.markdown("<style>{}</style>".format(open("styles.css").read()), unsafe_allow_html=True)
