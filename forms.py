# This is the form for the Grade Level Text Analyzer.
class TextForm(forms.Form):
    # Create a CharField to hold the text input, using a textarea widget for multiline input.
    text = forms.CharField(
        # Configure the textarea widget with Bootstrap class for styling and set its size.
        widget=forms.Textarea(
            attrs={"class": "form-control", "rows": 5, "style": "max-width: 500px;"}
        ),
        label="Enter text to analyze",  # Set the label for the text input field.
        # Add validators to ensure the text length is within the specified range.
        validators=[
            # Minimum length validator: Text must be at least 1200 characters.
            MinLengthValidator(
                1200, message="The sample you've provided is too short."
            ),
            # Maximum length validator: Text must not exceed 10000 characters.
            MaxLengthValidator(
                10000, message="The sample you've provided is too long."
            ),
        ],
    )
