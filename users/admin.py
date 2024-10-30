from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin): # Admin for managing profiles (through Django)
    list_display = ('user', 'first_name', 'surname', 'nickname')
    search_fields = ('user__username', 'nickname')
    list_filter = ('nickname',)
    
admin.site.register(Profile, ProfileAdmin)