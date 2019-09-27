新建项目 (scrapy startproject xxx)：新建一个新的爬虫项目
	scrapy.cfg: 项目的配置文件。
	mySpider/: 项目的Python模块，将会从这里引用代码。
	mySpider/items.py: 项目的目标文件。
	mySpider/pipelines.py: 项目的管道文件。
	mySpider/settings.py: 项目的设置文件。
	mySpider/spiders/: 存储爬虫代码目录。
	
明确目标 （编写items.py）：明确你想要抓取的目标
	打开 mySpider 目录下的 items.py。
	Item 定义结构化数据字段，用来保存爬取到的数据，有点像 Python 中的 dict，但是提供了一些额外的保护减少错误。
	可以通过创建一个 scrapy.Item 类， 并且定义类型为 scrapy.Field 的类属性来定义一个 					Item（可以理解成类似于 ORM 的映射关系）。
	
制作爬虫 （spiders/xxspider.py）：制作爬虫开始爬取网页
1. 爬数据
在当前目录下输入命令，将在mySpider/spider目录下创建一个名为itcast的爬虫，并指定爬取域的范围：
scrapy genspider itcast "itcast.cn"
在mySpider目录下执行：scrapy crawl itcast
打印的日志出现 [scrapy] INFO: Spider closed (finished)，代表执行完成。
2. 取数据

存储内容 （pipelines.py）：设计管道存储爬取内容
	scrapy保存信息的最简单的方法主要有四种，-o 输出指定格式的文件，命令如下：
	scrapy crawl itcast -o teachers.json
	
	json lines格式，默认为Unicode编码
	scrapy crawl itcast -o teachers.jsonl
	
	csv 逗号表达式，可用Excel打开
	scrapy crawl itcast -o teachers.csv
	
	xml格式
	scrapy crawl itcast -o teachers.xml