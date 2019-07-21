from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class UserCreate(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email')


class UserChange(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields = ('username', 'email')


