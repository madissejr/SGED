from django import forms
from django.contrib.auth.forms import PasswordChangeForm


class UserChangePassword(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserChangePassword, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
