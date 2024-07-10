from .models import Runtext
from django import forms


class RuntextForm(forms.ModelForm):
    class Meta:
        model = Runtext
        fields = '__all__'
        widgets = {
            'text': forms.Textarea(
                attrs={'class': 'form-control', 'rows': '5', 'style': 'resize: none;'}
            ),
            'text_color': forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color'}),
            'background_color': forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            if field.name not in ("text", "text_color", "background_color"):
                field.field.widget.attrs["class"] = "form-control"
