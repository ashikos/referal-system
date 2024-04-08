from django.contrib import admin
from v1.accounts import models

# Register your models here.

class ProjectUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', "referral")

# Register your models here.


admin.site.register(models.ProjectUser, ProjectUserAdmin)