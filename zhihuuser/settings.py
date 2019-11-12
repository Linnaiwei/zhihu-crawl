# -*- coding: utf-8 -*-

# Scrapy settings for zhihuuser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuuser'

SPIDER_MODULES = ['zhihuuser.spiders']
NEWSPIDER_MODULE = 'zhihuuser.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'zhihuuser (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': ' gzip, deflate, br',
    'accept-language': ' zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': ' max-age=0',
    'cookie': ' _zap=be1a6546-9946-4f28-bd25-7f745efc8bcc; d_c0="AACthWkrKxCPTnvGh53CYwO9ijRzkZhk_SA=|1570554968"; q_c1=2025f7e977b545cc854f11bf80d08e1b|1571248196000|1571248196000; __utmz=51854390.1571248197.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|3=entry_date=20191017=1; _xsrf=VNFNfxy8H8La9OvJbRFE6KkaFtV9IEN5; l_n_c=1; n_c=1; __utmc=51854390; SL_wptGlobTipTmp=1; SL_GWPT_Show_Hide_tmp=1; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1572262480,1573382181,1573408372,1573471260; anc_cap_id=9680ec875f534c7ba615dc91158e5767; capsion_ticket="2|1:0|10:1573492102|14:capsion_ticket|44:ZjU4NTU0ZjkyZTJhNDJlY2E3MzdiNGI2MmYyZDNlYWE=|22e4b36d074dfa62a69f6d93b0f45062fa300539b44bd72f77afb904b8e5005a"; tgw_l7_route=4860b599c6644634a0abcd4d10d37251; l_cap_id="NmEzM2EyMTAxNmNiNDRlZjhiY2I3NDg4ZWIyMjEzMDU=|1573507348|60e0c9190100dffee96644c801e96741e0dfdff5"; r_cap_id="YjYwZjRiNzI2N2Y1NDRkYWI3MDMzYmQ4YzA1NjQ4NmU=|1573507348|cdd2d86ac9ccd7b97bd26150ba18579c9f11a352"; cap_id="YjYyOGFhMzg5ZWFhNGE5OTllODhkNDVmMTRhNWQ0NDY=|1573507348|1e7760a7bf2f85131f07866d03a8563c80306295"; __utma=51854390.1435617889.1571248197.1573471253.1573507350.5; __utmb=51854390.0.10.1573507350; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1573507497',
    'referer': ' https://www.zhihu.com/question/355282555/answer/890045878',
    'sec-fetch-mode': ' navigate',
    'sec-fetch-site': ' same-origin',
    'sec-fetch-user': ' ?1',
    'upgrade-insecure-requests': ' 1',
    'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuuserSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuuserDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zhihuuser.pipelines.MongoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MONGO_URI = 'localhost'
MONGO_DB = 'zhihu'
