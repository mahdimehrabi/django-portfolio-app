from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project.apps.portfolio'

    def ready(self):
        import project.apps.portfolio.signals
