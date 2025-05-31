from flask import Flask, render_template, abort, url_for

app = Flask(__name__)

# Example data for some Indian states
states = {
    "Karnataka": {
        "description": "Karnataka is known for its rich heritage, beautiful landscapes, and the city of Bengaluru.",
        "image": "karnataka.jpg"
    },
    "Maharashtra": {
        "description": "Maharashtra is famous for Mumbai, the financial capital of India, and its vibrant culture.",
        "image": "maharashtra.jpg"
    },
    "Tamil Nadu": {
        "description": "Tamil Nadu is renowned for its Dravidian-style Hindu temples and classical arts.",
        "image": "tamilnadu.jpg"
    },
    "Kerala": {
        "description": "Kerala is called 'God's Own Country' and is famous for its backwaters and natural beauty.",
        "image": "kerala.jpg"
    },
    "West Bengal": {
        "description": "West Bengal is known for its literature, art, and the city of Kolkata.",
        "image": "westbengal.jpg"
    }
}

@app.route("/")
def home():
    return render_template("home.html", states=states)

@app.route("/state/<name>")
def state_page(name):
    name = name.replace("-", " ").title()
    state = states.get(name)
    if not state:
        abort(404)
    return render_template("state.html", name=name, description=state["description"], image=state["image"])

#main code segment
if __name__ == "__main__":
    app.run(debug=True)