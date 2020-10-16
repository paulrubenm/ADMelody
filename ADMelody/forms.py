from django import forms

def should_be_empty(value)
  if value:
    raise forms.ValidationError('Field is not empty')

class ContactForm(forms.Form)
  name = forms.CharField(max_length=80)
  message = forms.CharField(widget=forms.Textarea, required=True)
  email = forms.EmailField(required=True)
  phone = forms.NumberInput()
  forcefield = forms.CharField(
    required=False, widget=forms.HiddenInput, label="leave empty", validators=[should_be_empty])
  )
  