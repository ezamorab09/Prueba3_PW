from flask import Flask
from flask import render_template, request



app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/Ejercicio1', methods=['GET', 'POST'])
def promedionotas():
    if request.method == 'POST':
        num1 = float(request.form['numero1'])
        num2 = float(request.form['numero2'])
        num3 = float(request.form['numero3'])
        num = [num1, num2, num3]
        prom = sum(num) / len(num)

        if not (10 <= num1 <= 70) or not (10 <= num2 <= 70) or not (10 <= num3 <= 70):
            return render_template('Ejercicio1.html', mensaje_rango="Las notas deben estar en el rango de 10 a 70")

        asistencia_val = float(request.form.get('asistencia', 0))

        if not (0 <= asistencia_val <= 100):
            return render_template('Ejercicio1.html', mensaje_rango="La asistencia debe estar en el rango de 0 a 100")

        if prom >= 40 and asistencia_val >= 75:
            mensaje = "Aprobado"
        else:
            mensaje = "Reprobado"

        return render_template('Ejercicio1.html', prom=prom, asistencia=asistencia_val, mensaje=mensaje)
    return render_template('Ejercicio1.html')

@app.route('/Ejercicio2', methods=['GET', 'POST'])
def procesar_nombres():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        if not nombre1.isalpha() or not nombre2.isalpha() or not nombre3.isalpha():
            mensaje_error = "los nombres solo deben contener letras"
            return render_template('Ejercicio2.html', mensaje_error=mensaje_error)

        if not nombre1 or not nombre2 or not nombre3:
            mensaje_error = "por favor complete todos los campos"
            return render_template('Ejercicio2.html', mensaje_error=mensaje_error)

        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        longitud_nombre_mas_largo = len(nombre_mas_largo)

        return render_template('Ejercicio2.html', nombre_mas_largo=nombre_mas_largo, longitud_nombre_mas_largo=longitud_nombre_mas_largo)
    return render_template('Ejercicio2.html')

if __name__ == '__main__':

    app.run(debug=True)