# -*- coding: utf-8 -*-
import scrapy
from ..items import NewsItem


# from ..xpath_modles import func


class FinanceSpider(scrapy.Spider):
    """财经搜索网"""
    # 爬虫名，启动爬虫时需要的参数
    name = 'finance'
    # 爬取域范围，允许爬虫在这个域名下进行爬取(可选)
    allowed_domains = []
    # url列表，爬虫执行后第一批请求，将从这个列表获取
    page = 2

    # 并发爬取
    # start_urls =  ['http://news.21so.com/chanye/'+ str(page)+ '.html' for page in range(2, 6)]
    # start_urls = ['http://news.21so.com/chanye/index.html', 'http://news.21so.com/chanye/' + str(page) + '.html',
    #               'http://news.hexun.com/'
    #               ]
    # start_urls=['http://news.hexun.com/']

    urls = ['http://news.21so.com/chanye/index.html', 'http://news.21so.com/chanye/' + str(page) + '.html',
            'http://news.hexun.com/', 'http://finance.sina.com.cn/roll/index.d.html?cid=57012',
            'https://www.msn.cn/zh-cn/money/justinnews', 'http://www.21jingji.com/', 'https://www.lanjinger.com/',
            'http://www.nbd.com.cn/', 'http://www.cnforex.com/']

    # 重写start_quests方法
    def start_requests(self):

        headers = [{
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'},
            {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'},
            {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'},
            {
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                'cookie': 'UOR=,finance.sina.com.cn,; SINAGLOBAL=39.173.9.241_1585029197.407246; Apache=39.173.9.241_1585029197.407247; ULV=1585029197833:1:1:1:39.173.9.241_1585029197.407247:; U_TRS1=000000f1.d71a5c.5e79a051.2eb878f4; U_TRS2=000000f1.d7245c.5e79a051.2d67c8c8; lxlrttp=1578733570; UM_distinctid=1711fc5bd1bac0-085ec1b159a693-396a7f06-13c680-1711fc5bd1cbf8; __gads=ID=adfc5a1643bda66c:T=1585375985:S=ALNI_MaAPWapjRh3-zK6jzTIA2n-z0zVTA; hqEtagMode=1; CNZZDATA5581086=cnzz_eid%3D1439749904-1585373040-https%253A%252F%252Ffinance.sina.com.cn%252F%26ntime%3D1585394640; CNZZDATA5661630=cnzz_eid%3D1868432954-1585372979-%26ntime%3D1585394579; CNZZDATA5847902=cnzz_eid%3D1159717288-1585373225-%26ntime%3D1585394825; CNZZDATA1261995448=1293945500-1585372780-%7C1585394380; CNZZDATA1260051864=1250056124-1585372839-%7C1585394439; CNZZDATA1278178973=1283778191-1585394557-%7C1585394557; rotatecount=4'
            }, {
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                'cookie': 'RecentStocks=; anoncknm=; dpio=2; MC1=GUID=26600d3162a84cfd9926199685c80a29&HASH=2660&LV=202003&V=4&LU=1585400548374; MS0=09d420c15719432dbca59182beb30993; MUID=18CDA26B381868ED1E1DACF03967697A; _cb_ls=1; _cb=5mdkCDVFSx5jNple; _cb_svref=null; ecadprovider=40; adv_xm_uuid_day_365=b85a52e1-a515-467e-8cf0-6781b224b264; _chartbeat2=.1585400552862.1585400700616.1.TIZwhQwux1DIWw03DgRbE0CdtYTR.6'
            }, {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'},
            {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'},
            {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'},
            {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'},
        ]

        for url, headers in zip(self.urls, headers):
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        # 对网页做一个判断，进行网页分类，根据网页类型取数据
        if response.url == self.urls[0] or response.url == self.urls[1]:
            """财经搜索网"""
            node_list = response.xpath('//div[@class="textBox"]')
            for node in node_list:
                item = NewsItem()
                # 提取每条新闻的信息
                # 标题
                item['newsTitle'] = node.xpath('./h5/a/text()').extract()[0]
                # 关键字
                if len(node.xpath('./div[@class="tags"]/a/text()')):
                    item['newsKeyword'] = node.xpath('./div[@class="tags"]/a/text()').extract()
                else:
                    item['newsKeyword'] = ""
                # 链接
                item['newsLink'] = node.xpath('./h5/a/@href').extract()[0]
                # 二级页面链接
                detail_url = node.xpath('./h5/a/@href').extract()[0]

                yield scrapy.Request(url=detail_url, callback=self.detail_0_1_parse, meta={"item": item})

                # yield item
            # 构建下一页请求，取了前6页的新闻
            if int(self.page) < 6:
                self.page += 1
                url = 'http://news.21so.com/chanye/' + str(self.page) + '.html'
                yield scrapy.Request(url, callback=self.parse)

        elif response.url == self.urls[2]:
            """和讯财经网"""

            # url = func(response)
            node_list = response.xpath('//div[@class="l"]//ul/li')  # 包含了所有链接,写到最细的分类
            for node in node_list:
                item = NewsItem()
                # 标题
                item['newsTitle'] = node.xpath('./a/text()').extract()[0]  # 每一条的链接
                # 关键字
                item['newsKeyword'] = ""
                # 链接
                item['newsLink'] = node.xpath('./a/@href').extract_first()
                # 二级页面链接
                detail_url = node.xpath('./a/@href').extract()[0]
                yield scrapy.Request(url=detail_url, callback=self.detail_2_parse, meta={"item": item})

        elif response.url == self.urls[3]:
            """新浪财经期货"""
            node_list = response.xpath('//ul[@class="list_009"]/li')
            for node in node_list:
                item = NewsItem()
                # 标题
                item['newsTitle'] = node.xpath('./a/text()').extract_first()
                # 关键字
                item['newsKeyword'] = ""
                # 链接
                item['newsLink'] = node.xpath('./a/@href').extract_first()
                detail_url = node.xpath('./a/@href').extract_first()

                yield scrapy.Request(url=detail_url, callback=self.detail_3_parse, meta={"item": item})


        elif response.url == self.urls[4]:
            """msn"""
            node_list = response.xpath('//div[@class="rivercardphoto"]/ul/li')
            for node in node_list:
                item = NewsItem()
                item['newsTitle'] = node.xpath('./a/h3/text()').extract_first()
                item['newsKeyword'] = ""
                newsLink1 = node.xpath('./a/@href').extract_first()
                item['newsLink'] = 'https://www.msn.cn' + newsLink1
                detail_url = 'https://www.msn.cn' + newsLink1
                yield scrapy.Request(url=detail_url, callback=self.detail_4_parse, meta={"item": item})


        elif response.url == self.urls[5]:
            """21经济网"""
            node_list = response.xpath('//div[@id="data_list"]/div[@class="li"]/div')
            for node in node_list:
                item = NewsItem()
                item['newsTitle'] = node.xpath('./a/text()').extract_first()
                item['newsKeyword'] = ""
                item['newsLink'] = node.xpath('./a/@href').extract_first()
                detail_url = node.xpath('./a/@href').extract_first()
                yield scrapy.Request(url=detail_url, callback=self.detail_5_parse, meta={"item": item})

        elif response.url == self.urls[6]:
            """蓝鲸财经"""
            node_list = response.xpath('//div[@class="lj-rank-list__info"]')
            for node in node_list:
                item = NewsItem()
                item['newsTitle'] = node.xpath('./a/text()').extract_first()
                item['newsKeyword'] = ""
                newsLink1 = node.xpath('./a/@href').extract_first()
                item['newsLink'] = 'https://www.lanjinger.com/' + newsLink1
                detail_url = 'https://www.lanjinger.com/' + newsLink1
                yield scrapy.Request(url=detail_url, callback=self.detail_6_parse, meta={"item": item})

        elif response.url == self.urls[7]:
            """每经网"""
            node_list = response.xpath('//div[@class="m-center-box-text"]/ul[@class="u-news-list"]/li')
            for node in node_list:
                item = NewsItem()
                item['newsTitle'] = node.xpath('./a/text()').extract_first()
                item['newsKeyword'] = ""
                item['newsLink'] = node.xpath('./a/@href').extract_first()
                detail_url = node.xpath('./a/@href').extract_first()
                yield scrapy.Request(url=detail_url, callback=self.detail_7_parse, meta={"item": item})

        elif response.url == self.urls[8]:
            """环球外汇网"""
            node_list = response.xpath('//div[@class="mleft"]/figure/figcaption')
            for node in node_list:
                item = NewsItem()
                item['newsTitle'] = node.xpath('./a/text()').extract_first()
                item['newsKeyword'] = ""
                item['newsLink'] = node.xpath('./a/@href').extract_first()
                detail_url = node.xpath('./a/@href').extract_first()

                yield scrapy.Request(url=detail_url, callback=self.detail_8_parse, meta={"item": item})

    def detail_0_1_parse(self, response):
        """财经搜索二级页面"""
        item = response.meta["item"]

        node_list = response.xpath('//div[@class="articleInfo"]')
        for node in node_list:
            # 来源
            item['newsSource'] = node.xpath('normalize-space(./span[@class="articleSource"]/text())').extract()[0]
            # 时间
            item['newsTime'] = node.xpath('normalize-space(./span[@class="articleDate"]/text())').extract()[0]

            yield item

    def detail_2_parse(self, response):
        """和讯新闻二级页面"""
        item = response.meta["item"]

        if 'tv' in response.url:
            if response.xpath('normalize-space(//div[@class="little_screen"]/div/span[1]/text())'):
                item['newsTime'] = \
                    response.xpath('normalize-space(//div[@class="little_screen"]/div/span[1]/text())').extract()[0]
            else:
                item['newsTime'] = ""
            if response.xpath('normalize-space(//div[@class="little_screen"]/div/span[2]/a/text())'):
                item['newsSource'] = \
                    response.xpath('normalize-space(//div[@class="little_screen"]/div/span[2]/a/text())').extract()[0]
            else:
                item['newsSource'] = ""

        else:

            if len(response.xpath('//div[@class="clearfix"]//span/text()')):
                item['newsTime'] = response.xpath('//div[@class="clearfix"]//span/text()').extract()[0]
            else:
                item['newsTime'] = ""
            if len(response.xpath('//div[@class="clearfix"]//a/text()')):
                item['newsSource'] = response.xpath('//div[@class="clearfix"]//a/text()').extract()[0]
            else:
                item['newsSource'] = ""

            yield item

    def detail_3_parse(self, response):
        """新浪财经期货二级页面"""
        item = response.meta["item"]
        node_list = response.xpath('//div[@class="date-source"]')
        for node in node_list:
            # 来源
            if len(node.xpath('./span[@class="date"]/text()')):
                item['newsSource'] = node.xpath('./span[@class="date"]/text()').extract_first()
            else:
                item['newsSource'] = ""
            # 时间
            if len(node.xpath('./a/text()')):
                item['newsTime'] = node.xpath('./a/text()').extract_first()
            else:
                item['newsTime'] = ""
            yield item

    def detail_4_parse(self, response):
        """msn二级页面"""
        item = response.meta["item"]
        node_list = response.xpath('//div[@class="authortime-info"]')
        for node in node_list:
            # 来源
            if len(node.xpath('./div[@class="authorname-txt gap"]/span/text()')):
                item['newsSource'] = node.xpath('./div[@class="authorname-txt gap"]/span/text()').extract_first()
            else:
                item['newsSource'] = ""
            # 时间
            if len(node.xpath('./div[@class="timeinfo-txt"]/time/text()')):
                item['newsTime'] = node.xpath('./div[@class="timeinfo-txt"]/time/text()').extract_first()
            else:
                item['newsTime'] = ""
            yield item

    def detail_5_parse(self, response):
        """21经济网二级页面"""
        item = response.meta["item"]
        node_list = response.xpath('//p[@class="Wh"]')
        for node in node_list:
            if len(node.xpath('./span[3]/text()')):
                item['newsSource'] = node.xpath('./span[3]/text()').extract_first()
            else:
                item['newsSource'] = ""
            # 时间
            if len(node.xpath('./span[1]/text()')):
                item['newsTime'] = node.xpath('./span[1]/text()').extract_first()
            else:
                item['newsTime'] = ""

            yield item

    def detail_6_parse(self, response):
        """蓝鲸财经二级页面"""
        item = response.meta["item"]
        node_list = response.xpath('//div[@class="article-info clear-fix"]')
        for node in node_list:
            # 来源
            if len(node.xpath('./span[2]/text()')):
                item['newsSource'] = node.xpath('normalize-space(./span[2]/text())').extract_first()
            else:
                item['newsSource'] = ""
            # 时间
            if len(node.xpath('./span[4]/text()')):
                item['newsTime'] = node.xpath('./span[4]/text()').extract_first()
            else:
                item['newsTime'] = ""
            yield item

    def detail_7_parse(self, response):
        """每经网二级页面"""
        item = response.meta["item"]
        node_list = response.xpath('//div[@class="g-article-top"]/p')
        for node in node_list:
            if len(node.xpath('./span[1]/text()')):
                item['newsSource'] = node.xpath('normalize-space(./span[1]/text())').extract_first()
            else:
                item['newsSource'] = ""
            # 时间
            if len(node.xpath('./span[2]/text()')):
                item['newsTime'] = node.xpath('normalize-space(./span[2]/text())').extract_first()
            else:
                item['newsTime'] = ""

            yield item

    def detail_8_parse(self,response):
        """环球外汇网二级页面"""
        item = response.meta["item"]
        node_list = response.xpath('//div[@class="mleft"]/section/h3')
        for node in node_list:
            if len(node.xpath('./a/text()')):
                item['newsSource'] = node.xpath('./a/text()').extract_first()
            else:
                item['newsSource'] = ""
            # 时间
            if len(node.xpath('./time/text()')):
                item['newsTime'] = node.xpath('./time/text()').extract_first()
            else:
                item['newsTime'] = ""

            yield item
