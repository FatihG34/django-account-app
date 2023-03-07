from django.apps import AppConfig


class UseraccountConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "userAccount"

    def ready(self) -> None:
        import userAccount.api.signals
