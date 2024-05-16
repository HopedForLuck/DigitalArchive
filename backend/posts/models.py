from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models

User = get_user_model()

LENGTH_TEXT = 20
LENGTH_NAME = 200
LENGTH_SLUG = 50
LENGTH_DESCRIPTIONS = 500
LENGTH_LOCATION = 100


class Post(models.Model):
    name = models.CharField(
        max_length=LENGTH_NAME,
        verbose_name='Название',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор поста",
    )
    description = models.TextField(
        max_length=LENGTH_DESCRIPTIONS,
        verbose_name="Описание",
        null=True,
        blank=True,
    )
    photo = models.ImageField(
        upload_to='photos/',
        verbose_name="Фотография",
    )

    # Поля для работы с датой
    is_date_unknown = models.BooleanField(
        default=False,
        verbose_name="Известна ли дата фотосъёмки",
        help_text="Отметьте если дата фотосъёмки неизвестна",
    )
    day = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(31)],
        verbose_name="День фотографии",
    )
    month = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        verbose_name="Месяц фотографии",
    )
    year = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Год фотографии",
    )
    is_approx_date = models.BooleanField(
        default=False,
        verbose_name="Указана ли примерная дата",
        help_text="Отметьте если дата фотосъёмки указана примерно",
    )

    # Поля для работы с географическими данными
    is_location_unknown = models.BooleanField(
        default=False,
        verbose_name="Известно ли место фотосъёмки",
        help_text="Отметьте если место фотосъёмки неизвестно",
    )
    continent = models.ForeignKey(
        'Continent',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Материк",
    )
    region = models.ForeignKey(
        'Region',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Регион",
    )
    country = models.ForeignKey(
        'Country',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Страна",
    )
    area = models.ForeignKey(
        'Area',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Область",
    )
    city = models.ForeignKey(
        'City',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Город",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField(
        'Tag',
        verbose_name='Теги',
        related_name='posts',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.name[:LENGTH_TEXT]


class Tag(models.Model):
    name = models.CharField(
        max_length=LENGTH_NAME,
        verbose_name='Название',
        unique=True,
    )
    slug = models.SlugField(
        max_length=LENGTH_SLUG,
        verbose_name='slug',
        unique=True,
        validators=[RegexValidator(
            regex=r'^[-a-zA-Z0-9_]+$',
            message='Слаг содержит недопустимый символ'
        )]
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name[:LENGTH_TEXT]


class Comment(models.Model):

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор комментария",
    )
    text = models.TextField(
        max_length=LENGTH_DESCRIPTIONS,
        verbose_name="Текст комментария",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:LENGTH_TEXT]


class Continent(models.Model):
    name = models.CharField(
        max_length=LENGTH_LOCATION,
        unique=True,
        verbose_name="Название континента",
    )

    class Meta:
        verbose_name = 'Континент'
        verbose_name_plural = 'Континенты'

    def __str__(self):
        return self.name[:LENGTH_TEXT]


class Region(models.Model):
    name = models.CharField(
        max_length=LENGTH_LOCATION,
        unique=True,
        verbose_name="Название региона",
    )
    continent = models.ForeignKey(
        Continent,
        on_delete=models.CASCADE,
        verbose_name="Континент",
    )

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return self.name[:LENGTH_TEXT]


class Country(models.Model):
    name = models.CharField(
        max_length=LENGTH_LOCATION,
        unique=True,
        verbose_name="Название страны",
    )
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        verbose_name="Регион",
    )

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name[:LENGTH_TEXT]


class Area(models.Model):
    name = models.CharField(
        max_length=LENGTH_LOCATION,
        unique=True,
        verbose_name="Название области",
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        verbose_name="Страна",
    )

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Области'

    def __str__(self):
        return self.name[:LENGTH_TEXT]


class City(models.Model):
    name = models.CharField(
        max_length=LENGTH_LOCATION,
        unique=True,
        verbose_name="Название города",
    )
    area = models.ForeignKey(
        Area,
        on_delete=models.CASCADE,
        verbose_name="Область",
    )

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name[:LENGTH_TEXT]
