from tkinter import *
from tkinter import Entry, StringVar, ttk
from tkinter import filedialog
import ttkbootstrap as tk
from pytube import YouTube

window = tk.Window()
window.iconbitmap('Icon.ico')
window.title('Video Downloader')
user_input = tk.StringVar(window)
folder_path: StringVar = StringVar()
global filename


def on_progress(stream, total_size, bytes_remaining):
    # the total size of the video
    total_size = stream.filesize

    # function to get the size of the video
    def get_formatted_size(total_file_size, factor=1024, suffix='B'):
        # looping through the units
        for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
            if total_file_size < factor:
                return f"{total_file_size:.2f}{unit}{suffix}"
            total_file_size /= factor
        # the formatted video size
        return f"{total_file_size:.2f}Y{suffix}"

    # the formatted video size call the function
    formatted_size = get_formatted_size(total_size)
    # size downloaded after the start
    bytes_downloaded = total_size - bytes_remaining
    # percentage downloaded after the start
    percentage_completed = round(bytes_downloaded / total_size * 100)
    # updating the progress bar value
    progress_bar['value'] = percentage_completed
    # updating the empty label with the percentage value
    progress_label.config(text=str(percentage_completed) + '%  of:' + formatted_size)
    # updating the main window of the app
    window.update()


def browse_button():
    global folder_path
    global filename
    filename = filedialog.askdirectory()
    folder_path.set(filename)


def get_url():
    print((user_input.get()))  # calling get() here!
    # paste the YouTube video URL here
    url = (user_input.get())
    # set the download path and download the video
    yt = YouTube(url)
    print('The video name and size : ', yt.streams.get_highest_resolution().filesize_mb, 'Mb')
    yt = YouTube(url, on_progress_callback=on_progress)
    yt.streams.get_highest_resolution().download(filename)
    Label(window, width=20, text='Download Finished', bg='green').grid(row=5, column=0)


# grid() = geometry manager that organizes widgets in a table-like structure in a parent widget


titleLabel = Label(window, text="Youtube Video Downloader", font=("Arial bold", 20))
titleLabel.grid(row=0, column=0, columnspan=2)

Path_button = Button(window, text="Path location", width=20, command=browse_button)
Path_button.grid(row=1, column=0)
PathEntry = Entry(window, width=50, textvariable=folder_path)
PathEntry.grid(row=1, column=1)

linkLabel = Label(window, text="Past Video Link: ", bg='green')
linkLabel.grid()
linkEntry = Entry(window, width=50, textvariable=user_input)
linkEntry.grid(row=2, column=1)

downloadButton = Button(window, text="Download", bg='Blue', width=20, command=get_url)
downloadButton.grid(row=4, column=0)

# creating a progress bar to display progress
progress_bar = ttk.Progressbar(window, orient=HORIZONTAL, length=450, mode='determinate')
progress_bar.grid(row=4, column=1)

# creating the empty label for displaying download progress
progress_label = Label(window, text='')
# adding the label to the window
progress_label.grid(row=5, column=1)

window.mainloop()
