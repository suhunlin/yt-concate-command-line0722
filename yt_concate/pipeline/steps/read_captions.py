import time
from .step import Step

from yt_concate.multi_handler.yt_multi_threading import YTMultithreading
from yt_concate.multi_handler.yt_multi_processing import YTMultiProcessing


class ReadCaptions(Step):
    def process(self, utils, inputs, data):
        start_time = time.time()
        # single process
        # self.read_captions(data)
        # multi-threading
        multi_thread = YTMultithreading()
        multi_thread.run_multi_threading(self.read_captions_multi_handler, data, inputs)
        # multi_processing
        # ***Can't use multi-processing to handle data because the memory add is different***
        # multi_process = YTMultiProcessing()
        # multi_process.run_multi_processing(self.read_captions_multi_handler, data, inputs)
        end_time = time.time()
        print('Read captions cost time:', end_time - start_time)
        # for yt in data:
        #     print(yt.captions)
        return data

    def read_captions(self, data):
        for yt in data:
            if not yt.check_caption_file_exists():
                # print(yt.caption_id + '.txt file not exists!')
                continue
            captions = {}
            time_line = False
            with open(yt.caption_filepath, 'r') as f:
                for line in f:
                    if '-->' in line:
                        time_line = True
                        time = line.strip()
                        continue
                    if time_line:
                        time_line = False
                        caption = line.strip()
                        captions[caption] = time
                yt.captions = captions

    def read_captions_multi_handler(self, *args, **kwargs):
        for yt in args:
            if not yt.check_caption_file_exists():
                # print(yt.caption_id + '.txt file not exists!')
                continue
            captions = {}
            time_line = False
            with open(yt.caption_filepath, 'r') as f:
                for line in f:
                    if '-->' in line:
                        time_line = True
                        time = line.strip()
                        continue
                    if time_line:
                        time_line = False
                        caption = line.strip()
                        captions[caption] = time
                yt.captions = captions
