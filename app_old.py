from flask import Flask, render_template


app=Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/pred")
def pred():



    return render_template('index.html')
    # prediction=


if __name__=="__main__":
    app.debug=True
    app.run()