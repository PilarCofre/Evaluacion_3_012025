from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/calculonotas', methods=['GET', 'POST'])
def calculoNotas():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])
        resultadoNotas = nota1 + nota2 + nota3
        promedio = round(resultadoNotas / 3, 2)

        if asistencia >= 75 and promedio >= 4.0:
           resultadoFinal = "APROBO"

        else:
             resultadoFinal = "REPROBO"
        
        return render_template('calculonotas.html', promedio=promedio,resultadoFinal=resultadoFinal)

    return render_template('calculonotas.html')



@app.route ('/calculonombres', methods=['GET', 'POST'])
def largo_nombres():
    if request.method == 'POST':
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])

        nombres = [nombre1, nombre2, nombre3]
        nombre_largo = max(nombres, key=len)
        largo = len(nombre_largo)

   ## return nombre_largo, len(nombre_largo)
        return render_template('calculonombres.html',largo=largo, nombre_largo=nombre_largo)
    return render_template('calculonombres.html')


if __name__ == '__main__':
    app.run(debug=True)