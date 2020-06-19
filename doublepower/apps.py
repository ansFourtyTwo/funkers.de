from django.apps import AppConfig


class DoublepowerConfig(AppConfig):
    name = 'doublepower'

    def ready(self):
        import doublepower.signals  # noqa
