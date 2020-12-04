# Это именно низкоуровневые интерфейсы взаимодействия с моделью
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser 
        fields = UserCreationForm.Meta.fields + ('age', 'phone_number', 'salary_amount',)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = UserChangeForm.Meta.fields