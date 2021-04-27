from flask import Flask

app = Flask(__name__)

title = '<p style="font-size:100px"> PEPE </p>'
mi_web = """
            <h1>LA WEB DE JERE con h1</h1>
            <h2>LA WEB DE JERE con h2</h2>
            <h3>LA WEB DE JERE con h3</h3>
            <h4>LA WEB DE JERE con h4</h4>
            <h5>LA WEB DE JERE con h5</h5>
            <h6>LA WEB DE JERE con h6</h6>
        """

# funcion que devuelve el path / con la funcion hello_world
@app.route('/')
def hello_world():
    # return 'Hello, World!'
    return title+mi_web
    #devuelvo el titulo y el contenido de la web

if __name__ == '__main__':
    app.run()