from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Render the home page using the HTML5 template."""
    selected_items = request.args.getlist('items') if request.args else []

    # Map Czech item names to static image filenames (located in static/images)
    mapping = {
        'svíčky': 'images/candles.png',
        'koule': 'images/balls.png',
        'řetěz': 'images/chain.png',
    }

    overlay_files = [mapping[item] for item in selected_items if item in mapping]

    return render_template(
        "index.html",
        page_title="Domů",
        current_year=datetime.now().year,
        selected_items=selected_items,
        overlay_files=overlay_files,
    )


if __name__ == "__main__":
    app.run(debug=True)
