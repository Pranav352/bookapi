from rest_framework import viewsets , response
from api.models import Book
from.Serializer import Bookserializer #Loginserializers, 
from.Serializer import serializers



# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Bookserializer
    

    def update(self, request, *args, **kwargs):
        print(" Custom update method")
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        print(" Custom delete method called")
        return super().destroy(request, *args, **kwargs)
    
# class LoginApi(viewsets):
#     def POST(self, request):
        
#         data = request.data()
#         print(data)
#         return response({ 
#             "status": True,
#             "data": serializers.data
            
#             })

    


