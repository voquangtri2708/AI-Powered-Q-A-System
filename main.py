from fastapi import FastAPI, UploadFile, File, HTTPException
import os
import shutil
from query_processing import generate_answer
from document_processing import create_faiss_index, load_documents

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Đảm bảo thư mục tồn tại

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        
        # Lưu file vào thư mục uploads
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Xử lý tài liệu và cập nhật FAISS
        docs = load_documents(file_path)
        if not docs:
            raise HTTPException(status_code=400, detail="No text extracted from document.")

        create_faiss_index(docs)

        return {"message": f"File '{file.filename}' processed successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File processing failed: {str(e)}")

@app.get("/ask/")
async def ask_question(question: str):
    if not question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")

    try:
        answer = generate_answer(question)
        return {"question": question, "answer": answer}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate answer: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
