from flask import Flask

from src.service.UserService import UserService
from src.service.WorkService import WorkService

# spider 主入口
if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(UserService().api, url_prefix="/api/v1")
    app.register_blueprint(WorkService().api, url_prefix="/api/v1")
    app.run(port=10000, debug=True)
