import tkinter as tk
from tkinter import filedialog
import cv2
import os


def TTCut(file_path):
    cap = cv2.VideoCapture(file_path)

    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    end_time = frames / fps - 4

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(f"{os.path.splitext(file_path)[0]}-output.mp4", fourcc, fps, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    cap.set(cv2.CAP_PROP_POS_MSEC, 0)

    while cap.get(cv2.CAP_PROP_POS_MSEC) <= end_time * 1000:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

def select_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("MP4 files", "*.mp4")])

    for file_path in file_paths:
        TTCut(file_path)

root = tk.Tk()
root.title("Video Cutter")

select_button = tk.Button(root, text="Select Files", command=select_files)
select_button.pack(padx=20, pady=20)

root.mainloop()
