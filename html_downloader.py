# 下载器
import requests

class HtmlDownloader(object):
    def download(self, url):
        assert url is not None, "download()方法参数url不能为None"

        # if url is None:
        #     raise Exception("参数url不能不能为None")
        #
        # if url is None:
        #     return None

        headers = {
            'Host': 'baike.baidu.com',
            'Referer': 'https://baike.baidu.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f'请求失败， code {response.status_code}')

        return response.content.decode(encoding='utf-8')