# -*- coding: utf-8 -*-
from django.test import TestCase
from apps.hello.models import Contact
from model_mommy import mommy

# Create your tests here.


class SomeTestsModel(TestCase):

    def setUp(self):
        self.my_instance = mommy.make('hello.Contact', id=2, name=u'Олег', surname=u'Панчишин')

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

        object_list = Contact.objects.all()
        self.assertTrue(object_list)  # Test that database list is not empty
        self.assertIsNot(Contact.objects.all().count(), 0)
        self.assertEqual(Contact.objects.all().count(), 2)  # Test that base data has saved 2 objects

    def test_the_unicode_in_base(self):
        """Test in case unicode in base data """

        self.assertEqual(self.my_instance.__unicode__(), u'Олег Панчишин')
