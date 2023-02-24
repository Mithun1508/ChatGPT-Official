import openai
import os
from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)
openai.api_key = os.environ['APIKEY']
model_engine = "text-curie-001" 

@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		prompt = request.form["prompt"]
		completion = openai.Completion.create(
		 engine=model_engine,
		 prompt=prompt,
		 max_tokens=1000, 
		 n=1,
		 stop=None,
		 temperature=0.5,
		)
		response = completion.choices[0].text
		return response
	return render_template('index.html')


@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers',
	                     'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods',
	                     'GET,PUT,POST,DELETE,OPTIONS')
	return response


@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'),
	                           'favicon.png',
	                           mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
	app.debug = False 
	app.run(host='0.0.0.0', port=443)
