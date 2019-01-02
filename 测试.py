from html_downloader import HtmlDownloader

obj = HtmlDownloader()
result_html = obj.download(url="https://baike.baidu.com/item/Python/407313")
print(result_html)