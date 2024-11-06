from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import CombinedMilestoneForm
from django.db.models import Count

from .models import (
    Achievement,
    Milestones,
    Step,
)


def success(request):
    return render(request, "achievements/success.html")


def add_milestone_with_achievement(request):

    achievement_id = request.GET.get("achievement_id")
    achievements_with_milestones = (
        Achievement.objects.annotate(milestones_count=Count("milestones"))
        .filter(milestones_count__gt=0)
        .prefetch_related("milestones_set")
    )

    if request.method == "POST":
        form = CombinedMilestoneForm(request.POST)
        if form.is_valid():
            print("asfgasasfafs in", form.cleaned_data)

            try:

                ext = Milestones.objects.filter(
                    step=form.cleaned_data["step"],
                    achievement=form.cleaned_data["achievement"],
                ).first()  # 15
                ext_order = Milestones.objects.filter(
                    achievement=form.cleaned_data["achievement"],
                    order=form.cleaned_data["order"],
                ).first()  # 1
                if ext_order is not None:

                    ext.step = ext_order.step
                    ext.save()

                Milestones.objects.update_or_create(
                    order=form.cleaned_data[
                        "order"
                    ],  # Include 'order' in the lookup fields
                    achievement=form.cleaned_data[
                        "achievement"
                    ],  # Additional lookup field
                    defaults={
                        "step": form.cleaned_data["step"],  # Fields to update or create
                        "order": form.cleaned_data["order"],
                        "achievement": form.cleaned_data["achievement"],
                    },
                )
                return redirect(
                    "add_milestone_with_achievement"
                )  # Redirect to a success page or another appropriate page
            except Exception as error:
                print("dsfsdfsdf", error)

                if (
                    str(error)
                    == "UNIQUE constraint failed: achievements_milestones.order, achievements_milestones.achievement_id"
                ):
                    error = "Same order could not be repeated with the achievement."
                return render(
                    request,
                    "achievements/add_milestone_with_achievement.html",
                    {
                        "form": form,
                        "error": error,
                        "achievements_with_milestones": achievements_with_milestones,
                    },
                )
    else:
        form = CombinedMilestoneForm()
        error = "nothing to add"

    return render(
        request,
        "achievements/add_milestone_with_achievement.html",
        {
            "form": form,
            "achievements_with_milestones": achievements_with_milestones,
        },
    )


def load_steps(request):
    achievement_id = request.GET.get("achievement_id")

    steps = Step.objects.filter(achievement_id=achievement_id).values(
        "id", "step_description"
    )
    return JsonResponse(list(steps), safe=False)
