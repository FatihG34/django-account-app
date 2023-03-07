from rest_framework import serializers, validators
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    password_1 = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = (
            'id',
            'username',  # ! this field can be used identity_number
            'first_name',
            'last_name',
            'email',
            'profile_photo',
            'phone_number_1',
            'phone_number_2',
            'address_1',
            'address_2',
            'town',
            'city',
            'post_code',
            'country',
            'password',
            'password_1'
        )

    def validate(self, data):
        if data['password'] != data['password_1']:
            raise serializers.ValidationError(
                {
                    'password': "Password didn't match"
                }
            )
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password_1')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "profile_photo",
            "phone_number_1",
            "phone_number_2",
            "address_1",
            "address_2",
            "town",
            "city",
            "post_code",
            "country",
            "updated_date"
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "profile_photo",
            "phone_number_1",
            "phone_number_2",
            "address_1",
            "address_2",
            "town",
            "city",
            "post_code",
            "country",
            "updated_date",
            "is_staff",
        )


class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = (
            'key',
            'user'
        )
