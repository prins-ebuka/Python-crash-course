from pytube import YouTube

DOWNLOAD_FOLDER = "/home/ecihekwereme/Downloads"

video_url = "https://www.youtube.com/watch?v=ujlgCQjjC8s&list=PL9eF5phFMwVDEGHMg7fTIGCtrzaA3aFxB&index=29"

video_obj = YouTube(video_url)

stream = video_obj.streams.get_highest_resolution()

stream.download(DOWNLOAD_FOLDER)