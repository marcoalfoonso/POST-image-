import cv2
import requests

# URL del endpoint POST
url = "https://post-image-j0l5.onrender.com"

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se pudo abrir la cámara")
    exit()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Guardar frame temporal
    cv2.imwrite("frame.jpg", frame)

    # Enviar imagen
    with open("frame.jpg", "rb") as f:
        files = {"file": ("frame.jpg", f, "image/jpeg")}
        response = requests.post(url, files=files)

    print(response.status_code)

    # Mostrar video local
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()