from django.contrib import admin
from django.apps import apps

models = apps.get_app_config('hrm').get_models()

for model in models:
    class CustomizedAdmin(admin.ModelAdmin):
        list_display = [field.name for field in model._meta.concrete_fields]
        search_fields = [field.name for field in model._meta.concrete_fields]

    admin.site.register(model, CustomizedAdmin)