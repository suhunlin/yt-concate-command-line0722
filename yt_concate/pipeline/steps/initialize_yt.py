# import os.path
import sys

from .step import Step
# # 當前目錄()
# #/Users/shu-hunglin/Desktop/Python-Project-Practice/Allen-Course/Yt-concate-multi-handler/yt_concate/pipeline/steps
# CURRENT_DIR = os.path.split(os.path.abspath(__file__))[0]
# #當前目錄的上三層目錄
# #/Users/shu-hunglin/Desktop/Python-Project-Practice/Allen-Course/Yt-concate-multi-handler
# config_path = CURRENT_DIR.rsplit('/', 3)[0]
# sys.path.append(config_path)#將上三層目錄的路徑加到sys的path裡面，這樣就能看到Yt-concate-multi-handler目錄下面的所有module
from yt_concate.models.yt import YT #此時就可以用絕對路徑去import

class InitializeYT(Step):
    def process(self, utils, inputs, data):
        pass
        print(CURRENT_DIR)
        print(config_path)
        print(sys.path)
    def process(self, utils, inputs, data):
        return [YT(url) for url in data]