import getpass
import os

import requests
from bs4 import BeautifulSoup

"""
Requests库将响应内容封装在一个字典对象中，其中包括以下**键**（key）： 
    1.  url  - 返回响应的URL。 
    2.  status_code  - 返回响应的HTTP状态码。 
    3.  headers  - 返回响应的HTTP标头。 
    4.  text  - 以文本形式返回响应正文。 
    5.  content  - 以二进制形式返回响应正文。 
    6.  json()  - 将响应正文解析为JSON格式的Python对象。 
    7.  cookies  - 返回响应的Cookies。 
    8.  elapsed  - 从请求发送到响应接收所花费的时间。 
"""

_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/113.0.0.0 Safari/537.36",
    "Cookie": "Hm_lvt_debc91213222aae0abfdb6176ec8d28a=1685196862; "
              "__gads=ID=986ea88bdfdee136-223029be9cb400f2:T=1685196862:RT=1685200660:S"
              "=ALNI_MYyZn4LQPPGUIWehbLibLBL3rgiDw; "
              "__gpi=UID=00000c0ba3c4c57e:T=1685196862:RT=1685200660:S=ALNI_MZy9BuTVsGXLxztcGvG-Jjpe0myjA; "
              "Hm_lpvt_debc91213222aae0abfdb6176ec8d28a=1685200783",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7"
}


# 获取网页内容
def request_context(uri, headers, _type):
    if headers is None or len(headers) != 0:
        headers = _headers
    # 发送请求并将响应内容保存到文件中
    response = requests.get(uri, headers=headers)
    if "html" == _type:
        return BeautifulSoup(response.text, 'html.parser')
    if "json" == _type:
        return response.json()
    return response


# 获取图片内容
def request_images(uri):
    return requests.get(uri, headers=_headers)


# 保存图片内容
def download_images(module, uri, name):
    # 存放文件目录
    folder = '/Users/' + getpass.getuser() + '/Downloads/images/' + module

    # 如果目录不存在，则创建目录
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path_name = folder + '/' + name
    # 如果文件不存在,下载文件
    if not os.path.isfile(file_path_name):
        # 发送请求并将响应内容保存到文件中
        response = request_images(uri)
        with open(f'{file_path_name}', 'wb') as f:
            f.write(response.content)
        print(f'========== 下载文件成功！存储目录：{folder}｜文件名称：{name}')
        return 'saved'
    else:
        return 'exist'

