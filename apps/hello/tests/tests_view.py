from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse, resolve

# Create your tests here.


class SomeTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse("my_info"))

    def test_the_info_view(self):
        """Test for the view returning hard-coded data for the template"""

        info_url = resolve('/')
        self.assertEqual(info_url.func.__name__, 'Info_view')
        self.assertEqual(self.response.status_code, 200)
        self.assertIn(b'Oleg', self.response.content)
        self.assertIn(b'Panchyshyn', self.response.content)
        self.assertIn(b'octo.oleg@gmail.com', self.response.content)

    def test_for_template(self):
        """Test for template correctness"""
        self.assertTemplateUsed(self.response, 'my_info_template.html')
