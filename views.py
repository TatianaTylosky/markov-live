from flask import Flask, render_template
import markov

app = Flask(__name__)

@app.route("/")
def markov_result():
	# import ipdb; ipdb.set_trace()
	foo = markov.main()
	#print my_string
	print type(foo)
	return render_template('template.html', my_string=foo)
	# return my_string

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)