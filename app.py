from flask import Flask, render_template, request, jsonify
from detector import features, score, verdict_from_score


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    payload = request.json or {}
    url = payload.get("url") or request.form.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    feature_map = features(url)
    total_score = score(feature_map)
    return jsonify(
        {
            "features": feature_map,
            "score": total_score,
            "verdict": verdict_from_score(total_score),
        }
    )


@app.route("/api/status")
def status():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True)


