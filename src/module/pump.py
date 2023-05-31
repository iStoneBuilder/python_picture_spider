# https://www.pumpfashionmag.com/pumptorials


from src.baseutil.request_util import request_context, download_images

server = "https://www.pumpfashionmag.com"


def build_name(img_src):
    strs = img_src.split("/")
    file_name = strs[len(strs) - 1]
    replace_str = ["Cover+", "PUMP+", "Logo+", "Magazine+", "Fashion+", "Beauty+", "Beauty+Issue+", "+Editor",
                   "Choice+", "Tearsheets+", "Issue+", "%7C+", "%7C", "%26+", "%27s+"]
    for istr in replace_str:
        file_name = file_name.replace(istr, "")
    file_name = file_name.replace("+", "_")
    return file_name


def pump_page(uri):
    soup = request_context(uri, None, 'html')
    for link in soup.find_all('img'):
        img_src = link.get('data-src')
        if img_src is not None and img_src.startswith("http"):
            file_name = build_name(img_src)
            download_images('pump', img_src, file_name)


def pump():
    print(f'=========== pump 解析数据 START ===========')
    types = ["/pumptorials"]
    for iType in types:
        website = server + iType
        # 获取网站内容
        soup = request_context(website, None, 'html')
        # 存放请求的栏目
        links = [website]
        for link in soup.find_all('a'):
            classes = link.get("class")
            if "summary-title-link" in classes:
                href = link.get('href')
                if href not in links:
                    links.append(href)
                    pump_page(server + href)
    print(f'=========== nelkshuhe 解析数据完成 ✅ ===========')


if __name__ == '__main__':
    pump()
