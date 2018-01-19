from runModel import run_model

import unittest
import pickle
import os

test_input_path = "tests/inputs/{0}"
test_output_path = "tests/outputs/{0}"


class BaseTest(unittest.TestCase):
    """ base to other tests """

    def __init__(self):
        super(BaseTest, self).__init__()
        self.model_id = None
        self.input_file_path = None
        self.output_file_path = None

    def run_model(self):
        """ run model and return dict """
        run_model(self.model_id, self.input_file_path, self.output_file_path)

        # check file
        with open(self.output_file_path, mode='rb') as data_file:
            input_dict = pickle.load(data_file)
            # global properties given by user or previous model
            model_input = input_dict["input"]
            # output of previous models
            model_output = input_dict["output"]

        return model_input, model_output

    def delete_output_file(self):
        """ delete file """
        if os.path.exists(self.output_file_path):
            os.remove(self.output_file_path)


class TestSpeedModel(BaseTest):
    """  run speed model """

    def __init__(self):
        super(TestSpeedModel, self).__init__()
        self.model_id = 'S'
        self.input_file_path = test_input_path.format("speed.model_input")
        self.output_file_path = test_output_path.format("speed.model_output")

    def test_run(self):
        """ validate output dict """
        _, model_output = self.run_model()

        # check dict answer here

        self.delete_output_file()


class TestForceModel(BaseTest):
    """  run force model """

    def __init__(self):
        super(TestForceModel, self).__init__()
        self.model_id = 'F'
        self.input_file_path = test_input_path.format("force.model_input")
        self.output_file_path = test_output_path.format("force.model_output")

    def test_run(self):
        """ validate output dict """
        _, model_output = self.run_model()

        # check dict answer here

        self.delete_output_file()


class TestEnergyModel(BaseTest):
    """  run energy model """

    def __init__(self):
        super(TestEnergyModel, self).__init__()
        self.model_id = 'E'
        self.input_file_path = test_input_path.format("energy.model_input")
        self.output_file_path = test_output_path.format("energy.model_output")

    def test_run(self):
        """ validate output dict """
        _, model_output = self.run_model()

        # check dict answer here

        self.delete_output_file()


class TestThermalModel(BaseTest):
    """  run thermal model """

    def __init__(self):
        super(TestThermalModel, self).__init__()
        self.model_id = 'T'
        self.input_file_path = test_input_path.format("heat.model_input")
        self.output_file_path = test_output_path.format("heat.model_output")

    def test_run(self):
        """ validate output dict """
        _, model_output = self.run_model()

        # check dict answer here

        self.delete_output_file()


if __name__ == '__main__':
    unittest.main()
