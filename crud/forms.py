from django import forms
from crud.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','firstname','lastname',
                  'age','gender','permissionLevel',"email",
                  'height','weight','nickname','bio','bloodGroup'
                  ]
        widgets = {
            # 'profilePicture': forms.FileInput(),
            'permissionLevel':forms.NumberInput(),
            'height':forms.NumberInput(),
            'weight':forms.NumberInput(),
            'age':forms.NumberInput()
        }

