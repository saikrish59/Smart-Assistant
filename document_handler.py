
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def handle_file_upload(uploaded_file):
    with open(f"/tmp/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.getvalue())
    loader = PyPDFLoader(f"/tmp/{uploaded_file.name}")
    pages = loader.load_and_split()
    return pages
