from pytube import Stream
from pytube import YouTube


class YoutubeVideo:
    url = ""
    yt = None

    def __init__(self, url):
        self.url = url
        self.yt = YouTube(url=url)

    def get_dict_stream(self, type_content):
        dict_stream = {}
        for i in self.yt.streams:
            if i.type == type_content:
                dict_stream[i.itag] = i
        return dict_stream

    def get_dict_video_stream(self):
        dict_stream = self.get_dict_stream(type_content="video")
        return dict_stream

    def get_dict_audio_stream(self):
        dict_stream = self.get_dict_stream(type_content="audio")
        return dict_stream

    def get_by_itag(self, itag) -> Stream:
        stream = self.yt.streams.get_by_itag(itag)
        return stream

    def download_stream(self, itag, filename):
        self.get_by_itag(itag).download(filename=filename)