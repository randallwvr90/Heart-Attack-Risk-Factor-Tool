from flask import Flask, render_template,request
# import model


app=Flask(__name__)


@app.route("/")
# , method=["POST"]
def prediction():
    # if request.method=="POST":
    #     prediction=

    return render_template('index.html')



if __name__=="__main__":
    app.debug=True
    app.run()