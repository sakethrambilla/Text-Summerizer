from textSummerizer.config.configuration import ConfigurationManager
from textSummerizer.components.data_tranformation import DataTransformation


class DataTransformationTraningPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()
