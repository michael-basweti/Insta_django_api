from .models import MyUser, Profile
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    """Serializers userserializer requests and creates a new user."""

    # Ensure email is provided and is unique
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=MyUser.objects.all(),
                message='This email is already used by another user',
            )
        ],
        error_messages={
            'required': 'Email is required',
        }
    )

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.RegexField(
        regex="^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
        max_length=128,
        min_length=8,
        write_only=True,
        required=True,
        error_messages={
            'required': 'Password is required',
            'invalid': 'Password must have a number and a letter',
            'min_length': 'Password must have at least 8 characters',
            'max_length': 'Password cannot be more than 128 characters'
        }
    )
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # posts = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="posts:post_create_view")
   
    class Meta:
        model = MyUser
        fields = (
            'id',
            'email',
            'full_name',
            'password',
            'posts'
        )
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        user = MyUser(
            email=validated_data['email'],
            full_name=validated_data['full_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    # username = serializers.RegexField(
    #     regex='^(?!.*\ )[A-Za-z\d\-\_]+$',
    #     min_length=4,
    #     required=True,
    #     source='user.username',
    #     validators=[
    #         UniqueValidator(
    #             queryset=Profile.objects.all(),
    #             message='Username must be unique',
    #         )
    #     ],
    #     error_messages={
    #         'invalid': 'Username cannot have a space',
    #         'required': 'Username is required',
    #         'min_length': 'Username must have at least 4 characters'
    #     }
    # )

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        super().update(instance, validated_data)
        if user_data is not None and user_data.get('user_id') is not None:
            instance.user.username = user_data.get('user_id')
            instance.user.save()
        return instance

    class Meta:
        model = Profile
        fields = '__all__'