import streamlit as st
import requests

st.title("AI-Powered Q&A System")

# Upload tài liệu
uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt"])
if uploaded_file is not None:
    files = {"file": uploaded_file.getvalue()}
    try:
        response = requests.post("http://localhost:8000/upload/", files=files)
        response.raise_for_status()  # Kiểm tra lỗi HTTP
        st.success(response.json().get("message", "File uploaded successfully!"))
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to upload file: {e}")

# Nhập câu hỏi
question = st.text_input("Enter your question:")
if st.button("Get Answer"):
    if not question.strip():
        st.warning("Please enter a question before clicking 'Get Answer'.")
    else:
        try:
            response = requests.get(f"http://127.0.0.1:8000/ask/?question={question}")
            response.raise_for_status()  # Kiểm tra lỗi HTTP

            st.write("### API Response:")
            st.json(response.json())  # Hiển thị phản hồi JSON đẹp hơn

            answer = response.json().get("answer", "No answer received.")
            st.write("### Answer:")
            st.write(answer)

        except requests.exceptions.RequestException as e:
            st.error(f"API request failed: {e}")
        except ValueError:
            st.error("Failed to parse JSON response from API.")
