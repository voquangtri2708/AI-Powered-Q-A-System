
# **Hệ Thống Hỏi-Đáp Sử Dụng RAG và LLM**  

## **Giới Thiệu**  
Đây là một hệ thống Hỏi-Đáp (Q&A) sử dụng **Retrieval-Augmented Generation (RAG)** kết hợp với mô hình ngôn ngữ lớn (**LLM**).  
Hệ thống cho phép tải lên tài liệu, xử lý văn bản thành **vector embeddings** (FAISS) và tạo câu trả lời bằng **LLM** (Gemini).  



## **Cách Cài Đặt & Chạy Dự Án**  

### **1. Clone Dự Án**  
```sh
git clone https://github.com/voquangtri2708/AI-Powered-Q-A-System.git
cd AI-Powered-Q-A-System
```

### **2. Tạo và Kích Hoạt Môi Trường Ảo**  
```sh
python -m venv venv # Windown
```

### **3. Cài Đặt Dependencies**  
```sh
pip install -r requirements.txt
```

### **4. Cấu Hình Biến Môi Trường**  
Tạo tệp `.env` và thêm API keys:  
```ini
GEMINI_API_KEY=your_gemini_api_key
document=your_document_path
```

### **5. Xử Lý Tài Liệu & Tạo FAISS Index**  
```sh
python document_processing.py
```

### **6. Chạy API Backend**  
#### **Chạy với FastAPI**  
```sh
uvicorn main:app --reload
```

### **7. Chạy Streamlit để sử dụng**  
Nhập câu hỏi liên quan đến tài liệu hoặc up tài liệu khác để có câu trả lời về tài liệu 

```sh
streamlit run app.py
```


## **Liên Hệ**  
📧 Email: voquangtri2708@gmail.com  
🔗 GitHub: [voquangtri2708](https://github.com/voquangtri2708)  

---
