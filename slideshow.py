import tkinter as tk
import time
from PIL import Image, ImageTk

root=tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("900x900")

image_paths=[
    r"C:/Users/Personal/Pictures/Camera Roll/WIN_20260223_22_49_50_Pro.jpg",
    r"C:/Users/Personal/Pictures/Camera Roll/WIN_20260223_22_50_02_Pro.jpg",
    r"C:/Users/Personal/Pictures/Camera Roll/WIN_20260227_09_52_53_Pro.jpg",
    r"C:/Users/Personal/Pictures/Camera Roll/WIN_20260227_09_53_00_Pro.jpg",
    r"C:/Users/Personal/Pictures/Camera Roll/WIN_20260227_09_53_08_Pro.jpg",
    r"C:/Users/Personal/Pictures/Camera Roll/WIN_20260223_20_25_25_Pro.jpg"
]

image_size=(700,700)
images=[]
for path in image_paths:
    img= Image.open(path)
    img= img.resize(image_size)
    images.append(img)

final_images=[]
for img in images:
    photo= ImageTk.PhotoImage(img)
    final_images.append(photo)

image_label=tk.Label(root)
image_label.pack(pady=30)

def start_slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image=photo
        root.update()
        time.sleep(2)

play_button=tk.Button(
    root,
    text="Play the Slideshow",
    font=("Arial",17),
    command=start_slideshow
)

play_button.pack(pady=40)

root.mainloop()
