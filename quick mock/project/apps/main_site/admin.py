from django.contrib import admin
from main_site.models import DataPoint, Milestone, Sale


class DataPointAdmin(admin.ModelAdmin):
    list_display = (
        "recorded_at", "num_total_users", "num_active_users", "num_authenticated", 
        "num_filled_in_profile", "num_hit_home_page", "num_with_one_class", 
        "num_with_one_buddy", "num_attended_one_event", 
        "num_buddy_requests", "num_buddies", "buddy_ratio",
    )
    model = DataPoint


class MilestoneAdmin(admin.ModelAdmin):
    list_display = ("name", "recorded_at", "type")
    model = Milestone


class SaleAdmin(admin.ModelAdmin):
    list_display = ("name", "recorded_at", "status")
    model = Sale

admin.site.register(Milestone, MilestoneAdmin)
admin.site.register(DataPoint, DataPointAdmin)
admin.site.register(Sale, SaleAdmin)
