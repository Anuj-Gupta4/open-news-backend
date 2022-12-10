from django import forms
from .models import article

class articleform(forms.ModelForm):
    class Meta:
        model = article
        fields = ["headline", 
        "byline", 
        "introduction", 
        "body", 
        "conclusion",
        "image",
        ]
        # labels = {
        #     "headline": "Enter your news title",
        #     "byline": "Enter author name",
        #     "introduction": "Enter Introduction part",
        #     "body": "Enter description",
        #     "conclusion": "Enter conclusion",
        #     }
        widgets = {
            'headline':forms.TextInput(attrs={'class':'form-control'}),
            'byline':forms.TextInput(attrs={'class':'form-control'}),
            'introduction':forms.Textarea(attrs={'class':'form-control'}), 
            'body':forms.Textarea(attrs={'class':'form-control'}), 
            'conclusion':forms.Textarea(attrs={'class':'form-control'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
        }