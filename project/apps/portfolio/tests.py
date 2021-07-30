from django.test import TestCase, Client
from django.utils.translation import activate
from django.shortcuts import reverse
from .models import Menu, Header
# Create your tests here.


class IndexTest(TestCase):
    def SetUp(self):
        self.client = Client()

    def test_display_menu_index_page(self):
        menu = Menu.objects.create(
            title="menu1", link="https://www.google.com")

        activate('en')
        response = self.client.get(reverse('portfolio:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, menu.title)

    def test_display_header_index_page(self):
        header = Header.objects.create(
            first_title='gdsgds', first_title_fa='sdg',
            second_title="Gdssgd", second_title_fa='gdgsgsdgdsc',
            background='images/background.jpg')

        activate('en')
        response = self.client.get(reverse('portfolio:index'))
        self.assertContains(response, header.first_title)
        self.assertContains(response, header.second_title)
        self.assertContains(response, header.background)
