from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your Email'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Message'}))


#class UserInfoForm(forms.Form):
#    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;'}))
#    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 300px;'}))