from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import shutil
import os

app = FastAPI()

IMAGE_PATH = "latest.jpg"

# Endpoint POST para recibir imagen
@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    
    with open(IMAGE_PATH, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "Imagen recibida"}

# Endpoint GET para recuperar imagen
@app.get("/image")
def get_image():
    
    if os.path.exists(IMAGE_PATH):
        return FileResponse(IMAGE_PATH, media_type="image/jpeg")

    return {"error": "No hay imagen todavía"}