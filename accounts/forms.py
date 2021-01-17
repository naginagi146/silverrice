from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.shortcuts import redirect, get_object_or_404



class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'user_photo', 'user_name', 'first_name', 'last_name', 'date_of_birth')
        widgets = {
            'date_of_birth': forms.SelectDateWidget
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'user_name', 'email',
            'user_photo',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

# class FollowForm(forms.ModelForm):

#     class Meta:
#         model = MyUser
#         fields = ("following",)

    # def follow(self, request, pk):
    #     follow = get_object_or_404(MyUser, pk=pk)
    #     to_user = Post.objects.get(user=id)
    #     if request.method == 'POST':
    #         # データの新規追加
    #         user = request.user
    #         follow.myuser.following(to_user)
    #         follow.save()

    #     return redirect('account/profile.html')
