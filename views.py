# This is the code for the Grade Level Analyzer.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def grade_level_analyzer(request):
    # Check if the request method is POST.
    if request.method == "POST":
        # Initialize the form with data from the request.
        form = TextForm(request.POST)
        # Validate the form.
        if form.is_valid():
            # Extract the input text from the form.
            input_text = form.cleaned_data["text"]
            # Calculate readability scores using different indices.
            results = {
                "flesch_kincaid_grade": textstat.flesch_kincaid_grade(input_text),
                "gunning_fog": textstat.gunning_fog(input_text),
                "coleman_liau_index": textstat.coleman_liau_index(input_text),
            }
            # Calculate the weighted average of the scores.
            average_score = round(
                (0.5 * results["flesch_kincaid_grade"])
                + (0.3 * results["gunning_fog"])
                + (0.2 * results["coleman_liau_index"]),
                1,
            )
            # Calculate the uniform average of the scores.
            uniform_average_score = round(
                (
                    results["flesch_kincaid_grade"]
                    + results["gunning_fog"]
                    + results["coleman_liau_index"]
                )
                / 3,
                1,
            )
            # Add the calculated scores to the results dictionary.
            results["average_score"] = average_score
            results["uniform_average_score"] = uniform_average_score
            # Prepare the context with the form and results for rendering.
            context = {"form": form, "results": results}
            # Render the results page with the context.
            return render(request, "projects/grade_level_results.html", context)
        else:
            # If the form is invalid, re-render the page with the form.
            return render(request, "projects/grade_level_analyzer.html", {"form": form})
    else:
        # If the request is not POST, create a new form and render the page.
        form = TextForm()
        return render(request, "projects/grade_level_analyzer.html", {"form": form})
