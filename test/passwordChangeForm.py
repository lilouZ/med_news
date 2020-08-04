
class CustomPasswordChange(PasswordChangeForm):
    error_css_class = 'has-error'
    error_messages = {'password_incorrect':
                "The old password is not correct. Please try again."}
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