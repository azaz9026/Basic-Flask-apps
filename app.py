## Flask App Routing



from flask import Flask,render_template,request,redirect,url_for

## create a simple flask application

app = Flask(__name__)


@app.route('/' , methods=['GET'])
def welcome():
    
    
    return "Welcome to the Azaz Project of Flask"

@app.route('/index' , methods=['GET'])
def index():
    return "Welcome to the Index Page Project of Flask"


## Variable rule


@app.route('/success/<int:score>')
def success(score):
    return " <h3> The Person has Passed and the Score is :- </h3> " +  str(score)


@app.route('/fail/<int:score>')
def fail(score):
    return " <h3> The Person has Fail and the Score is :- </h3> " + str(score)
    


@app.route('/form' , methods=["GET" , "POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:
        Maths=float(request.form['Maths'])
        Science=float(request.form['Science'])
        History=float(request.form['History'])

        average_marks = (Maths + Science + History)/3

        res=""

        if average_marks >= 50:
            res="success"
        else:
            res="fail"

        return redirect(url_for(res,score=average_marks))
    
  ## return render_template('form.html' , score=average_marks)



if __name__=="__main__":
    app.run(debug=True)

