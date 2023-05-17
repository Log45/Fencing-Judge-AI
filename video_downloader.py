from pytube import YouTube
import os

working_dir = os.getcwd()

def Download(link):
    youtubeObject = YouTube(link, use_oauth=True, allow_oauth_cache=False)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path=working_dir+"/yt_downloads")
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)
