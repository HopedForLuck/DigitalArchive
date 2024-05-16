from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'bio',
            'password',  # Обратить внимание на безопасное использование
        )
        extra_kwargs = {
            'password': {'write_only': True},  # Гарантирует, что пароль не будет отображаться при запросе данных
            'confirmation_code': {'read_only': True}  # Поле confirmation_code не доступно для изменения через API
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        # Пример обработки обновления пользователя, включая безопасное обновление пароля
        instance = super().update(instance, validated_data)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            instance.save()
        return instance