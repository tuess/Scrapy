# -*- coding: utf-8 -*-
import scrapy
#引入在items.py中定义的item类
from mySpider.items import MyspiderItem


class ItcastSpider(scrapy.Spider):
##    name = "" ：这个爬虫的识别名称，必须是唯一的，在不同的爬虫必须定义不同的名字。
    name = 'itcast'
##    allow_domains = [] 是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页，不存在的URL会被忽略。
    allowed_domains = ['itcast.cn']
##    start_urls = () ：爬取的URL元祖/列表。爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些urls开始。其他子URL将会从这些起始URL中继承性生成
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

##parse(self, response) ：解析的方法，每个初始URL完成下载后将被调用，调用的时候传入从每一个URL传回的Response对象来作为唯一参数，主要作用如下：
##负责解析返回的网页数据(response.body)，提取结构化数据(生成item)生成需要下一页的URL请求
    def parse(self, response):
##        filename="teacher.html"
##        open(filename,'w').write(response.body)
        
##            #获取网站标题
##            context=response.xpath('/html/head/title/text()')
##
##            #提取网站标题
##            title=context.extract_first()
##            print(title)
##            pass

                #存放老师信息的集合
                items=[]

                for each in response.xpath("/html/body/div[1]/div[5]/div[2]/div[1]/ul/li[1]/div[2]"):
                    item=MyspiderItem()
                    #extract()方法返回的都是unicode字符串
                    name=each.xpath("h3/text()").extract()
                    title=each.xpath("h4/text()").extract()
                    info=each.xpath("p/text()").extract()
                    
##                    print (name,title,info)

                    #xpath返回的是一个元素的列表
                    item['name']=name[0]
                    item['title']=title[0]
                    item['info']=info[0]

                    items.append(item)
                    
                #直接返回最后的数据
                return items
