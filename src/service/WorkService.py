from flask import Blueprint, jsonify

from src.module.cun import download_cun_works


class WorkService:

    def __init__(self):
        self.api = Blueprint('app_work', __name__)
        self.api.add_url_rule('/work/<string:_pic_type>/<string:_work_id>', methods=['GET'],
                              view_func=self.download_images_by_workid)

    def download_images_by_workid(self, _pic_type, _work_id):
        print(_pic_type, _work_id, self.api.name)
        if 'cun' == _pic_type:
            download_cun_works(_work_id)
        return jsonify({"code": "success", "message": ""})
