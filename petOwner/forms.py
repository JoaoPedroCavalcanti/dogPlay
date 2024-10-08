from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.django_forms import add_attr, add_placeholder

# register
class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: John')
        add_placeholder(self.fields['last_name'], 'Ex.: Doe')
        add_attr(self.fields['username'], 'css', 'a-css-class')

    password = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Password must not be empty'
        },
        help_text=(
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        ),
        label='Password'
    )
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
    
    
# Login
class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Type your username')
        add_placeholder(self.fields['password'], 'Type your password')
        
    
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )








    # password2 = forms.CharField(
    #     required=True,
    #     widget=forms.PasswordInput(attrs={
    #         'placeholder': 'Repeat your password'
    #     })
    # )




        # exclude = ['first_name']
        # labels = {
        #     'username': 'Username',
        #     'first_name': 'First name',
        #     'last_name': 'Last name',
        #     'email': 'E-mail',
        #     'password': 'Password',
        # }
        # help_texts = {
        #     'email': 'The e-mail must be valid.',
        # }
        # error_messages = {
        #     'username': {
        #         'required': 'This field must not be empty',
        #     }
        # }
        # widgets = {
        #     'first_name': forms.TextInput(attrs={
        #         'placeholder': 'Type your username here',
        #         'class': 'input text-input'
        #     }),
        #     'password': forms.PasswordInput(attrs={
        #         'placeholder': 'Type your password here'
        #     })
        # }

    # def clean_password(self):
    #     data = self.cleaned_data.get('password')

    #     if 'teste' in data:
    #         raise ValidationError(
    #             'Não digite %(value)s no campo password',
    #             code='invalid',
    #             params={'value': '"teste"'}
    #         )


    #     return data

    # def clean_first_name(self):
    #     data = self.cleaned_data.get('first_name')

    #     if 'teste' in data:
    #         raise ValidationError(
    #             'Não digite %(value)s no campo first name',
    #             code='invalid',
    #             params={'value': '"teste"'}
    #         )

    #     return data
    
    # def clean(self):
    #     cleaned_data = super().clean()

    #     password = cleaned_data.get('password')
    #     password2 = cleaned_data.get('password2')

    #     if password != password2:
    #         password_confirmation_error = ValidationError(
    #             'Password and password2 must be equal',
    #             code='invalid'
    #         )
    #         raise ValidationError({
    #             'password': password_confirmation_error,
    #             'password2': [
    #                 password_confirmation_error,
    #             ],
    #         })
    
    
    