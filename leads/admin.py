from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
      # Show useful columns on the list page
    list_display = ("id", "name", "email","country_code", "phone", "business_type", 
                    "created_at", "materials_preview", "message_preview")
    # Make ID and Name clickable to open the full detail page
    list_display_links = ("id", "name")
    # Filters/search to find leads quickly
    list_filter = ("business_type", "created_at")
    search_fields = ("name", "email", "phone", "company_name", "designation", "message")
    # Show fields in this order on the detail page; created_at is read-only
    readonly_fields = ("created_at",)
    fields = ("name", "email", "phone","country_code", "company_name", "designation", "business_type", "materials", "message", "created_at")

    # Nice, compact previews for list page
    def materials_preview(self, obj):
        return ", ".join(obj.materials) if obj.materials else "-"
    materials_preview.short_description = "materials"

    def message_preview(self, obj):
        if not obj.message:
            return "-"
        return (obj.message[:60] + "…") if len(obj.message) > 60 else obj.message
    message_preview.short_description = "message"

