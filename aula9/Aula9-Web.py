from flask import Flask


app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')
app.run()