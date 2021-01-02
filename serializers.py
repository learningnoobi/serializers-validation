from rest_framework import serializers
from .models import Anime


class AnimeSerializer(serializers.ModelSerializer):
    def start_r(value):
        if value[0].lower() == 'x':
            raise serializers.ValidationError("there is no name from x in Nepal")
    name = serializers.CharField(validators=[start_r])

    class Meta:
        model = Anime
        fields = ('id', 'name', 'age', 'address')

    def validate_name(self, value):
        if value.lower() == "rayon": 
            raise serializers.ValidationError("That is god's name boy.Don't you dare use that name !") 
        return value

    def validate_age(self, value):
        if value < 18: 
            raise serializers.ValidationError("Not for minor .") 
        return value

    def validate(self,data):
        nm = data.get('name')
        age = data.get('age')
        if nm.lower() == 'rayon' or age <18:
            raise serializers.ValidationError("wrong choice")
        return data
