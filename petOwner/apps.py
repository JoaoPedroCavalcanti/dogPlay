from django.apps import AppConfig


class PetownerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'petOwner'

    def ready(self, *args, **kwargs) -> None:
        import petOwner.signals
        super_ready = super().ready(*args, **kwargs)
        return super_ready