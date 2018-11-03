from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("main.html")


@app.route("/computerscience", methods=["GET", "POST"])
def computerscience():
    return render_template("computerscience.html")


@app.route("/CScourse", methods=["GET", "POST"])
def CScourse():
    dict = {"intro": ["CSCI051", "CSCI054", "CSCI062"],
            "core": ["CSCI101", "CSCI105", "CSCI140"],
            "electives": ["CSCI124", "CSCI131", "CSCI133", "CSCI151", "CSCI158", "CSCI159", "CSCI181N",
                          "CSCI181Q", "CSCI181R", "CSCI181S", "CSCI192", "CSCI199DR", "CSCI199IR", "CSCI199RA"],
            "math": ["MATH058 or MATH060"]}
    course_list = ["CSCI051", "CSCI054", "CSCI062", "CSCI101", "CSCI105", "CSCI140", "CSCI124", "CSCI131", "CSCI133",
                   "CSCI134", "CSCI151", "CSCI158", "CSCI159", "CSCI181N", "CSCI181Q", "CSCI181R", "CSCI181S",
                   "CSCI192", "CSCI199DR", "CSCI199IR", "CSCI199RA", "MATH058 or MATH060"]
    courses_taken = []
    if request.method == "POST":
        for i in range(1, 23):
            if request.form.get("course" + str(i)):
                courses_taken.append(course_list[i-1])

    intro_needed = ""
    for x in dict["intro"]:
        if x not in courses_taken:
            intro_needed += x + ". "
    if intro_needed == "":
        intro_needed = "None!"

    core_needed = ""
    for x in dict["core"]:
        if x not in courses_taken:
            core_needed += x + ". "
    if core_needed == "":
        core_needed = "None!"

    electives_suggested1 = []
    for x in dict["electives"]:
        if x not in courses_taken:
            electives_suggested1.append(x)
    if len(electives_suggested1) <= len(dict["electives"]) - 3:
        electives_suggested = "None!"
    else:
        electives_suggested = ""
        for item in electives_suggested1:
            electives_suggested += item + ". "

    math_needed = ""
    for x in dict["math"]:
        if x not in courses_taken:
            math_needed += x + ". "
    if math_needed == "":
        math_needed = "None!"

    return render_template("CScourses.html", intro_needed=intro_needed, core_needed=core_needed, electives_suggested=electives_suggested, math_needed=math_needed)


@app.route("/dance", methods=["GET", "POST"])
def dance():
    return render_template("dance.html")


@app.route("/DANCEcourses", methods=["GET", "POST"])
def DANCEcourses():
    dict = {"modern_dance": ["DANC010", "DANC050", "DANC120", "DANC122"],
            "ballet": ["DANC012", "DANC051", "DANC123", "DANC124"],
            "core": ["DANC135", "DANC130", "DANC140", "DANC160"],
            "electives": ['DANC013',
                           'DANC136', 'DANC137', 'DANC138', 'DANC139', 'DANC141', 'DANC150', 'DANC151', 'DANC152',
                           'DANC166', 'DANC170', 'DANC175', 'DANC176', 'DANC180',
                           'DANC181', 'DANC192', 'THEA052', "THEA024"]}
    course_list = ["DANC010", "DANC050", "DANC120", "DANC122", "DANC012", "DANC051", "DANC123", "DANC124", "DANC135", "DANC130",
                    "DANC14O", "DANC160", "DANC192", "DANC180", "DANC181", "THEA023", "THEA024", "THEA002", "MUS065", "DANC150",
                    "DANC151", "DANC152", "THEA052", "DANC166", "DANC170", "DANC175"]

    courses_taken = []
    if request.method == "POST":
        for i in range(1, 27):
            if request.form.get("course" + str(i)):
                courses_taken.append(course_list[i-1])

    md_needed = ""
    for x in dict["modern_dance"]:
        if x in courses_taken:
            md_needed = "None!"
        else:
            md_needed += x + ". "

    ballet_needed = ""
    for x in dict["ballet"]:
        if x in courses_taken:
            ballet_needed = "None!"
        else:
            ballet_needed += x + ". "

    core_needed = ""
    for x in dict["core"]:
        if x not in courses_taken:
            core_needed += x + ". "
    if core_needed == "":
        core_needed = "None!"

    electives_suggested1 = []
    for x in dict["electives"]:
        if x not in courses_taken:
            electives_suggested1.append(x)
    if len(electives_suggested1) <= len(dict["electives"]) - 3:
        electives_suggested = "None!"
    else:
        electives_suggested = ""
        for item in electives_suggested1:
            electives_suggested += item + ". "

    return render_template("DANCEcourses.html", md_needed=md_needed, ballet_needed=ballet_needed, core_needed=core_needed, electives_suggested=electives_suggested)


if __name__ == "__main__":
    app.run(debug=True)
