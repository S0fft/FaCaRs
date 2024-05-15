# import io
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer

from rest_framework import serializers

from cars.models import Car


class CarSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.category_id = validated_data.get("category_id", instance.category_id)
        instance.save()

        return instance


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
