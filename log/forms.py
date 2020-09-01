from django import forms
from django.contrib.auth.models import User
from django.core import validators


class LoginForm(forms.Form):
    user_name_l = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری را وارد کنید', 'class': 'input'}),
        label='نام کاریری'
    )

    password_l = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور را وارد کنید', 'class': 'input'}),
        label='کلمه ی عبور'
    )

    def clean_user_name(self):
        user_name_l = self.cleaned_data.get('user_name')
        is_exists_user = User.objects.filter(username=user_name_l).exists()
        if not is_exists_user:
            raise forms.ValidationError('کاربری با این نام یافت نشد')
        return user_name_l


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری را وارد کنید', 'class': 'input'}),
        label='نام کاریری',
        validators=[
            validators.MaxLengthValidator(limit_value=20, message='تعداد کارکتر بیشتر از 20 است'),
            validators.MinLengthValidator(4, 'تعداد کارکتر کمی وارد شده')
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل  را وارد کنید', 'class': 'input'}),
        label='ایمیل ',
        validators=[validators.EmailValidator('ایمیل صحیح نیست')]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور را وارد کنید', 'class': 'input'}),
        label='کلمه ی عبور'
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور را تکرار کنید', 'class': 'input'}),
        label=' تکرار کلمه ی عبور'
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError('ایمیل تکراری است')
        # if len(email) > 20:
        #     raise forms.ValidationError('تعداد کارکتر های ایمیل باید کمتر از 20 باشد')
        return email

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exists_user_by_username = User.objects.filter(username=user_name).exists()

        if is_exists_user_by_username:
            raise forms.ValidationError('کاربر قبلا ثبت نام کرده')
        return user_name

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('رمز ها مغایرت دارند')
        return password


