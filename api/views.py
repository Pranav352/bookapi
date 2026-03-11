from rest_framework import viewsets , response, request
from api.models import Book
from.Serializer import Bookserializer,Loginserializers 
from.Serializer import serializers
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response 


# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Bookserializer
    permission_classes = [IsAuthenticated]
    

    def update(self, request, *args, **kwargs):
        print(" Custom update method")
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        print(" Custom delete method called")
        return super().destroy(request, *args, **kwargs)
    
#JWT token 
    
class LoginApi(APIView):
    def post(self, request):
        serializer = Loginserializers(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=401)
        
        # Check if user is admin
        if not user.is_staff:
            return Response({'error': 'Only admin users can access this endpoint'}, status=403)
        
        # Create or get token
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username,
            'message': 'Login successful'
        })

    
