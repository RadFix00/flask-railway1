from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Conectar con PostgreSQL en Railway
DATABASE_URL = os.getenv("postgresql://postgres:NIJVkfPfpktAhDZeumKhPYrxFiBcGzlu@switchyard.proxy.rlwy.net:37801/railway")
conn = psycopg2.connect(DATABASE_URL)

@app.route('/productos')
def get_productos():
    cur = conn.cursor()
    cur.execute("SELECT * FROM productos")  # Asegúrate de tener una tabla 'productos'
    rows = cur.fetchall()
    cur.close()
    
    productos = [{"id": row[0], "nombre": row[1], "precio": row[2]} for row in rows]
    return jsonify(productos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
