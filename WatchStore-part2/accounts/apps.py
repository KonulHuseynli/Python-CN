#Applari tanimaq ucundur(Settings fayli app-sa gore taniyir)
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    
    def ready(self) -> None:
        from accounts import signals



