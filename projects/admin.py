from django.contrib import admin
from projects.models import Project, Training

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    pass

class TrainingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Training, TrainingAdmin)