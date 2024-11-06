from django.contrib import admin
from .models import (
    Achievement,
    Step,
    Milestones,
)


@admin.register(Achievement)
class AdminAchievement(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Step)
class AdminStep(admin.ModelAdmin):
    list_display = ["achievement", "step_description"]


@admin.register(Milestones)
class AdminMilestones(admin.ModelAdmin):
    list_display = ["order", "achievement", "step"]
