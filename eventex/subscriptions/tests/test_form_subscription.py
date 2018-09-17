from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        """Form must have 4 fields """
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """ CPF must only accept digits """

        form = self.make_validated_form(cpf='ABCD5678901')
        # self.assertListEqual(['cpf'], list(form.errors))
        errors = form.errors
        field = 'cpf'
        errors_list = errors[field]
        msg = 'CPF deve conter apenas números'
        self.assertEqual([msg], errors_list)

    def test_cpf_11_digitos(self):
        form = self.make_validated_form(cpf='1234')
        self.assertListEqual(['cpf'], list(form.errors))

    def test_must_be_capitalized(self):
        form = self.make_validated_form(name='ORLANDO Saraiva')
        self.assertEqual('Orlando Saraiva', form.cleaned_data['name'])

    def make_validated_form(self, **kwargs):
        valid =  dict(
            name='Orlando Saraiva Jr',
            cpf='12345678901',
            email='orlandosaraivajr@gmail.com',
            phone='19992975416'
        )
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form