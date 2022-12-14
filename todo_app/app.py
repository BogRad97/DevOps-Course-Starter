import flask
from todo_app.data.models.view_model import ViewModel
from todo_app.flask_config import Config
from todo_app.data.todo_service import TodoService

def create_app():
    app = flask.Flask(__name__)
    app.config.from_object(Config())
    todo_service = TodoService()


    @app.route('/')
    def index():
        todo_lists = todo_service.get_items()
        view_model = ViewModel(todo_lists)
        return flask.templating.render_template("index.html", view_model=view_model)


    @app.route('/add-todo', methods=["POST"])
    def add_todo():
        todo_name = flask.request.form.get('todo_name')
        todo_service.add_item(todo_name)

        response = flask.redirect('/')
        response.autocorrect_location_header = False

        return response


    @app.route('/remove-todo', methods=["POST"])
    def remove_todo():
        card_id = flask.request.form.get('id')
        todo_service.remove_item(card_id)

        response = flask.redirect('/')
        response.autocorrect_location_header = False
        
        return response


    @app.route('/move-across', methods=['POST'])
    def move_across():
        card_id = flask.request.form.get('id')
        todo_service.move_across(card_id)

        response = flask.redirect('/')
        response.autocorrect_location_header = False

        return response


    @app.route('/move-backwards', methods=['POST'])
    def move_backwards():
        card_id = flask.request.form.get('id')
        todo_service.move_backwards(card_id)

        response = flask.redirect('/')
        response.autocorrect_location_header = False

        return response
    
    return app

