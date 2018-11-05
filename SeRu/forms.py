from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import User


class UserCreateForm(UserCreationForm):
    telefono_contacto = forms.CharField(max_length=9, required=True)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('telefono_contacto',)

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("No se puede crear un usuario y un perfil de usuario sin save() en la base de datos")
        user = super(UserCreateForm, self).save(commit=True)
        user_profile = User(telefono_contacto=self.cleaned_data['telefono_contacto'],)
        user_profile.save()
        return user, user_profile