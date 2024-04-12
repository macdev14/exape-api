from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from apps.api.serializers import QuoteSerializer, UserSerializer, CustomTokenSerializer
from apps.authentication.models import Quote, User
# Create your views here.
# ViewSets define the view behavior.
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status

class ApiViewSet(viewsets.ModelViewSet): 
    pass

class UserViewSet(ApiViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return User.objects.filter()

class ProcessViewSet(viewsets.ViewSet):
    
    def create(self, request):
        
        data = request.data
        
        cotacao = data.get('cotacao')
        quote_exists = Quote.objects.filter(pk=cotacao).exists()
        
        if not quote_exists:
            return Response("Quote not found", status=status.HTTP_400_BAD_REQUEST)
        quote = Quote.objects.get(pk=cotacao)
        result = quote.item_value/quote.installments
        
        result = "{:.2f}".format(result)
        return Response({"result": result})
        



class QuoteViewSet(viewsets.ViewSet):
    serializer_class = QuoteSerializer
    permission_classes = [IsAuthenticated]
   
    def list(self, request, qt_id=None):
        queryset = Quote.objects.all()
        serializer = QuoteSerializer(queryset, many=True)
        qt_id = request.query_params.get('qt_id')
        if qt_id:
            queryset = Quote.objects.filter(pk=qt_id).first()
            serializer = QuoteSerializer(queryset)
        print('list called')
        return Response(serializer.data)

    def retrieve(self, request, pk=None,qt_id=None):
        if pk:
            user = get_object_or_404(User, pk=pk)
            queryset = Quote.objects.filter(user=user)
            serializer = QuoteSerializer(queryset, many=True)
        elif qt_id:
            queryset = Quote.objects.get(qt_id)
            serializer = QuoteSerializer(queryset, many=True)
        print('retrieve called')
        return Response(serializer.data)

    def create(self, request):
        serializer = QuoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer

