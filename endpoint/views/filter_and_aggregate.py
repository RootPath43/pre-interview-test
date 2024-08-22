from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from endpoint.calculations.calculations import Calculation


class FilterAndAggregateView(APIView):

    def get(self, request, *args, **kwargs):

        calculation_instance = Calculation()  # singleton object call

        data = calculation_instance.filter_and_aggregate()

        return Response(data, status=status.HTTP_200_OK)
