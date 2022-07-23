from yt_concate.models.found import Found
from .step import Step


class Search(Step):
    def process(self, utils, inputs, data):
        found = []
        search_word = inputs['search_word']

        for yt in data:
            if not yt.check_caption_file_exists():
                continue
            captions = yt.captions
            for caption in yt.captions:
                if search_word in caption:
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    found.append(f)
        for obj in found:
            print(obj.yt, obj.caption, obj.time)
        return found
