import os
import faiss
import numpy as np
from langchain.document_loaders import PyMuPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv

# Đọc API key từ biến môi trường
load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
document_path = os.getenv("document")
print("google api key: ",GOOGLE_API_KEY)
if not GOOGLE_API_KEY:
    raise ValueError("Vui lòng thiết lập GOOGLE_API_KEY trước khi chạy script.")

# Load tài liệu PDF
def load_documents(file_path):
    loader = PyMuPDFLoader(file_path)
    docs = loader.load()
    return [doc.page_content for doc in docs]

# Tạo vector embeddings với Gemini và lưu vào FAISS
def create_faiss_index(docs, index_path="vector_store"):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",  google_api_key=GOOGLE_API_KEY)
    vectorstore = FAISS.from_texts(docs, embeddings)
    vectorstore.save_local(index_path)

if __name__ == "__main__":
    file_path = document_path
    docs = load_documents(file_path)
    create_faiss_index(docs)
    print("Documents indexed successfully!")
