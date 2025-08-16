from flask import Flask, render_template, request
import random

rspapp = Flask(__name__)

RPS = ["Rock", "Paper", "Scissor"]

win = 0
lose = 0
draw = 0

@rspapp.route("/", methods=["GET", "POST"])
def index():
    global win, lose, draw
    result = ""
    if request.method == "POST":
        user_choice = request.form.get("choice")
        rdm = random.choice(RPS)
        
        if user_choice == rdm:
            result = "Draw!"
            draw += 1
        elif (user_choice == "Rock" and rdm == "Scissor") or \
             (user_choice == "Paper" and rdm == "Rock") or \
             (user_choice == "Scissor" and rdm == "Paper"):
            result = "You Won!"
            win += 1
        else:
            result = "You Lost!"
            lose += 1
        
        return render_template("index.html", result=result, rdm=rdm, win=win, lose=lose, draw=draw)
    
    return render_template("index.html", result=result, rdm="", win=win, lose=lose, draw=draw)

if __name__ == "__main__":
    rspapp.run(debug=True)
