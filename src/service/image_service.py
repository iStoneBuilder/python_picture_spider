from flask import Blueprint, jsonify

from src.module.cun import download_cun_users, download_cun_works
from src.module.tuchong import download_tuchong_users, download_tuchong_works


class ImageService:

    def __init__(self):
        self.api = Blueprint('image_service', __name__)
        self.api.add_url_rule('/user/<string:_pic_type>/<string:_user_id>', methods=['GET'],
                              view_func=self.download_images_by_userid)
        self.api.add_url_rule('/work/<string:_pic_type>/<string:_work_id>', methods=['GET'],
                              view_func=self.download_images_by_workid)

    def download_images_by_userid(self, _pic_type, _user_id):
        print(_pic_type, _user_id, self.api.name)
        # CUN 图片下载
        if 'cun' == _pic_type:
            download_cun_users(_user_id)
        elif 'tuchong' == _pic_type:
            download_tuchong_users(_user_id)
        return jsonify({"code": "success"})

    def download_images_by_workid(self, _pic_type, _work_id):
        print(_pic_type, _work_id, self.api.name)
        if 'cun' == _pic_type:
            download_cun_works(_work_id)
        elif 'tuchong' == _pic_type:
            download_tuchong_works(_work_id)
        return jsonify({"code": "success", "message": ""})
