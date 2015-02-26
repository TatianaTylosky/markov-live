from flask import Flask, render_template, request
import markov

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        # session['username'] = request.form['username']
        input = request.form['input']
        print "POST"
        return "the actual input"
    return "input function ran"

def output():
	# import ipdb; ipdb.set_trace()
	foo = markov.main()
	#print my_string
	print type(foo)
	return render_template('template.html', my_string=foo)
	# return my_string

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)