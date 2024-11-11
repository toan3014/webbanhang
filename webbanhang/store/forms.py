from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Địa chỉ Email", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Địa chỉ Email'}))
    first_name = forms.CharField(label="Họ", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Họ'}))
    last_name = forms.CharField(label="Tên", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tên'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Tên tài khoản'
        self.fields['username'].label = 'Tên tài khoản'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Bắt buộc. Tối đa 150 ký tự. Chỉ có chữ cái, chữ số và các ký tự @/./+/-/_.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Mật khẩu'
        self.fields['password1'].label = 'Mật khẩu'
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Mật khẩu không được giống thông tin cá nhân của bạn.</li><li>Mật khẩu phải chứa ít nhất 8 ký tự.</li><li>Mật khẩu không được là một mật khẩu phổ biến.</li><li>Mật khẩu không được chỉ chứa các ký tự số.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Nhập lại mật khẩu'
        self.fields['password2'].label = 'Nhập lại mật khẩu'
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Nhập lại mật khẩu để xác nhận.</small></span>'