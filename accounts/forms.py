from django import forms
from django.contrib.auth.models import User



class UserRegisterForm(forms.ModelForm):
    # username = forms.TextInput()
    # email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','email','password')
        help_texts = {
            'username': None,
        }

    def save(self, commit=True):
        # save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

