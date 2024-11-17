from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'class': 'name w-100 theme-border pl-20 pt-15 pb-15 pr-10 form-color border-radius5 openS-font-family'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your Email',
                'class': 'email w-100 theme-border pl-20 pt-15 pb-15 pr-10 form-color border-radius5 openS-font-family'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Your Phone',
                'class': 'phone w-100 theme-border pl-20 pt-15 pb-15 pr-10 form-color border-radius5 openS-font-family'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Your Subject',
                'class': 'subject w-100 theme-border pl-20 pt-15 pb-15 pr-10 form-color border-radius5 openS-font-family'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Start writing message here',
                'class': 'massage w-100 theme-border pl-20 pt-15 pr-10 primary-color border-radius5 openS-font-family'
            }),
        }
