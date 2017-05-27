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

        model_instance = Contact.objects.first()
        rendered_bio = model_instance.bio.split('.\n')
        self.assertIn(model_instance.name, self.response.content)
        self.assertIn(model_instance.surname, self.response.content)
        self.assertIn(model_instance.email, self.response.content)
        self.assertIn(model_instance.jabber, self.response.content)
        self.assertIn(rendered_bio[0], self.response.content)
        self.assertIn(rendered_bio[1], self.response.content)
        self.assertIn(model_instance.skype, self.response.content)
        self.assertIn(model_instance.contacts, self.response.content)

class SomeTestsRequestsView(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse("my_requests_story"))
    
    def test_for_requests_template(self):
        """Test for template correctness"""
        self.assertTemplateUsed(self.response, 'my_requests_template.html')

    def test_requests_view(self):
        """Test for view its url """
        response = self.client.get(reverse("my_requests_story"))
        request_url = resolve('/requests')
        self.assertEqual(request_url.func.__name__, 'Requests_view')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<th>Request method</th>', response.content)
        self.assertIn(b'<th>Request link</th>', response.content)
        self.assertIn(b'<th>Request date</th>', response.content)