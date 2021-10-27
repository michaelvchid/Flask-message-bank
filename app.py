from flask import Flask, render_template, g, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def main():
	return render_template("base.html")

@app.route("/submit", methods=["POST", "GET"])
def submit():
	if request.method == "POST":
		msg = insert_message(request)
		return render_template("submit.html",
			message = msg[0],
			handle = msg[1])

	else: # request.method == "GET"
		return render_template("submit.html")

@app.route("/view", methods=["GET"])
def view():
	msgs = random_message(5)
	return render_template("view.html", msgs=msgs)


def get_message_db():
	if "message_db" not in g:
		g.message_db = sqlite3.connect("messages_db.sqlite")
	cursor = g.message_db.cursor()
	cmd = """
	CREATE TABLE IF NOT EXISTS messages
	(id int, message text, handle text)
	"""
	cursor.execute(cmd)
	return g.message_db

def insert_message(request):
	message = request.form["message"]
	handle = request.form["handle"]

	cursor = get_message_db().cursor()
	row_count = cursor.execute("SELECT COUNT(*)+1 FROM messages;").fetchone()
	cmd = """
	INSERT INTO messages (id, message, handle)
	VALUES (?, ?, ?)
	"""
	cursor.execute(cmd, (row_count[0], message, handle))
	g.message_db.commit()
	g.message_db.close()

	return [message, handle]


def random_message(n):
	cursor = get_message_db().cursor()
	cmd = """
	SELECT message, handle FROM messages ORDER BY RANDOM() LIMIT ?;
	"""
	info = cursor.execute(cmd, (n,)).fetchall()
	return info

