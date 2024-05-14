import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


class CarSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_upadate = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()


# class CarModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# def encode():
#     model = CarModel('KIA', 'Ceed')
#     model_sr = CarSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)


# def decode():
#     stream = io.BytesIO(b'{"title": "KIA", "content": "Ceed"}')
#     data = JSONParser().parse(stream)
#     serializer = CarSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data, type(serializer.validated_data), sep='\n')
