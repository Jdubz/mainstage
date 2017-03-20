from flask import Flask, url_for
app = Flask(__name__,  static_url_path='/static')

@app.route('/')
def index():
  url_for('static', filename='style.css')
  url_for('static', filename='bundle.js')
  return app.send_static_file('index.html')

if __name__ == "__main__":
  app.run()