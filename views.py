from flask import Flask, render_template, request
import markov

views = Flask(__name__)

@app.route("/", methods=['GET'])
def landing_page():
    return render_template('template.html')

@app.route("/", methods=['POST'])
def submit():
    their_input = request.form['input']
    print "POST"
    # print their_input
    foo = markov.main(their_input)
    return render_template('template.html', my_string=foo)
    # return my_string

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)