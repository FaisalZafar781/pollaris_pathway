from django.apps import AppConfig


class InsightsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'insights'

    def ready(self):
        import insights.signals
        from django.contrib.auth import get_user_model
        from django.core.management import call_command
        from django.db.utils import OperationalError
        import os

        User = get_user_model()
        try:
            # Create superuser if it doesn't exist
            if not User.objects.filter(username="admin").exists():
                User.objects.create_superuser("admin", "admin@example.com", "admin123")

            # Load data only once — avoid duplicate loads
            if os.environ.get("RUN_DATA_LOAD_ONCE") != "1":
                call_command('loaddata', 'fixtures/data.json')
                os.environ["RUN_DATA_LOAD_ONCE"] = "1"
        except OperationalError:
            # Database might not be ready during migrations
            pass