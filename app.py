from flask import Flask, render_template, g, request
import sqlite3

# Creates app with file name
app = Flask(__name__)

# Creates a home page
@app.route("/")
def main():
	return render_template("base.html")

# Creates page that lets users submit messages
@app.route("/submit", methods=["POST", "GET"])
def submit():
	# If the page is loaded after submitting a message:
	if request.method == "POST":
		msg = insert_message(request)
		return render_template("submit.html",
			message = msg[0],
			handle = msg[1])

	# If we're just viewing the page and didn't submit a form
	else: # request.method == "GET"
		return render_template("submit.html")

# Creates page that lets users view messages
@app.route("/view", methods=["GET"])
def view():
	msgs = random_message(5)
	return render_template("view.html", msgs=msgs)


def get_message_db():
	# Connect to the db if it is not yet
	if "message_db" not in g:
		g.message_db = sqlite3.connect("messages_db.sqlite")
	cursor = g.message_db.cursor()

	# make the following table if it is not made yet
	cmd = """
	CREATE TABLE IF NOT EXISTS messages
	(id int, message text, handle text)
	"""
	cursor.execute(cmd)
	return g.message_db

def insert_message(request):
	# Gets info from the form submitted once user submits message
	message = request.form["message"]
	handle = request.form["handle"]

	cursor = get_message_db().cursor()
	# Gives each entry a unique id
	row_count = cursor.execute("SELECT COUNT(*)+1 FROM messages;").fetchone()
	cmd = """
	INSERT INTO messages (id, message, handle)
	VALUES (?, ?, ?)
	"""
	cursor.execute(cmd, (row_count[0], message, handle))

	# Make sure the action is committed and saved:
	g.message_db.commit()
	g.message_db.close()

	return [message, handle]


def random_message(n):
	cursor = get_message_db().cursor()

	# Get n random messages and handles from the table
	cmd = """
	SELECT message, handle FROM messages ORDER BY RANDOM() LIMIT ?;
	"""
	info = cursor.execute(cmd, (n,)).fetchall()
	return info

