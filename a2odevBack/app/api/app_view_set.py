from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from app.models import ExersiceChess, StringProblem


class AppViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'], name='Processing the problem exercise.')
    def process(self, request):
        data = request.data.get('data')
        problem_index = data.get('index')
        string_input = data.get('input')

        if not problem_index:
            #return Response({"error": "Missing problem index."}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": data}, status=status.HTTP_400_BAD_REQUEST)
        if not string_input:
            return Response({"error": "Missing parameters."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            strategy = self.get_exercise_processor(int(problem_index))
            output = strategy.process_exercise(string_input)
            return Response({"data": output})

        except Exception as e:
            return Response({"error":  str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_exercise_processor(self, index):
        if index == 1:
            return ExersiceChess()
        elif index == 2:
            return StringProblem()
        else:
            raise ValueError("Invalid value for index")


