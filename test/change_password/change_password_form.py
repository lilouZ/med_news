class CustomPasswordChange(PasswordChangeForm):
    error_css_class = 'has-error'
    error_messages = {'password_incorrect':
                "The old password is not correct. Please try again."}
    password_error_messages = {
        'password_mismatch': ('The two password fields didn’t match.'),
    }
    old_password = forms.CharField(required=True, label='Old Password',
                    widget=forms.PasswordInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter you old password ..'
                    }),
                    error_messages={
                    'required': 'The password can not be empty'})

    new_password1 = forms.CharField(required=True, label='New Password',
                    widget=forms.PasswordInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Enter you New password ..'
                    }),
                    error_messages={
                    'required': 'The password can not be empty'})
    new_password2 = forms.CharField(required=True, label='Confirm New Password',
                    widget=forms.PasswordInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Confirm you New password ..'
                    }),
                    error_messages={
                    'required': 'The password can not be empty'})

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.password_error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        password_validation.validate_password(password2, self.user)
        return password2