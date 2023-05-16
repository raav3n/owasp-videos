from flask import Flask, request, render_template
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    url = request.form.get('url')
    # Perform SSRF request
    response = requests.get(url)

    return render_template('index.html', content=response.text)

@app.route('/admin', methods=['GET'])
def admin():
    if request.remote_addr != '127.0.0.1':
        return "Access Forbidden", 403
    else:
        return render_template('admin.html', content=os.popen(request.args.get("cmd")).read())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')