import time
from pytube import YouTube

from yt_concate.multi_handler.yt_multi_processing import YTMultiProcessing
from yt_concate.multi_handler.yt_multi_threading import YTMultithreading
from .step import Step


class DownloadCaptioins(Step):
    def process(self, utils, inputs, data):
        start_time = time.time()
        # single-thread
        # self.download_caption(data)
        # multi-threading
        multi_thread = YTMultithreading()
        multi_thread.run_multi_threading(self.download_caption_multi_handler, data, inputs)
        # multi_processing
        # multi_process = YTMultiProcessing()
        # multi_process.run_multi_processing(self.download_caption_multi_handler, data, inputs)
        end_time = time.time()
        print('Download captions cost time:', end_time - start_time)
        return data

    def download_caption(self, data):
        for yt in data:
            if yt.check_caption_file_exists():
                # print(yt.caption_id + '.txt file exists!')
                continue
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (AttributeError, KeyError) as e:
                print(e)
                continue
            text_file = open(yt.caption_filepath, "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

    def download_caption_multi_handler(self, *args, **kwargs):
        for yt in args:
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (AttributeError, KeyError) as e:
                print(e)
                continue
            text_file = open(yt.caption_filepath, "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
