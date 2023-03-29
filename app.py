from flask import Flask, render_template

app = Flask(__name__)


# home
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/video1')
def video1():
    return render_template("video1.html")


# js stuff
@app.route('/js/101-resources')
def js_1():
    return render_template("page1.html")
@app.route('/js/101-basics')
def js_2(): 
    return render_template("page3.html")

@app.route('/js/101-js-in-100-seconds')
def js_3(): 
    return render_template("page2.html")
@app.route('/js/102-prototype-chain')
def js_4(): 
    return render_template("page4.html")
@app.route('/js/102-destructuring')
def js_5(): 
    return render_template("page5.html")
@app.route('/js/102-spread')
def js_6(): 
    return render_template("page6.html")
@app.route('/js/102-optional-chaining')
def js_7(): 
    return render_template("page7.html")
@app.route('/js/102-nullish-coalescing')
def js_8(): 
    return render_template("page8.html")
@app.route('/js/102-higher-order-functions')
def js_9(): 
    return render_template("page9.html")
@app.route('/js/102-closures')
def js_10(): 
    return render_template("page10.html")
@app.route('/js/102-array-tricks')
def js_11(): 
    return render_template("page11.html")
@app.route('/js/102-history-of-js')
def js_12(): 
    return render_template("page12.html")
@app.route('/js/algo-sum')
def js_13(): 
    return render_template("page13.html")
@app.route('/js/algo-binary-search')
def js_14(): 
    return render_template("page14.html")
@app.route('/js/algo-lru')
def js_15(): 
    return render_template("page15.html")
@app.route('/js/algo-vitest')
def js_16(): 
    return render_template("page16.html")
@app.route('/js/app-setup')
def js_17(): 
    return render_template("page17.html")
@app.route('/js/app-rest')
def js_18(): 
    return render_template("page18.html")
@app.route('/js/app-server')
def js_19(): 
    return render_template("page19.html")
@app.route('/js/app-rest-client')
def js_20(): 
    return render_template("page20.html")
@app.route('/js/app-frontend')
def js_21(): 
    return render_template("page21.html")
@app.route('/js/app-loader')
def js_22(): 
    return render_template("page22.html")
@app.route('/js/app-error-handling')
def js_23(): 
    return render_template("page23.html")








if __name__ == "__main__":
    app.run(debug=True)