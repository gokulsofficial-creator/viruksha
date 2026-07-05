from django import forms
from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'email', 'phone', 'company_name', 'service_type', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-border-subtle rounded focus:outline-none focus:border-secondary focus:ring-1 focus:ring-secondary',
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 border border-border-subtle rounded focus:outline-none focus:border-secondary focus:ring-1 focus:ring-secondary',
                'placeholder': 'Enter your email address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-border-subtle rounded focus:outline-none focus:border-secondary focus:ring-1 focus:ring-secondary',
                'placeholder': 'Enter your phone number'
            }),
            'company_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-border-subtle rounded focus:outline-none focus:border-secondary focus:ring-1 focus:ring-secondary',
                'placeholder': 'Enter your company name (optional)'
            }),
            'service_type': forms.Select(attrs={
                'class': 'w-full px-4 py-3 border border-border-subtle rounded focus:outline-none focus:border-secondary focus:ring-1 focus:ring-secondary bg-surface-white'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-border-subtle rounded focus:outline-none focus:border-secondary focus:ring-1 focus:ring-secondary',
                'placeholder': 'Brief subject of your enquiry'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 border border-border-subtle rounded focus:outline-none focus:border-secondary focus:ring-1 focus:ring-secondary',
                'placeholder': 'Describe your project requirements or material needs in detail...',
                'rows': 5
            }),
        }
