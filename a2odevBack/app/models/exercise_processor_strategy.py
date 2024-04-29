class ExerciseProcessorStrategy:
    def process_exercise(self, json_data):
        raise NotImplementedError("Subclasses must implement the method")
    def read_input_data(self, json_data):
        raise NotImplementedError("Subclasses must implement the method")