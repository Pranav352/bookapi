from rest_framework import viewsets
from api.models import Book
from.Serializer import Bookserializer



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
    


