from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Orlando Saraiva Jr", cpf="12345678901",
                    email="orlandosaraivajr@gmail.com", phone="19-99297-5416")
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br','orlandosaraivajr@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Orlando Saraiva Jr',
            '12345678901',
            'orlandosaraivajr@gmail.com',
            '19-99297-5416',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
