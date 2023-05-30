from flask import Blueprint, jsonify

from src.module.cun import download_cun_users


class UserService:

    def __init__(self):
        self.api = Blueprint('app_user', __name__)
        self.api.add_url_rule('/user/<string:_pic_type>/<string:_user_id>', methods=['GET'],
                              view_func=self.download_images_by_userid)

    def download_images_by_userid(self, _pic_type, _user_id):
        print(_pic_type, _user_id, self.api.name)
        # CUN 图片下载
        if 'cun' == _pic_type:
            download_cun_users(_user_id)
        return jsonify({"code": "success"})
