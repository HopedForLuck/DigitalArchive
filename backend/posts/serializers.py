import datetime

from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from users.serializers import CustomUserSerializer
from .models import (
    Post, Comment, Tag,
    Continent, Region, Country, Area, City,
)


class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = ['id', 'name']


class RegionSerializer(serializers.ModelSerializer):
    continent = ContinentSerializer(read_only=True)

    class Meta:
        model = Region
        fields = ['id', 'name', 'continent']


class CountrySerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'region']


class AreaSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Area
        fields = ['id', 'name', 'country']


class CitySerializer(serializers.ModelSerializer):
    area = AreaSerializer(read_only=True)

    class Meta:
        model = City
        fields = ['id', 'name', 'area']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']


class CommentSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    continent = ContinentSerializer(read_only=True)
    country = CountrySerializer(read_only=True)
    region = RegionSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    photo = Base64ImageField()

    def validate(self, data):
        self.validate_location(data)
        if data.get('is_date_unknown'):
            return data
        self.validate_date(data)
        return data

    def validate_location(self, data):
        if data.get('is_location_unknown'):
            if any([data.get('continent'), data.get('country'), data.get('region'), data.get('city')]):
                raise serializers.ValidationError(
                    "Не должно быть указано местоположение, если выбрано 'Место съемки неизвестно'."
                )
        else:
            if not any([data.get('continent'), data.get('country'), data.get('region'), data.get('city')]):
                raise serializers.ValidationError(
                    "Укажите хотя бы одно место съемки или выберите 'Место съемки неизвестно'."
                )

    def validate_date(self, data):
        year = data.get('year')
        month = data.get('month')
        day = data.get('day')
        if year is None:
            raise serializers.ValidationError(
                "Год должен быть указан или выбрана опция 'дата неизвестна'."
            )
        date = self.construct_date(year, month, day)
        self.check_date_in_future(date)
        self.check_minimal_date(date)

    def construct_date(self, year, month, day):
        try:
            if day is not None and month is not None:
                return datetime.date(year, month, day)
            elif month is not None:
                return datetime.date(year, month, 1)
            else:
                return datetime.date(year, 1, 1)
        except ValueError:
            raise serializers.ValidationError("Некорректная дата.")

    def check_date_in_future(self, date):
        if date > datetime.date.today():
            raise serializers.ValidationError("Дата не может быть в будущем.")

    def check_minimal_date(self, date):
        if date < datetime.date(1826, 1, 1):
            raise serializers.ValidationError(
                "Дата не может быть ранее 1826 года, когда была сделана первая фотография."
            )

    class Meta:
        model = Post
        fields = [
            'id', 'name', 'author', 'description', 'day', 'month', 'year',
            'is_date_unknown', 'is_approx_date', 'continent', 'country', 'region', 'city',
            'created_at', 'updated_at', 'tags', 'comments', 'is_location_unknown', 'photo'
        ]
        extra_kwargs = {
            'is_approx_date': {'help_text': 'Отметьте, если дата фотосъёмки является примерной.'},
            'is_date_unknown': {'help_text': 'Отметьте, если дата фотосъёмки неизвестна.'},
            'is_location_unknown': {'help_text': 'Отметьте, если место фотосъёмки неизвестно.'},
        }
