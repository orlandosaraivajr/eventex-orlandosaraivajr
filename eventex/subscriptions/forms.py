from django import forms
from django.core.exceptions import ValidationError

<<<<<<< HEAD

def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números')
    if len(value) != 11:
        raise ValidationError('CPF deve conter onze números')

class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Telefone')
=======
from eventex.subscriptions.models import Subscription

'''
class SubscriptionFormOld(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='Email', required=False)
    phone = forms.CharField(label='Telefone', required=False)

'''

class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = ['name','cpf','email','phone']
>>>>>>> 0c1e7745507a033ee2e39b332021a4795a39a8bf

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
<<<<<<< HEAD
        return ' '.join(words)
=======
        return ' '.join(words)

    def clean(self):
        self.cleaned_data = super().clean()
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone')

        return self.cleaned_data
>>>>>>> 0c1e7745507a033ee2e39b332021a4795a39a8bf
