from django.test import TestCase, Client
from django.shortcuts import reverse
from .models import Menu
# Create your tests here.


class MenuTest(TestCase):
    def SetUp(self):
        self.client = Client()

    def test_index_page(self):
        menu = Menu.objects.create(
            title="menu1", link="https://www.google.com")
        response = self.client.get(reverse('portfolio:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, menu.title)
