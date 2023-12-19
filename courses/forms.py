from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.forms import ValidationError
from django import forms


class RegisterForm(UserCreationForm):
    username = forms.CharField(label = "使用者名稱")
    first_name = forms.CharField(label = "名字")
    last_name = forms.CharField(label = "姓氏")
    email = forms.EmailField(label = "電子郵件")
    password1 = forms.CharField(label = "密碼", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "確認密碼", widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
    
    # 檢查 email 是否已經被註冊
    def clean_email(self):
        email = self.cleaned_data["email"]
        user = None
        try:
            user = User.objects.get(email = email)
        except:
            return email
        
        if user is not None:
            raise ValidationError("這個 Email 已被註冊過了!")
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label = "使用者名稱/電子郵件", required=True)
    password = forms.CharField(label = "密碼", required=True, widget = forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        user = None
        
        # 檢查使用者名稱/電子郵件是否存在
        try:
            if "@" in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)
                
        except:
            raise ValidationError("使用者名稱/電子郵件不存在!")

        # 檢查密碼是否正確
        result = authenticate(username=user.username, password=password)
        if result is not None:
            login(self.request, result)
            return self.cleaned_data
        else:
            raise ValidationError("密碼錯誤")
