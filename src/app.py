from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('principal.html')

@app.route('/acercade')
def about():     
    return render_template('acercade.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/historia')
def historia():
    return render_template('historia.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True) 
