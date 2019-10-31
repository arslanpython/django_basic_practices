from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Stock
from .serializer import StockSerializer


class StockList(APIView):

    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        data = serializer.data
        print('---->', data)
        return Response(data)

    def post(self, request):
        pass
