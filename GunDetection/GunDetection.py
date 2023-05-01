from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import tkinter as tk
from tkinter import filedialog, messagebox

model = YOLO ("model/gundetection.pt")
classNames = ['AK47', 'Pistol']

def video_image_function():
    file_path = filedialog.askopenfilename(title="Select a video or image file to do detection",
                                       filetypes=(("video files", "*.mp4;*.avi;*.mov"), ("image files", "*.jpg;*.jpeg;*.png")))

    if file_path:

    # model prediction
        model.predict (source = file_path, 
                        show=True, 
                        save=True, 
                        hide_labels=False, 
                        hide_conf=False, 
                        conf=0.5, 
                        save_txt=False, 
                        save_crop=False, 
                        line_thickness=2)

    else:
        messagebox.showwarning("Warning", "No file selected!")
 
#main window
root = tk.Tk()
root.title("Select an Option for detection")
root.geometry("400x200")  
root.resizable(False, False)

#label in the window
label = tk.Label(root, text="Click the button to select file:", font=("Arial", 16))
label.pack(pady=10)

#buttons
video_button = tk.Button(root, text="Select Video or Image", command=video_image_function, width=10, height=2, font=("Arial", 10), wraplength=80)
video_button.pack()

root.mainloop()
