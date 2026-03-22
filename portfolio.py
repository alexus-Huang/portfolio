from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("index.html")

@app.route("/about")
def aboutPage():
    return render_template("about.html")


@app.route("/otherProjectsPage")
def otherProjectsPage():
    return render_template("otherProjects.html")
if __name__ == "__main__":
    app.run(debug=True)
