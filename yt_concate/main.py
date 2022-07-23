import os
import sys

CURRENT_DIR = os.path.split(os.path.abspath(__file__))[0]
config_path = CURRENT_DIR.rsplit('/', 1)[0]
sys.path.append(config_path)

from command_line_handler import CommandLineHandler
from utils import Utils
from pipeline.pipeline import Pipeline
from pipeline.steps.preflight import Preflight
from pipeline.steps.get_video_list import GetVideoList
from pipeline.steps.initialize_yt import InitializeYT
from pipeline.steps.download_captions import DownloadCaptioins
from pipeline.steps.read_captions import ReadCaptions
from pipeline.steps.search import Search
from pipeline.steps.download_videos import DownloadVideos


def main():
    print(config_path)

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptioins(),
        ReadCaptions(),
        Search(),
        DownloadVideos(),

    ]

    inputs = {
        'channel_id': 'UCKSVUHI9rbbkXhvAXK-2uxA',
        'search_word': 'incredible',
        'limit': 20

    }
    clh = CommandLineHandler()
    print('default user input:', inputs)
    inputs.update(clh.run_command_line_opt_parser())
    print('update user input:', inputs)
    inputs.update()
    utils = Utils()
    p1 = Pipeline(steps)
    p1.run_pipeline(utils, inputs)


if __name__ == '__main__':
    main()
