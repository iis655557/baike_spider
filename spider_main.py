from . import html_outputer, html_downloader, html_parser, url_manager
import time



#  项目入口
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmlParser()
        self.output = html_outputer.HtmlOutputer()


    def craw(self, root_url, page_amount=5, time_sleep=1):
        try:
            count = 1
            # 添加第一个待爬取url
            self.urls.add_new_url(root_url)
            # 如何集合中有url，那么就取出一个url请求，没有连接就跳出
            while self.urls.has_new_url():
                new_url =self.urls.get_new_url()
                print(f"craw {count}:{new_url}")
                html_content = self.downloader.download(new_url)
                mew_urls, new_data = self.parser.parser.parse(html_content)
                self.urls.add_new_urls(new_url)
                self.output.collect_data(new_url, new_data)
                count += 1
                if count > page_amount:
                    break

        except Exception as e:
            print(f'craw failed {new_url} reason:{e}')

if __name__ == '__main__':
    # 爬取的页面
    ROOT_URL = 'https://baike.com/item/Python/407313'
    # 总共请求多少页
    PACE_AMOUNT = 5
    # 每次请求间隔时间 秒
    TIME_SLEEP = 1
    spider = SpiderMain()
    spider.craw(ROOT_URL, PACE_AMOUNT, TIME_SLEEP)