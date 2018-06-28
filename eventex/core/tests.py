from django.test import TestCase

class HomeTest(TestCase):
    def setUp(self):
        """Setup access / """
        self.response = self.client.get('/')

    def test_get(self):
        """GET / must return code 200"""
        self.assertEquals(200, self.response.status_code)

    def test_template_used(self):
        """Must be used index.html"""
        self.assertTemplateUsed(self.response, 'index.html')
