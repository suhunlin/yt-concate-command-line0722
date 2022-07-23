from .step import Step


class Preflight(Step):
    def process(self, utils, inputs, data):
        return utils.creat_dir()