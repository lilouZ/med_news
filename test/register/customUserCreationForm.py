class UserForm(UserCreationForm):
    email_error_messages = {
        'email_is_not_unique':('The email is already exist !'),
    }
    password1 = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                        'placeholder':'password',
                                        'required': 'true',

        })
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                        'placeholder':'Enter the same password as above, for verification.',
                                        'type': 'password',
                                        'required': 'true',
        })
    )
    email = forms.CharField(
        label=("Email"),
        widget=forms.TextInput(attrs={'class': 'form-control',
                                    'type': 'email',
                                    'placeholder': 'Email address',
                                    'required': 'true'
        })
    )
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
        }



    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                self.email_error_messages['email_is_not_unique'],
                code='email_is_not_unique',
            )
        return email

        