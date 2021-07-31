from django.test import TestCase, Client
from django.utils.translation import activate
from django.shortcuts import reverse
from .models import Menu, Header
# Create your tests here.

# the code of second language that you used for your website
# in my case is fa
second_lang = 'fa'


class IndexTest(TestCase):
    def SetUp(self):
        self.client = Client()

    def test_display_menu_index_page(self):
        menu = Menu.objects.create(
            title="menu1", link="https://www.google.com", title_fa='sdsgdsdg')

        activate('en')
        response = self.client.get(reverse('portfolio:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, menu.title)

        activate(second_lang)
        response = self.client.get(reverse('portfolio:index'))
        self.assertContains(response, menu.title_fa)

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

        activate(second_lang)
        response = self.client.get(reverse('portfolio:index'))
        self.assertContains(response, header.first_title_fa)
        self.assertContains(response, header.second_title_fa)
