from flask import Flask, render_template, request, redirect
from webex_device_xapi import dial

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def call():
    if request.method == "POST":
        dial()
        return redirect(request.url)
    else:
        return render_template("form.html")


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
