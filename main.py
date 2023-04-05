from replit import web
import flask
app = flask.Flask(__name__)

users = web.UserStore()

@app.route("/")
@web.authenticated
def index():
  hits = users.current.get("hits", 0) + 1
  users.current["hits"] = hits
  return f"You've visited {hits} times!"

web.run(app)  