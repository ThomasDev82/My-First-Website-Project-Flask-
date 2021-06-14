from flask import Flask, render_template

Home = Flask(__name__)


@Home.route("/")
def page():
    return render_template("Home_Template.html", pagetitle="Home")


@Home.route("/about")
def aboutp():
    return render_template("About_Template.html", pagetitle="About")


if __name__ == '__main__':
    Home.run(debug=True, port=2000)
