from flask import Flask, render_template
import json

app = Flask(__name__)

# Load video database
with open("videos.json") as f:
    videos = json.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/profile/<topic>")
def profile(topic):

    # normalize topic
    topic = topic.lower()

    filtered = [
        v for v in videos
        if v["category"].lower().replace(" ", "_") == topic
    ]

    trending = [v for v in filtered if v.get("level") == "trending"]
    beginner = [v for v in filtered if v.get("level") == "beginner"]
    advanced = [v for v in filtered if v.get("level") == "advanced"]
    recommended = [v for v in filtered if v.get("level") == "recommended"]

    return render_template(
        "profile.html",
        topic=topic,
        trending=trending,
        beginner=beginner,
        advanced=advanced,
        recommended=recommended
    )

if __name__ == "__main__":
    app.run(debug=True)