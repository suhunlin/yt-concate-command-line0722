from yt_concate.models.yt import YT
class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    @property
    def steps(self):
        return self._steps

    @steps.setter
    def steps(self, steps):
        self._steps = steps

    def run_pipeline(self, utils, inputs):
        data = None

        for step in self.steps:
            data = step.process(utils, inputs, data)
            print(step)
            # print(step, data)
