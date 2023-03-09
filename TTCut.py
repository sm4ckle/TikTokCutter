import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    if file_path:
        process_file(file_path)

def process_file(file_path):
    input_path = os.path.abspath(file_path)
    output_path = os.path.splitext(input_path)[0] + "-output.mp4"
    duration = get_video_duration(input_path)
    command = f"ffmpeg -hide_banner -y -i {input_path} -vcodec h264_nvenc -ss 0 -to {duration-4.1} -copyts {output_path}"
    subprocess.call(command, shell=True)
    tk.messagebox.showinfo(title="Video Processing", message="Processing complete!")

def get_video_duration(file_path):
    command = f"ffprobe -i {file_path} -show_entries format=duration -v quiet -of csv=\"p=0\""
    output = subprocess.check_output(command, shell=True)
    return float(output)

root = tk.Tk()
root.eval('tk::PlaceWindow . center')
root.title("TikTok Cutter")
root.geometry("200x100")
label = tk.Label(root, text="Select a TikTok MP4 file:")
label.pack(pady=10)
button = tk.Button(root, text="Browse", command=select_file)
button.pack(pady=10)
root.mainloop()
