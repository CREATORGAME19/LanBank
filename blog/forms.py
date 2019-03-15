from django import forms

class ContactForm(forms.Form):
    word = forms.CharField(
        max_length=20000,
        widget=forms.Textarea(),
    )
    translation = forms.CharField(
        max_length=20000,
        widget=forms.Textarea(),
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        word = cleaned_data.get('word')
        translation = cleaned_data.get('translation')
        if not word and not translation:
            raise forms.ValidationError('You have to write something!')
class BlankForm(forms.Form):
    def clean(self):
        cleaned_data = super(BlankForm, self).clean()
class AnswerForm(forms.Form):
    answer = forms.CharField(
        max_length=20000,
        widget=forms.Textarea(),
    )

    def clean(self):
        cleaned_data = super(AnswerForm, self).clean()
        answer = cleaned_data.get('answer')
        if not answer:
            raise forms.ValidationError('You have to write something!')
class RemoveForm(forms.Form):
    item_number = forms.CharField(
        max_length=20000,
        widget=forms.Textarea(),
    )

    def clean(self):
        cleaned_data = super(RemoveForm, self).clean()
        item_number = cleaned_data.get('item_number')
        if not item_number:
            raise forms.ValidationError('You have to write something!')
