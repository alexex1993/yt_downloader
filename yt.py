#from pytube import YouTube
#from pytube.cli import on_progress #this module contains the built in progress bar.
from YoutubeVideo import YoutubeVideo

video = YoutubeVideo(url="https://www.youtube.com/watch?v=LXb3EKWsInQ")


video.download_stream(699, "kek.mp4")



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
