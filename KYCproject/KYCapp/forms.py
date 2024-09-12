from django import forms

class KnowYourCustomerForm(forms.Form):
    first_name = forms.CharField(max_length=50, label="First Name", error_messages={'required': 'Please fill in your first name', 'max_length': 'Name should  not be longer than 50 characters'}, widget=forms.TextInput({'class': 'form-control', 'placeholder':'John'}), required=False)

    last_name = forms.CharField(max_length=50, label="Last Name", error_messages={'required': 'Please fill in your last name', 'max_length': 'Name should  not be longer than 50 characters'}, widget=forms.TextInput({'class': 'form-control', 'placeholder':'Doe'}), required=False)
    
    date_of_birth = forms.CharField(label="Date of Birth", error_messages={'required':'Please fill in your date of birth'}, widget=forms.CharField({'class': 'form-control', 'placeholder': '01/01/2000'}), required=False)

    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')], label="Gender", required=False)    

    country = forms.ChoiceField(choices=[('Uganda', 'Kenya', 'Tanzania', 'Rwanda', 'Burundi')], label="Country", required=False)

    district=forms.ChoiceField(choices=[('Kampala', 'Nairobi', 'Kigali', 'Dar Es Salaam', 'Bujumbura')], label="District", required=False)
     
    town = forms.ChoiceField(choices=[('Kampala', 'Nairobi', 'Kigali', 'Bujumbura', 'Dar Es Salaam')], label="Town", required=False)
     
    zip_code = forms.CharField(max_length=20, label="Zip Code", error_messages={'required':'Please enter a zip code', 'max_length':'Your zip code should not be more than 20 characters'}, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '12345'}), required=False)

    phone_number_1 = forms.CharField(max_length=20, label="Phone Number 1", error_messages={'required':'Please enter a contact', 'max_length':'Your contact should not be more than 20 characters'}, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+256 712345678'}), required=False)

    phone_number_2 = forms.CharField(max_length=20, label="Phone Number 2", error_messages={'required':'Please enter a contact', 'max_length':'Your contact should not be more than 20 characters'}, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+256 712345678'}), required=False)

    email = forms.EmailField(max_length=50, label="Email", error_messages={'required':'Please enter a valid email address', 'max_length':'Your email should not be more than 50 characters'}, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'johndoe@example.com'}), required=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'