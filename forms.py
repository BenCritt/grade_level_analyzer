from django import forms
from django.core.exceptions import ValidationError
from django import forms
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
)


class TextForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "rows": 5, "style": "max-width: 500px;"}
        ),
        label="Enter text to analyze",
        validators=[
            MinLengthValidator(
                1200, message="The sample you've provided is too short."
            ),
            MaxLengthValidator(
                10000, message="The sample you've provided is too long."
            ),
        ],
    )
