# http://encensmagazine.com/


from src.baseutil.request_util import request_context, download_images

server = "http://encensmagazine.com"


def encens_srcset(srcset):
    if srcset != "":
        # /_/issues/issue-41/831/57b2f.jpg 927w
        jpgs = srcset.split(",")[0]
        ijpg = jpgs.strip().split(" ")
        # 处理文件名
        file_name = ijpg[0].split("/issue-")[1].replace("/", "_")
        # 下载文件
        download_images('encens', server + "/" + ijpg[0], file_name)


def encens():
    print(f'=========== encens 解析数据 START ===========')
    website = server + "/api/data"
    # 获取网站内容
    soup = request_context(website, None, 'json')
    # 所有数据
    issues = soup['issues']
    # 循环处理数据
    for item in issues:
        assets = item['assets']
        if isinstance(assets, list):
            for iAsset in assets:
                encens_srcset(iAsset['srcset'])
    print(f'=========== nelkshuhe 解析数据完成 ✅ ===========')


if __name__ == '__main__':
    encens()
