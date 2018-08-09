from scrapy.conf import settings
from .items2 import Master


import pika
import sys
class MasterPipeline(object):
    def __init__(self):
        self.queue = 'task_queue'

    def open_spider(self, spider):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue)


    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        #message = {'volume_url':item['volume_url']}
        message = item['volume_url']
        self.channel.basic_publish(exchange='',
                      routing_key=self.queue,
                      body=message,
                      )
        name = item['name']
        display_name = item['display_name']
        tag = item['tag']
        author = item['author']
        summary = item['summary']
        thumbnail = item['thumbnail']
        return item 

