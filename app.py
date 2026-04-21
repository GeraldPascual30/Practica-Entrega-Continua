from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hola DevOps</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: Arial, sans-serif;
            }

            body {
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #0f172a, #1e3a8a, #06b6d4);
                color: white;
            }

            .card {
                background: rgba(255, 255, 255, 0.12);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 40px;
                width: 90%;
                max-width: 600px;
                text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            }

            h1 {
                font-size: 3rem;
                margin-bottom: 15px;
            }

            p {
                font-size: 1.2rem;
                margin-bottom: 20px;
                color: #e2e8f0;
            }

            .badge {
                display: inline-block;
                background: #22c55e;
                color: white;
                padding: 10px 20px;
                border-radius: 999px;
                font-weight: bold;
                margin-bottom: 25px;
            }

            .buttons {
                display: flex;
                justify-content: center;
                gap: 15px;
                flex-wrap: wrap;
                margin-top: 20px;
            }

            a {
                text-decoration: none;
                background: white;
                color: #0f172a;
                padding: 12px 20px;
                border-radius: 12px;
                font-weight: bold;
                transition: 0.3s;
            }

            a:hover {
                background: #e2e8f0;
                transform: scale(1.05);
            }

            .footer {
                margin-top: 25px;
                font-size: 0.95rem;
                color: #cbd5e1;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <div class="badge">Aplicación Activa</div>
            <h1>Hola Mundo 🚀</h1>
            <p>Práctica básica de DevOps con Flask y Docker</p>

            <div class="buttons">
                <a href="/health">Health</a>
                <a href="/info">Info</a>
            </div>

            <div class="footer">
                Desarrollado para demostrar el ciclo básico de DevOps
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return """
    <h1>Estado de la aplicación: OK ✅</h1>
    <p>La aplicación está funcionando correctamente.</p>
    """

@app.route("/info")
def info():
    return """
    <h1>Información de la aplicación</h1>
    <p>Nombre: Hola DevOps</p>
    <p>Versión: 1.0</p>
    <p>Tecnología: Python Flask + Docker</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)