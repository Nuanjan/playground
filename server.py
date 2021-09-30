from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)	# notice the 2 new named arguments!
@app.route('/play')
def play():
    return render_template("play.html")

@app.route('/play/<x>')
def playNum(x):
    return render_template("playNum.html", x=int(x))
@app.route('/play/<x>/<color>')
def playNumAndColor(x, color):
    print(color)
    return render_template("playNumAndColor.html", x=int(x),color=color)
if __name__=="__main__":
    app.run(debug=True)

