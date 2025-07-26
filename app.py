from flask import Flask, jsonify
import os
from dotenv import load_dotenv
import psycopg
from psycopg import sql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
load_dotenv()

def select_table(table_name):
    # 使用 with 確保連線關閉
    with psycopg.connect(os.getenv("DATABASE_URL")) as conn:
        with conn.cursor() as cur:
            query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
            cur.execute(query)
            rows = cur.fetchall()
    return rows

@app.route("/")
def index():
    return """
<ul>
<li><a href="/article">article</a></li>
<li><a href="/bank">bank</a></li>
<li><a href="/cloud">cloud</a></li>
<li><a href="/experience">experience</a></li>
<li><a href="/article">article</a></li>
<li><a href="/food">food</a></li>
<li><a href="/host">host</a></li>
<li><a href="/inventory">inventory</a></li>
<li><a href="/mail">mail</a></li>
<li><a href="/member">member</a></li>
<li><a href="/routine">routine</a></li>
<li><a href="/subscription">subscription</a></li>
<li><a href="/video">video</a></li>
<ul>

"""

@app.route("/<table_name>")
def get_table(table_name):
    try:
        rows = select_table(table_name)
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)