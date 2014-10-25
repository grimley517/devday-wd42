from django.contrib import admin
from donations.models import Campaign, Donations

# Register your models here.
class CampaignAdmin(admin.ModelAdmin):
    pass

class DonationsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Donations, DonationsAdmin)