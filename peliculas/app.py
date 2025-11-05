from flask import Flask, render_template #Importa la clase Flask y la función render template desde el paquete flask

app = Flask(__name__) # Crea la aplicación Flask; __name__ ayuda a inicializar recursos y plantillas

# Datos de ejemplo para las peliculas:
#Diccionario donde cada clave es una categoría y su valor es una lista de diccionarios (película)
peliculas = {
    "suspenso": [
        {'titulo': 'El silencio de los Inocentes',
        'sinopsis': "Una joven agente del fel busca la ayuda de un asesino encarcelado para atrapar a otro."},
        {'titulo': "Perdida",
        'sinopsis': "Un hombre se convierte en el principal sospechoso cuando su esposa desaparece."},
    ],
    "terror": [
        {'titulo': 'El Exorcista',
        'sinopsis': "Una niña es poseida por una entidad demoniaca."},
        {'titulo': 'Hereditary',
        'sinopsis': 'una familia es atormentada tras la muerte de su matriarca.'},
    ],
    "romance": [
        {'titulo': 'Orgullo y Prejuicio',
        'sinopsis': 'Elizabeth Bennet se enfrenta al arrogante Sr. Darcy en la Inglaterra del siglo XIX.'},
        {'titulo': 'La La Land',
        'sinopsis': "un pianista de jazz y una aspirante a actriz persiguen sus sueños en Los Angeles."},
    ],
    "infantil": [
        {'titulo': 'Toy Story',
        'sinopsis': 'un grupo de juguetes cobra vida cuando su dueño no está.'},
        {'titulo': 'Mi Vecino Totoro',
        'sinopsis': 'Dos hermanas se mudan al campo y se hacen amigas de un espíritu del bosque.'},
    ]
}

@app.route('/') # Define la ruta raíz (http://localhost:5000/)
def index():
    return render_template('index.html') # Renderiza la plantilla templates/index.html para la página principal

@app.route('/suspenso') # Define la ruta /suspenso
def suspenso():
    # Pasa la lista de películas de la categoria 'suspenso' a la plantilla suspenso.html
    return render_template("suspenso.html", peliculas=peliculas["suspenso"])

@app.route('/terror')  # Define la ruta/terror
def terror():
    #Pasa la lista de películas de la categoría 'terror' a la plantilla terror.html
    return render_template('terror.html', peliculas=peliculas['terror'])

@app.route('/romance') #Define la ruta /romance
def romance():
    #Pasa la lista de películas de la categoría 'romance' a la plantilla romance.html
    return render_template('romance.html', peliculas=peliculas['romance'])

@app.route('/infantil') # Define la ruta/infantil
def infantil():
    #Pasa la lista de películas de la categoría 'infantil a la plantilla infantil.html
    return render_template("infantil.html", peliculas=peliculas['infantil'])

if __name__ == '__main__': # comprueba si se ejecuta este archivo directamente (no importado)
    app.run(debug=True) # Inicia el servidor de desarrollo con recarga automática y modo debug activado