from django.contrib import admin
from .models import Fillup, Newsletter
import csv
from django.http import HttpResponse


def export_to_csv(modeladmin, request, queryset):
    """
    Custom admin action to export selected records to a CSV file.
    """
    # Get model fields dynamically
    field_names = [field.name for field in modeladmin.model._meta.fields]

    # Create the HTTP response for the CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={modeladmin.model._meta.model_name}_export.csv'

    # Write the CSV
    writer = csv.writer(response)
    writer.writerow(field_names)  # Write header row
    for obj in queryset:
        row = [getattr(obj, field) for field in field_names]
        writer.writerow(row)

    return response

export_to_csv.short_description = "Export selected items to CSV"


class Fillupadmin(admin.ModelAdmin):
    actions = [export_to_csv]
class Newsletteradmin(admin.ModelAdmin):
    actions = [export_to_csv]
admin.site.register(Fillup, Fillupadmin)
admin.site.register(Newsletter, Newsletteradmin)