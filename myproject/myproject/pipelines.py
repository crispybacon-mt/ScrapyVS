# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
from os import walk


class MyprojectPipeline:
    def file_path(self, request, response=None, info=None, *, item=None):

        filename = request.url.split("/")[-1]
        return filename
    
    def get_media_requests(self, item, info):
        adapter = ItemAdapter(item)
        ZIP_FILES = "./ZIP_FILES"
        

        return item
