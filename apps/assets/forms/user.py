# -*- coding: utf-8 -*-
#
from django import forms
from django.utils.translation import gettext_lazy as _

from ..models import AdminUser, SystemUser
from common.utils import validate_ssh_private_key, ssh_pubkey_gen, get_logger

logger = get_logger(__file__)
__all__ = [
    'FileForm', 'SystemUserForm', 'AdminUserForm', 'PasswordAndKeyAuthForm',
]


class FileForm(forms.Form):
    file = forms.FileField()


class PasswordAndKeyAuthForm(forms.ModelForm):
    # Form field name can not start with `_`, so redefine it,
    password = forms.CharField(
        widget=forms.PasswordInput, max_length=128,
        strip=True, required=False,
        help_text=_('Password or private key passphrase'),
        label=_("Password"),
    )
    # Need use upload private key file except paste private key content
    private_key_file = forms.FileField(required=False, label=_("Private key"))

    def clean_private_key_file(self):
        private_key_file = self.cleaned_data['private_key_file']
        password = self.cleaned_data['password']

        if private_key_file:
            key_string = private_key_file.read()
            private_key_file.seek(0)
            if not validate_ssh_private_key(key_string, password):
                raise forms.ValidationError(_('Invalid private key'))
        return private_key_file

    def validate_password_key(self):
        password = self.cleaned_data['password']
        private_key_file = self.cleaned_data.get('private_key_file', '')

        if not password and not private_key_file:
            raise forms.ValidationError(_(
                'Password and private key file must be input one'
            ))

    def gen_keys(self):
        password = self.cleaned_data.get('password', '') or None
        private_key_file = self.cleaned_data['private_key_file']
        public_key = private_key = None

        if private_key_file:
            private_key = private_key_file.read().strip().decode('utf-8')
            public_key = ssh_pubkey_gen(private_key=private_key, password=password)
        return private_key, public_key


class AdminUserForm(PasswordAndKeyAuthForm):
    def save(self, commit=True):
        # Because we define custom field, so we need rewrite :method: `save`
        admin_user = super().save(commit=commit)
        password = self.cleaned_data.get('password', '') or None
        private_key, public_key = super().gen_keys()
        admin_user.set_auth(password=password, public_key=public_key, private_key=private_key)
        return admin_user

    def clean(self):
        super().clean()
        if not self.instance:
            super().validate_password_key()

    class Meta:
        model = AdminUser
        fields = ['name', 'username', 'password', 'private_key_file', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _('Name')}),
            'username': forms.TextInput(attrs={'placeholder': _('Username')}),
        }
        help_texts = {
            'name': '* required',
            'username': '* required',
        }


class SystemUserForm(PasswordAndKeyAuthForm):
    # Admin user assets define, let user select, save it in form not in view
    auto_generate_key = forms.BooleanField(initial=True, required=False)

    def save(self, commit=True):
        # Because we define custom field, so we need rewrite :method: `save`
        system_user = super().save()
        password = self.cleaned_data.get('password', '') or None
        auto_generate_key = self.cleaned_data.get('auto_generate_key', False)
        private_key, public_key = super().gen_keys()

        if auto_generate_key and not password:
            logger.info('Auto generate key and set system user auth')
            system_user.auto_gen_auth()
        else:
            system_user.set_auth(password=password, private_key=private_key, public_key=public_key)
        return system_user

    def clean(self):
        super().clean()
        auto_generate = self.cleaned_data.get('auto_generate_key')
        if not self.instance and not auto_generate:
            super().validate_password_key()

    class Meta:
        model = SystemUser
        fields = [
            'name', 'username', 'protocol', 'auto_generate_key',
            'password', 'private_key_file', 'auto_push', 'sudo',
            'comment', 'shell', 'priority',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _('Name')}),
            'username': forms.TextInput(attrs={'placeholder': _('Username')}),
        }
        help_texts = {
            'name': '* required',
            'username': '* required',
            'auto_push': _('Auto push system user to asset'),
            'priority': _('High level will be using login asset as default, if user was granted more than 2 system user'),
        }