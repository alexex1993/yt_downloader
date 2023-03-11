import threading
import os
from pytube import Stream
from pytube import YouTube


class YoutubeVideo:
    def __init__(self, url, path):
        self.url = url
        self.yt = YouTube(url=url)
        self.path = path
        self.video_id = self.yt.vid_info["videoDetails"]["videoId"]

    def get_by_itag(self, itag) -> Stream:
        stream = self.yt.streams.get_by_itag(itag)
        return stream

    def get_extension_by_itag(self, itag) -> str:
        mime_type = self.yt.streams.get_by_itag(itag).mime_type
        extension = mime_type.replace("audio/", "").replace("video/", "")
        return extension

    def download_stream(self, itag, filename) -> None:
        print(f"start downloading {itag}")
        self.get_by_itag(itag).download(filename=filename)
        print(f"end downloading {itag}")

    def get_itag_default_stream(self) -> int:
        stream = self.yt.streams.get_highest_resolution()
        return stream.itag

    def download_video_and_audio(self, itag_video=None, itag_audio=None):
        if itag_video is None and itag_audio is None:
            itag_video = self.get_itag_default_stream()

        def download_stream(itag):
            extension = self.get_extension_by_itag(itag)
            full_filename = os.path.join(self.path, f"{self.video_id}___{itag}.{extension}")
            self.download_stream(itag, f"{full_filename}")

        if itag_video:
            video_thread = threading.Thread(target=download_stream, args=(itag_video,))
            video_thread.start()
        if itag_audio:
            audio_thread = threading.Thread(target=download_stream, args=(itag_audio,))
            audio_thread.start()

    def print_all_codecs(self):
        for i in self.yt.streams:
            if i.type == "video":
                format = f"{i.itag} : {i.type} : {i.mime_type.replace('video/','')}@{i.resolution}@{i.fps}fps@{i.video_codec}@{i.audio_codec}"
                print(format)
            if i.type == "audio":
                format = f"{i.itag} : {i.type} : {i.mime_type.replace('audio/', '')}@{i.abr}@{i.audio_codec}"
                print(format)