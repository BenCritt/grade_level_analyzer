from django.shortcuts import render
from .forms import QRForm
import os
import qrcode
from django.http import HttpResponse
from .forms import WeatherForm
import requests
import json
import datetime
from pyzipcode import ZipCodeDatabase
import numpy as np
import matplotlib.pyplot as plt
from .forms import MonteCarloForm
from django.shortcuts import redirect
from django.conf import settings
from .forms import TextForm
import textstat


def grade_level_analyzer(request):
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data["text"]
            results = {
                "flesch_kincaid_grade": textstat.flesch_kincaid_grade(input_text),
                "gunning_fog": textstat.gunning_fog(input_text),
                "coleman_liau_index": textstat.coleman_liau_index(input_text),
            }
            # Calculate the weighted average of the scores
            average_score = round(
                (0.5 * results["flesch_kincaid_grade"])
                + (0.3 * results["gunning_fog"])
                + (0.2 * results["coleman_liau_index"]),
                1,
            )
            # Calculate the uniform average of the scores
            uniform_average_score = round(
                (
                    results["flesch_kincaid_grade"]
                    + results["gunning_fog"]
                    + results["coleman_liau_index"]
                )
                / 3,
                1,
            )
            # Add the average scores to the results dictionary
            results["average_score"] = average_score
            results["uniform_average_score"] = uniform_average_score
            # Define the context with results and form
            context = {"form": form, "results": results}
            return render(request, "projects/grade_level_results.html", context)
        else:
            # Form is not valid, re-render the page with the form
            return render(request, "projects/grade_level_analyzer.html", {"form": form})
    else:
        # GET request, so create a new form and render the page
        form = TextForm()
        return render(request, "projects/grade_level_analyzer.html", {"form": form})
