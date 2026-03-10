from rest_framework import serializers
from .models import Book




# create serializers here

class Bookserializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'  # all fields in the model

# class Loginserializers(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()