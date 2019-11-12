# -*- coding: utf-8 -*-
import json
import re

import scrapy
from scrapy import Spider, Request
# from zhihuuser.items import UserItem
from zhihuuser.items import UserItem


class ZhihuSpider(Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    start_user = 'liang-zi-wei-48'

    user_url = 'https://www.zhihu.com/people/{user}/activities'
    user_query = 'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,mark_infos,created_time,updated_time,review_info,excerpt,is_labeled,label_info,relationship.is_authorized,voting,is_author,is_thanked,is_nothelp,is_recognized;data[*].author.badge[?(type=best_answerer)].topics;data[*].question.has_publishing_draft,relationship'

    followees_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
    followees_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'

    followers_query = 'data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'
    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'

    def start_requests(self):
        # url = 'https://www.zhihu.com/api/v4/members/liang-zi-wei-48/followers?include={}'
        yield Request(self.user_url.format(user=self.start_user), callback=self.parse_user)
        yield Request(self.followers_url.format(user=self.start_user, include=self.followers_query, offset=0, limit=20),
                      callback=self.parse_followers)
        yield Request(self.followees_url.format(user=self.start_user, include=self.followees_query, offset=0, limit=20),
                      callback=self.parse_followees)

    def parse_user(self, response):
        item = UserItem()
        url_token = re.findall('people/(.*?)/activities', response.url)
        if len(url_token) > 0:
            item['name'] = response.css('#ProfileHeader span.ProfileHeader-name::text').get()
            item['url_token'] = url_token[0]
            yield item
            print(item['name'])
            print(item['url_token'])
            print('*' * 200)
            yield Request(self.followers_url.format(user=item['url_token'], include=self.followers_query, offset=0, limit=20), callback=self.parse_followers)
            yield Request(self.followees_url.format(user=item['url_token'], include=self.followees_query, offset=0, limit=20), callback=self.parse_followees)

    def parse_followers(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token')), callback=self.parse_user)
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(url=next_page, callback=self.parse_followers)

    def parse_followees(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token')), callback=self.parse_user)
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(url=next_page, callback=self.parse_followees)
