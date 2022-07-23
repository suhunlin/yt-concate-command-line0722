import time
from pytube import YouTube

from .step import Step
from yt_concate.multi_handler.yt_multi_threading import YTMultithreading
from yt_concate.multi_handler.yt_multi_processing import YTMultiProcessing

class DownloadVideos(Step):
    def process(self, utils, inputs, data):
        start_time = time.time()
        #single handler
        # self.download_video(data)
        #multi-threading
        # multi_thread = YTMultithreading()
        # multi_thread.run_multi_threading(self.download_video_multi_handler, data, inputs)
        #multi-processing
        multi_process = YTMultiProcessing()
        multi_process.run_multi_processing(self.download_video_multi_handler, data, inputs)
        end_time = time.time()
        print('Download Videos cost time:', end_time - start_time)

    def download_video(self, data):
        yt_set = set([found.yt for found in data])
        for yt in yt_set:
            if yt.check_video_file_exists():
                continue
            print(yt.url, 'downloading......')
            YouTube(yt.url).streams.first().download(output_path=yt.video_filepath, filename=yt.caption_id + '.mp4')

    def download_video_multi_handler(self, *args, **kwargs):
        yt_set = set([found.yt for found in args])
        for yt in yt_set:
            if not yt.check_caption_file_exists():
                continue
            print(yt.url, 'downloading......')
            YouTube(yt.url).streams.first().download(output_path=yt.video_filepath, filename=yt.caption_id + '.mp4')
