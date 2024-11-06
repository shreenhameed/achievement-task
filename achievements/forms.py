from django import forms


from .models import Achievement, Step


class CombinedMilestoneForm(forms.Form):
    achievement = forms.ModelChoiceField(
        queryset=Achievement.objects.all(), label="Achievement"
    )
    step = forms.ModelChoiceField(queryset=Step.objects.all(), label="Step")
    order = forms.IntegerField(required=False, label="Order")
