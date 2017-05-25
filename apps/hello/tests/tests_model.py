from django.test import TestCase
from apps.hello.models import Contact
from model_mommy import mommy

# Create your tests here.


class SomeTestsModel(TestCase):

    def setUp(self):
        self.my_instance = mommy.make('hello.Contact', id=2)

    def test_the_model(self):
        """Test the model Contact"""

        first_query = Contact.objects.get(id=2)
        self.assertEqual(first_query.name, self.my_instance.name)
        self.assertEqual(first_query.surname, self.my_instance.surname)
        self.assertEqual(first_query.bio, self.my_instance.bio)
        self.assertEqual(first_query.email, self.my_instance.email)
        self.assertEqual(first_query.jabber, self.my_instance.jabber)
        self.assertEqual(first_query.date, self.my_instance.date)
        self.assertEqual(first_query.skype, self.my_instance.skype)
        self.assertEqual(first_query.contacts, self.my_instance.contacts)

    def test_that_data_base_is_not_empty(self):
        """ Test that data base is not empty first objects loads from fixtures and second I made with model_mommy"""

        self.assertIsNot(Contact.objects.all().count(), 0)
        self.assertEqual(Contact.objects.all().count(), 2)
