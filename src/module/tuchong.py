""""
https://tuchong.com/rest/2/sites/1317325/posts?count=20&page=1
https://tuchong.com/rest/posts/116788760
"""
import json

from src.baseutil.irequests import request_context, download_images

server = "https://tuchong.com"


def _tuchong_works_data(_works_data):
    _tuchong_status = ''
    # 图片数组
    _works_imgs = _works_data['images']
    # 组图名称
    _works_title = _works_data['title']
    # 存储数据文件夹
    _works_folder = f'/user_{_works_data["author_id"]}'
    # 判断是否有数据
    if len(_works_imgs) > 0:
        print(
            f'========== ✅图组数据下载开始!   users_id: {_works_data["author_id"]} | works_id: {_works_data["post_id"]} ｜ '
            f'works_title: {_works_title}')
        _new_file_index = 1000000000
        # 循环处理数据
        for index, _i_works_data in enumerate(_works_imgs):
            # 生成新文件名
            _new_file_name = f'{_works_data["post_id"]}_{_new_file_index + index + 1}.jpg'
            # 处理新名字
            _new_file_name = _new_file_name.replace("_100000", "_")
            # 下载文件链接
            _file_download_uri = f'https://photo.tuchong.com/{_works_data["author_id"]}/f/{_i_works_data["img_id"]}.jpg'
            # 开始下载文件
            _tuchong_status = download_images("cun" + _works_folder, _file_download_uri, _new_file_name)
            if _tuchong_status == 'exist':
                print(
                    f'========== 跳过下载,文件组已存在! users_id: {_works_data["author_id"]} | works_id: {_works_data["post_id"]} ｜ works_title: {_works_title}')
    return _tuchong_status


# 组图
def _tuchong_works(_work_id):
    _work_uri = server + f'/rest/posts/{_work_id}'
    # 获取组图数据
    _works_data = request_context(_work_uri, None, 'json')
    # 处理post_id
    _works_data['post_id'] = _work_id
    _works_data['author_id'] = _works_data['post']['author_id']
    _works_data['title'] = _works_data['post']['title']
    # 下载组图数据
    return _tuchong_works_data(_works_data)


# 用户
def _tuchong_users(_users_id):
    print(f'========== ✅关注用户数据处理!开始 users_id: {_users_id}')
    # 下载链接
    _users_uri = f'{server}/rest/2/sites/{_users_id}/posts?count=20&page='
    _users_index = 1
    # 获取网站内容
    _users_datas = request_context(f"{_users_uri}{_users_index}", None, 'json')
    # 获取所有组
    _group_datas = _users_datas['post_list']
    if len(_group_datas) == 0:
        print(f'========== ✅没有找到用户数据!返回 users_id: {_users_id}')
        return
    while len(_group_datas) > 0:
        # 每一页的所有链接
        for _index, _index_data in enumerate(_group_datas):
            # 下载数据
            _tuchong_works_data(_index_data)
        _users_index = _users_index + 1
        # 获取网站内容
        _users_datas = request_context(f"{_users_uri}{_users_index}", None, 'json')
        # 获取所有组
        _group_datas = _users_datas['post_list']


if __name__ == '__main__':

    # _tuchong_users(1317325)

    _tuchong_works(116788760)
