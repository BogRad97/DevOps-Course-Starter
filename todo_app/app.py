import flask
from todo_app.flask_config import Config
import todo_app.data.session_items as si

app = flask.Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    todo_list = si.get_items()
    return flask.templating.render_template("index.html", todo_list=todo_list)

@app.route('/add-todo', methods=["POST"])
def add_todo():
    todo_name = flask.request.form.get('todo_name')
    si.add_item(todo_name)

    response = flask.redirect('/')
    response.autocorrect_location_header = False

    return response

@app.route('/remove-todo', methods=["POST"])
def remove_todo():
    id = flask.request.form.get('id')
    si.remove_item(id)

    response = flask.redirect('/')
    response.autocorrect_location_header = False
    
    return response
