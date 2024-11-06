from django.db import models


class Achievement(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Step(models.Model):
    achievement = models.ForeignKey(
        Achievement,
        on_delete=models.CASCADE,
        related_name="steps",
        db_index=True,
        null=True,
        blank=True,
    )

    step_description = models.CharField(max_length=255)

    def __str__(self):
        return self.step_description


class Milestones(models.Model):
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(null=True, blank=True)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)

    class Meta:
        ordering = ["order"]
        unique_together = ("order", "achievement")

    def __str__(self):
        return f"{self.achievement} - Step {self.order}"
