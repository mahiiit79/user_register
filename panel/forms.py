from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(),
        label= 'ایمیل',
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator()
        ]
    )

    password = forms.CharField(
        widget= forms.PasswordInput(),
        label= 'رمزعبور',
        validators= [
            validators.MaxLengthValidator(100),
            validators.RegexValidator( r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$',
                                       message=' رمز عبور باید شامل حداقل یک حرف بزرگ و یک حرف کوچک یک رقم و حداقل 8 کاراکتر باشد')
        ]
    )

    confirm_password = forms.CharField(
        widget= forms.PasswordInput(),
        label= 'تکرار رمز عبور',
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        else:
            raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')



class LoginForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
