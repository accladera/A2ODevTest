from app.models.exercise_processor_strategy import ExerciseProcessorStrategy
from app.models.strings import StringSubstrings


class StringProblem(ExerciseProcessorStrategy):
    def process_exercise(self, input_data):
        t = self.read_input_data(input_data)
        stringSubstring = StringSubstrings()
        return 0

    def read_input_data(self, input_data):
        t = str(input_data)
        if t.isupper():
            raise ValueError('String must be in lower case')
        return t
