from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Inquiry


class InquiryForm(forms.ModelForm):
    """詢價表單"""
    class Meta:
        model = Inquiry
        fields = ['name', 'phone', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '您的姓名'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '聯絡電話'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': '請輸入留言...'}),
        }


class RegisterForm(UserCreationForm):
    """會員註冊表單"""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '帳號'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': '密碼'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': '確認密碼'})


class LoginForm(AuthenticationForm):
    """登入表單"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': '帳號'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': '密碼'})


class CarSearchForm(forms.Form):
    """搜尋 / 篩選表單"""
    keyword = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': '搜尋車款...'}),
    )
    fuel_type = forms.ChoiceField(
        required=False,
        choices=[('', '所有燃料'), ('gasoline', '汽油'), ('diesel', '柴油'),
                 ('electric', '電動'), ('hybrid', '油電混合')],
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    min_price = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': '最低價格'}),
    )
    max_price = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': '最高價格'}),
    )
