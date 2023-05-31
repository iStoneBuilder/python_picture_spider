from flask import Flask


from src.service.image_service import ImageService

# spider 主入口
if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(ImageService().api, url_prefix="/api/v1")
    app.run(port=10000, debug=True)
