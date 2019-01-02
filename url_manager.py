
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        """
        添加新url
        :param url:
        :return:
        """
        pass
    def has_new_url(self):
        """
        判断是否有带爬取得new_url
        :return:
        """
        pass

    def get_new_url(self):
        """
        取一个新的url准备请求它
        :return:
        """
        pass

    def add_new_urls(self, urls):
        """
        一个词条页面上所有链接添加self.new_urls中
        :param urls:
        :return:
        """
        pass
