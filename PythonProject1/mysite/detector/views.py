# detector/views.py
from django.shortcuts import render
from .utils import heuristic_predict

def home(request):
    result = None
    features = None
    score = None

    if request.method == "POST":
        domain = request.POST.get("domain")
        if domain:
            label, feats, s = heuristic_predict(domain)
            result = "Suspicious / Scam" if label == 1 else "Likely Safe"
            features = feats
            score = s

    return render(request, "detector/home.html", {
        "result": result,
        "features": features,
        "score": score,
    })
