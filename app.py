from flask import Flask, render_template, request

app = Flask(__name__)

movies = {
    "Action": ["John Wick", "Mad Max", "The Dark Knight"],
    "Comedy": ["3 Idiots", "The Hangover", "Home Alone"],
    "SciFi": ["Interstellar", "Inception", "Avatar"],
    "Romance": ["Titanic", "The Notebook", "La La Land"]
}

@app.route("/", methods=["GET","POST"])
def index():
    recommended = []

    if request.method == "POST":
        genre = request.form["genre"]
        if genre in movies:
            recommended = movies[genre]

    return render_template("index.html", movies=recommended)

if __name__ == "__main__":
    app.run(debug=True)