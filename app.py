'''from flask import Flask, render_template

app = Flask(__name__)





@app.route("/")

def home():

    return render_template('home.html')





if __name__ == '__main__':

    app.run(debug=True)'''
from flask import Flask, render_template 
 
app = Flask(__name__) 
 
@app.route('/')
def home():
    return render_template("index.html")
    return "Hey there,this is Thanh's website"
@app.route('/about-me')
def about():
    return render_template('about.html')
@app.route('/introduction')
def WordSection1():
    return render_template('home.html')
@app.route('/feedback')
def feedback():
    return render_template('feedback.html')
@app.route('/test')
def test():
    return render_template('first embed.html')
@app.route('/newapp')
def app():
    return render_template('myapp.html')
 
if __name__ == '__main__': app.run(debug=True) 
 
