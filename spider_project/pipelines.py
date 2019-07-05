# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class SpiderProjectPipeline(object):
    def process_item(self, item, spider):
        return item


class PicRenamePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):   # 下载图片
        for img_url in item['img_url']:
            # 添加meta是为了下面重命名文件名使用
            yield Request(img_url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        cname = item['cname']
        image_guid = request.url.split('/')[-1]  # 得到图片后缀
        filename = u'{0}/{1}'.format(cname, image_guid)    # 如：/4kmeishi/xxx.jpg
        return filename