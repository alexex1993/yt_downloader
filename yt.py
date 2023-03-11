import threading
from YoutubeVideo import YoutubeVideo
from pytube import YouTube
from time import sleep
import os

video = YoutubeVideo(url="https://www.youtube.com/watch?v=kRxPpl_85gc", path="/var/www/html/downloads")
#video.print_all_codecs()
video.download_video_and_audio()
#print(video.get_itag_default_stream())


#print(os.path.join("/home/alexex/Down", f"file.txt"))


#yt = YouTube(url="https://www.youtube.com/watch?v=kRxPpl_85gc")
#s = yt.streams.get_by_itag(22).mime_type
#print(s.replace("audio/", "").replace("video/", ""))

#video.print_all_codecs()


#yt = YouTube("https://www.youtube.com/watch?v=LXb3EKWsInQ")

#dict_stream = {}

#for i in yt.streams:
#    if i.type == "video":
#        dict_stream[i.itag] = i
#        print(i)
#        #format = f"{i.mime_type.replace('video/','')}@{i.resolution}@{i.fps}@{i.video_codec}@{i.audio_codec}"
#        print(i.audio_codec)



#print(dict_stream)

#yt.streams.get_by_itag(699).download(filename="kek.mp4")

#yt.streams.filter(progressive=False).order_by('resolution').desc().first().download()
#YouTube("https://www.youtube.com/watch?v=LXb3EKWsInQ").streams.get_highest_resolution().download()
