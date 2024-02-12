from django import forms

class ContractFileForm(forms.Form):
    contract_file = forms.FileField(label="Upload a Contract")