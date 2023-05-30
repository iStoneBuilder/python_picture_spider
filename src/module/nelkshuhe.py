# http://www.nelkshuhe.com/


from src.baseutil.irequests import request_context, download_images

server = "http://www.nelkshuhe.com"


def nelkshuhe():
    print(f'=========== nelkshuhe 解析数据 START ===========')
    # 获取网站内容
    soup = request_context(server + "/", None, 'html')
    # 存放请求的栏目
    links = [server + "/"]
    for link in soup.find_all('a'):
        href = link.get('href')
        # 链接已存在，跳过
        if href not in links:
            # 存储链接
            links.append(href)
            # 解析链接
            nelkshuhe_page(href)
    print(f'=========== nelkshuhe 解析数据完成 ✅ ===========')


def nelkshuhe_page(uri):
    soup = request_context(uri, None, 'html')
    for link in soup.find_all('img'):
        # 文件URI
        file_uri = link.get('src')
        # 链接数组
        file_part = file_uri.split('/')
        # 文件名称
        file_name = file_part[len(file_part) - 1]
        file_alt = link.get('alt')
        # 如果file_alt 无值
        if file_alt is None or len(file_alt) == 0:
            if file_name.startswith('th-'):
                new_name = file_name.replace('th-', '')
                file_uri = file_uri.replace(file_name, new_name)
                file_name = new_name
            download_images('nelkshuhe', file_uri, file_name)
            continue
        if file_alt.startswith('http'):
            download_images('nelkshuhe', file_alt, file_name)
        else:
            if file_name != file_alt:
                file_uri = file_uri.replace(file_name, file_alt)
                download_images('nelkshuhe', file_uri, file_alt)


if __name__ == '__main__':
    nelkshuhe()
