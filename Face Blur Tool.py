import cv2
import tkinter as tk
from tkinter import filedialog

def blur_faces(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        face = image[y:y+h, x:x+w]
        face = cv2.GaussianBlur(face, (99, 99), 30)
        image[y:y+h, x:x+w] = face

    output_path = image_path.replace(".", "-blurred.")
    cv2.imwrite(output_path, image)
    
    cv2.imshow("Blurred Faces", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        blur_faces(file_path)

#GUI setup 

root = tk.Tk()
root.title("Face Blur Tool")
root.geometry("300x200")

select_button = tk.Button(root, text="Select Image", command=open_file)
select_button.pack(pady=20)

root.mainloop()