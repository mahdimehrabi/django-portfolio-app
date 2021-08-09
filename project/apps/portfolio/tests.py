from django.test import TestCase, Client
from django.utils.translation import activate
from django.shortcuts import reverse
from django.utils.translation import get_language
from django.core import mail
from django.conf import settings
from faicon.fields import Icon
from .models import (Menu, Header, About, Study,
                     Experience, Project, Skill, Social,
                     ContactMessage)

# Create your tests here.

# the code of second language that you used for your website
# in my case is fa
second_lang = 'fa'


class PortfolioTest(TestCase):
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

    def test_aboutme_index_page(self):
        about = About.objects.create(
            text='lorem ipsum this is a fake big text',
            text_fa='fake persian long text')
        activate('en')
        response = self.client.get(reverse('portfolio:index'))
        self.assertContains(response, about.text)

        activate(second_lang)
        response = self.client.get(reverse('portfolio:index'))
        self.assertContains(response, about.text_fa)

    def test_switch_langugage(self):
        activate('en')
        response = self.client.get(
            reverse('portfolio:switch-lang', args=(second_lang,)))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_language(), second_lang)

        response = self.client.get(
            reverse('portfolio:switch-lang', args=('en',)))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_language(), 'en')

    def test_study_index_page(self):
        study = Study.objects.create(university_title='dgsgds',
                                     study_grade='sdggsd',
                                     description='sdggsdsdggsd',
                                     study_duration_date='sdggsdgsd',
                                     university_title_fa='سیلسسیل',
                                     study_grade_fa='لسیلسیلیسگ',
                                     description_fa='سلسیللسی',
                                     study_duration_date_fa='سیبلل')

        activate('en')
        response = self.client.get(reverse('portfolio:index'))
        self.assertContains(response, study.university_title)

        activate(second_lang)
        response = self.client.get(reverse('portfolio:index'))
        self.assertContains(response, study.university_title_fa)

    def test_experience_index_page(self):
        experience = Experience.objects.create(
            employer_name='test_text',
            job_title='test_text',
            description='test_text',
            work_duration_date='test_text',

            employer_name_fa='متن تستی',
            job_title_fa='test_text',
            description_fa='test_text',
            work_duration_date_fa='test_text',
        )
        activate('en')
        response = self.client.get(reverse('portfolio:index'))
        self.assertContains(response, experience.employer_name)

        activate(second_lang)
        response = self.client.get(reverse('portfolio:index'))
        self.assertContains(response, experience.employer_name_fa)

    def test_project_index_page(self):
        project = Project.objects.create(
            title="titasadffassafe", link="https://www.google.com",
            title_fa='شبسبسش', description='dgsgsdgdsgds',
            description_fa='بشبشسبشس',
            image='images/background.jpg')

        activate('en')
        response = self.client.get(reverse('portfolio:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, project.title)

        activate(second_lang)
        response = self.client.get(reverse('portfolio:index'))
        self.assertContains(response, project.title_fa)

    def test_skill_index_page(self):
        skill = Skill.objects.create(
            title="titasadffassafe", title_fa='شبسبسش')

        activate('en')
        response = self.client.get(reverse('portfolio:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, skill.title)

        activate(second_lang)
        response = self.client.get(reverse('portfolio:index'))
        self.assertContains(response, skill.title_fa)

    def test_social_index_page(self):
        social = Social.objects.create(
            link='https://www.test.com',
            icon=Icon("sfasfa", "Safsfasaf", "aaa"))

        response = self.client.get(reverse('portfolio:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, social.link)

    def test_send_meesage(self):
        old_cm_counts = ContactMessage.objects.count()
        response = self.client.post(reverse('portfolio:index'), {
                                    'email': "test@test.com", "message": "text text text"})
        self.assertEqual(response.status_code, 302)

        self.assertEqual(len(mail.outbox), 1)
        self.assertTrue("text text text" in mail.outbox[0].body)
        self.assertTrue(settings.ADMIN_EMAIL in mail.outbox[0].to)
        cm_counts = ContactMessage.objects.count()
        self.assertEqual(old_cm_counts+1, cm_counts)
