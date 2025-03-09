import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings# Có thể thay bằng embedding khác nếu cần
from dotenv import load_dotenv

# Load biến môi trường từ .env
load_dotenv()

# API Key của Gemini (Google AI)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Missing Gemini API Key. Set GEMINI_API_KEY in environment variables.")


# Load FAISS index với Google Generative AI embeddings
def load_faiss_index(index_path="vector_store"):
    if not os.path.exists(index_path):
        raise FileNotFoundError(f"FAISS index not found at '{index_path}'. Run document processing first.")

    # Lấy API key từ biến môi trường
    load_dotenv()
    google_api_key = os.getenv("GEMINI_API_KEY")
    if google_api_key is None:
        raise ValueError("Missing Google API Key! Set GOOGLE_API_KEY in environment variables.")

    # Sử dụng Google Generative AI Embeddings (GenMini)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GEMINI_API_KEY)

    return FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

# Truy vấn và sinh câu trả lời bằng Gemini
def generate_answer(question, k=3):
    try:
        vectorstore = load_faiss_index()
        docs = vectorstore.similarity_search(question, k=k)

        if not docs:
            return "No relevant information found."

        context = "\n".join([doc.page_content for doc in docs])

        # llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GEMINI_API_KEY)
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=GEMINI_API_KEY, api_version="v1")

        prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
        response = llm.invoke(prompt)

        return response.content.strip()

    except Exception as e:
        return f"Error generating answer: {str(e)}"

if __name__ == "__main__":
    question = "Hệ thống RAG hoạt động như thế nào?"
    print(generate_answer(question))
