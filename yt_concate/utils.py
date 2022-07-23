import os

from settings import OUTPUTS_DIR
from settings import DOWNLOADS_DIR
from settings import VIDEOS_DIR
from settings import CAPTIONS_DIR


class Utils:
    def creat_dir(self):
        os.makedirs(OUTPUTS_DIR, exist_ok=True)
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        return 'Make dir success!'

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def check_video_list_file_exists(self, filepath):
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0
