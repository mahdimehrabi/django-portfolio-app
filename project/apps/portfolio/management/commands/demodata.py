from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from project.apps.portfolio.models import (Header, HeaderButton, About, Experience,
                                           Project, Social, Skill, Study, Menu)


class Command(BaseCommand):
    help = "Add demo data to site"

    def handle(self, *args, **options):
        Menu.objects.create(title='About', title_fa='درباره من', link='#about')
        Menu.objects.create(title='Experience',
                            title_fa='سوابق کاری', link='#experience')
        Menu.objects.create(
            title='Projects', title_fa='پروژه ها', link='#projects')
        Menu.objects.create(title='Education',
                            title_fa='تحصیلات', link='#education')
        Menu.objects.create(
            title='Skills', title_fa='مهارت ها', link='#skills')
        Menu.objects.create(title='Contact me',
                            title_fa='تماس بامن', link='#contact')

        header = Header.objects.create(first_title='mahdi mehrabi', first_title_fa='مهدی مهرابی',
                                       second_title='software developer', second_title_fa='توسعه دهنده نرم افزار',
                                       background='images/bg.jpg')

        HeaderButton.objects.create(title='My stackoverflow', title_fa='استک اورفلوی من',
                                    link='https://stackoverflow.com/users/10053470/mahdi-mehrabi',
                                    Header=header
                                    )
        HeaderButton.objects.create(
            title='My github', title_fa='گیت هاب من',
            link='https://github.com/mahdimehrabi',
            Header=header
        )

        About.objects.create(
            text='Iam an iranain software developer, I have good experience with python, django and javascript,\
            and I have passion for learning specially topics that related to Blockchain, AI and bigdata , I born in year 2000\
            and this is my phone number +989120401761 you can contact me in whatsapp',
            text_fa='من یک برنامه نویسم که تجربه و مهارت خوبی با پایتون , جنگو و جاوا اسکریپت داره و عاشق یادگیریه \
             همچنین من عاشق بلاک چین و هوش مصنوعی ام , من متولد بهمن 78 هستم و این شماره موبایل منه 09120401761 توی واتس اپ در خدمتتون هستم'
        )

        Study.objects.create(
            description='I achieved high school diploma at abas pour high school',
            description_fa='من دیپلمم رو در دبیرستان عباس پور گرفتم',
            university_title='abbaspor highschool',
            university_title_fa='دبیرستان عباس پور',
            study_grade='high school',
            study_grade_fa='دبیرستان',
            study_duration_date='2014 - 2017',
            study_duration_date_fa='1393 - 1396'
        )

        Project.objects.create(
            title='website of community of medical knowledge base companies',
            title_fa='انجمن شرکت های دانش بنیان حوزه سلامت',
            link='http://hsbca.ir/',
            description='Developing website of community of medical knowledge base companies ',
            description_fa='توسعه انجمن شرکت های دانش بنیان حوزه استخدام استان تهران',
            image='images/bg.jpg'
        )

        Project.objects.create(title='سامانه استخدام دیجی بنیان',
                               title_fa='medical job finder website',
                               link='http://digibonyan.com/es/',
                               description='this is a job finder website for medical companies',
                               description_fa='وبسایت استخدامی دیجی بنیان کدنویسی اختصاصی بک اند و فرانت اند',
                               image='images/bg.jpg'
                               )
        Skill.objects.create(title='Python')
        Skill.objects.create(title='Django')
        Skill.objects.create(title='Javascript')
        Skill.objects.create(title='react')
        Skill.objects.create(title='react native')

        #todo: add socials
