from flask import Flask, render_template, redirect, request, url_for
import os

app = Flask(__name__)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["Name"]
        return redirect(url_for("session", name=user))
    if request.method == "GET":
        user = request.args.get("Name")
        return redirect(url_for("session", name=user))


@app.route("/hello")
def hello():
    path = False
    returned_string = ""
    if not path:
        path = "/home/ersinerdogan/Downloads/metabolitics-master/metabolitics/datasets/naming/"

    main_dict = {}
    for file in os.listdir(path):
        f = open(path + file, "r")
        if file != "toy-mapping.json":
            for pair in f.read()[1:-1].split(", "):
                key, value = pair.split('": "')
                id, name = key[1:], value[:-1]

                if name in main_dict:
                    main_dict[name].append(id)
                else:
                    main_dict[name] = [id]

    for item in main_dict:
        matches = ""
        for match in main_dict[item]:
            matches += match + " - "
        returned_string += item + "----------->" + matches[:-3] + ""

    return render_template(returned_string)


@app.route("/session/<Name>")
def session(Name):
    return "Welcome %s" % Name


if __name__ == '__main__':
    app.run(debug=True)
