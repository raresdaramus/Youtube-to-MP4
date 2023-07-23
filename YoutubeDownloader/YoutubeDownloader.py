import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

def download_video():
    url = url_entry.get()
    output_path = filedialog.askdirectory()

    if url:
        try:
            yt = YouTube(url)
            yDownload = yt.streams.get_highest_resolution()

            message_label.config(text="Downloading video...")
            yDownload.download(output_path)
            message_label.config(text="Video downloaded successfully.")

        except Exception as e:
            message_label.config(text=f"An error occurred: {e}")

    else:
        message_label.config(text="Please provide a URL.")

# Create the main window
window = tk.Tk()
window.title("YouTube Video Downloader")

# Create widgets
url_label = tk.Label(window, text="Enter the YouTube video URL:")
url_label.pack()

url_entry = tk.Entry(window, width=50)
url_entry.pack()

download_button = tk.Button(window, text="Download Video", command=download_video)
download_button.pack()

message_label = tk.Label(window, text="")
message_label.pack()

# Run the main event loop
window.mainloop()
