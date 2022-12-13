from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/download', methods=["POST", "GET"])
def download():
   return "Downloading Video"

if __name__ == '__main__':
   app.run(port=80, debug=True)