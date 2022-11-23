from django import forms

tipo_de_planilhas = (
    ('1', 'CSV'),
    ('2', 'EXCEL'),
)


class UploadFileForm(forms.Form):
    file = forms.FileField()
    options = forms.ChoiceField(choices=tipo_de_planilhas)
    widgets = {
        file: forms.FileInput(),
        options: forms.SelectMultiple(),
    }
