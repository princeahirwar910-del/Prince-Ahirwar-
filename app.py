from flask import Flask, render_template

app = Flask(__name__)

# Ye route home page ko render karega
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Local testing ke liye debug=True rakhein
    app.run(debug=True)
  
