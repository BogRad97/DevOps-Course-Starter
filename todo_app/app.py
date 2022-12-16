import flask
from todo_app.data.models.view_model import ViewModel
from todo_app.flask_config import Config
from todo_app.data.todo_service import TodoService
from loggly.handlers import HTTPSHandler
from logging import Formatter
from prometheus_flask_exporter import PrometheusMetrics

def set_logger(app):
    if app.config['LOGGLY_TOKEN'] is not None:
        handler = HTTPSHandler(f'https://logs-01.loggly.com/inputs/{app.config["LOGGLY_TOKEN"]}/tag/todo-app')
        handler.setFormatter(
            Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
        )
        app.logger.addHandler(handler)

def create_app():
    app = flask.Flask(__name__)
    app.config.from_object(Config())
    set_logger(app)
    app.logger.setLevel(app.config['LOG_LEVEL'])
    metrics = PrometheusMetrics(app)
    
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
        app.logger.info(f"Added todo with title: {todo_name}")

        response = flask.redirect('/')
        response.autocorrect_location_header = False

        return response


    @app.route('/remove-todo', methods=["POST"])
    def remove_todo():
        card_id = flask.request.form.get('id')
        todo_service.remove_item(card_id)
        app.logger.info(f'Removed todo with id: {card_id}')

        response = flask.redirect('/')
        response.autocorrect_location_header = False
        
        return response


    @app.route('/move-across', methods=['POST'])
    def move_across():
        card_id = flask.request.form.get('id')
        todo_service.move_across(card_id)
        app.logger.info(f'Moved across todo with id: {card_id}')

        response = flask.redirect('/')
        response.autocorrect_location_header = False

        return response


    @app.route('/move-backwards', methods=['POST'])
    def move_backwards():
        card_id = flask.request.form.get('id')
        todo_service.move_backwards(card_id)
        app.logger.info(f'Moved backwards todo with id: {card_id}')

        response = flask.redirect('/')
        response.autocorrect_location_header = False

        return response
    
    return app

