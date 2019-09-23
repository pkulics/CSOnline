from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    # 用户名和密码不能为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)


class RegisterForm(forms.Form):
    '''注册验证表单'''
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)
    captcha = CaptchaField(error_messages={'invalid':'验证码错误'})


class ForgetPwdForm(forms.Form):
    '''忘记密码'''
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid':'验证码错误'})


class ModifyPwdForm(forms.Form):
    '''重置密码'''
    password1 = forms.CharField(required=True,min_length=5)
    password2 = forms.CharField(required=True,min_length=5)
    