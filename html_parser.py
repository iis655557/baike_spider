from lxml import etree

class HtmlParser(object):
    def parse(self, html_content):
        """
        # 接收网页的html内容响应，xpath解析，返回想要的数据
        :param html_content: {str} '<htmL></html>'
        :return: new_urls {list} ['https://baike.com/item/某一词条/234234', '']
        :return: new_data {dict} {'title': title, 'summary': summary}
        """
        assert html_content is not None, "html_content为空 请检查"

        dom = etree.HTML(html_content)

        pattern_title = '//dd[@class="lemmaWgt-lemmaTitle-title"]/h1/text()'
        pattern_summary = '//div[@class="lemma-summary"]/div/text()'
        pattern_href = '//div[@class="main-content"]//a[@target="_blank"]/@href'

        title = dom.xpath(pattern_title)[0]
        summary = dom.xpath(pattern_summary)[0]
        new_urls = dom.xpath(pattern_href)      # ['/item/阿姆斯特丹/2223423', ]

        for index, href in enumerate(new_urls):
            # todo 判断链接是否合法，可以用正则或str.find('item')
            new_urls[index] = 'https://baike.baidu.com' + href

        # return title, summary, new_urls
        # context = {}
        # context['title'] = title
        # context['summary'] = summary
        # context['new_urls'] = new_urls
        # return context
        new_data = {'title': title, 'summary': summary}
        return new_urls, new_data