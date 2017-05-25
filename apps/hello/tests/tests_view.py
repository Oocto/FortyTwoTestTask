from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse, resolve
from ..models import Contact
from model_mommy import mommy
# Create your tests here.


class SomeTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.my_instance = mommy.make('hello.Contact')
        self.response = self.client.get(reverse("my_info"))

    def test_the_info_view(self):
        """Test for the view returning hard-coded data for the template"""

        info_url = resolve('/')
        self.assertEqual(info_url.func.__name__, 'Info_view')
        self.assertEqual(self.response.status_code, 200)

    def test_for_template(self):
        """Test for template correctness"""
        self.assertTemplateUsed(self.response, 'my_info_template.html')

    def test_the_view_render_Contact_instance(self):
        """Test that view renders data from model"""

        my_info = self.response.context_data['info']
        self.assertIsInstance(my_info, Contact)

        model_instance = Contact.objects.all()
        for c in model_instance:
            self.assertIn(c.name, self.response.content)
            self.assertIn(c.surname, self.response.content)
            self.assertIn(c.email, self.response.content)
            self.assertIn(c.jabber, self.response.content)
            self.assertIn(c.skype, self.response.content)
