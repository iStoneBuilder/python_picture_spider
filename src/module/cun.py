""""
http://www.cnu.cc/users/518554?page=2 用户
"""
import json

from src.baseutil.async_util import async_executor
from src.baseutil.request_util import request_context, download_images

server = "http://www.cnu.cc"


def download_cun_works_data(_params_data):
    _works_data = _params_data['data']
    _cun_status = ''
    # 图片数组
    _works_data_img = _works_data.find_all('div', {"id": "imgs_json"})
    # 组图名称
    _works_title = _works_data.find('h2', {"class": "work-title"}).text.strip()
    # 作者名
    _works_author = _works_data.find('span', {"class": "author-info"}).find('strong').text.strip()
    # 存储数据文件夹
    _works_folder = f'C{_params_data["userId"]}_IMG_{_works_author}'
    # 判断是否有数据
    if len(_works_data_img) > 0:
        print(
            f'========== ✅图组数据下载开始!   users_id: {_params_data["userId"]} | works_id: {_params_data["workId"]} ｜'
            f'works_title: {_works_title}')
        _works_data_list = json.loads(_works_data_img[0].text)
        _new_file_index = 1000000000
        # 循环处理数据
        for index, _i_works_data in enumerate(_works_data_list):
            _works_paths = _i_works_data['img'].split(".")
            # 获取文件后缀
            _works_suffix = _works_paths[len(_works_paths) - 1]
            # 生成新文件名
            _new_file_name = f'{_params_data["workId"]}_{_new_file_index + index + 1}.{_works_suffix}'
            # 处理新名字
            _new_file_name = _new_file_name.replace("_100000", "_")
            # 下载文件链接
            _file_download_uri = "http://imgoss.cnu.cc/" + _i_works_data['img'] + "?x-oss-process=style/content"
            # 开始下载文件
            _cun_status = download_images(_works_folder, _file_download_uri, _new_file_name)
            if _cun_status == 'exist':
                print(
                    f'========== 跳过下载,文件组已存在! users_id: {_params_data["userId"]} | '
                    f'works_id: {_params_data["workId"]} ｜ works_title: {_works_title}')
    return _cun_status


# 组图
def download_cun_works(_work_id):
    _work_uri = server + f'/works/{_work_id}'
    # 获取组图数据
    _works_data = request_context(_work_uri, None, 'html')
    if _works_data is not None:
        # 获取作者URI
        _span_author_uri = _works_data.find('span', {"class": "author-info"}).find('a').get('href')
        # 获取用户ID
        _users_id = _span_author_uri.replace('http://www.cnu.cc/users/', '')
        # 下载组图数据
        async_executor(download_cun_works_data, {'data': _works_data, 'workId': _work_id, 'userId': _users_id})
    return 'NotFind'


# 用户
def download_cun_users(_users_id):
    print(f'========== ✅关注用户数据处理!开始 users_id: {_users_id}')
    # 下载链接
    _users_uri = f'{server}/users/{_users_id}?page='
    _users_index = 0
    # 获取网站内容
    _users_datas = request_context(f"{_users_uri}{_users_index}", None, 'html')
    # 获取所有组
    _group_datas = _users_datas.find_all('a', {"class": "thumbnail"})
    if len(_group_datas) == 0:
        print(f'========== ✅没有找到用户数据!返回 users_id: {_users_id}')
        return
    while len(_group_datas) > 0:
        # 每一页的所有链接
        for _index, _index_data in enumerate(_group_datas):
            _index_hrefs = _index_data.get('href').split('/')
            # 组ID
            _works_id = _index_hrefs[len(_index_hrefs) - 1]
            # 下载数据
            async_executor(download_cun_works, _works_id)
        _users_index = _users_index + 1
        # 获取网站内容
        _users_datas = request_context(f"{_users_uri}{_users_index}", None, 'html')
        # 获取所有组
        _group_datas = _users_datas.find_all('a', {"class": "thumbnail"})
