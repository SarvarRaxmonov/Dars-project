from django.apps import AppConfig


class bulimConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bulim'
    
    def ready(self):
        import bulim.signals
