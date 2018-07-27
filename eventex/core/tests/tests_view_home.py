from django.test import TestCase
from django.shortcuts import resolve_url as r

class HomeTest(TestCase):
    def setUp(self):
        """Setup access / """
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET / must return code 200"""
        self.assertEquals(200, self.response.status_code)

    def test_template_used(self):
        """Must be used index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expected)