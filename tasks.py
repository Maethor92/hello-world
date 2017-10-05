#!/usr/bin/env python
import json
import re
from celery import Celery

app = Celery('tasks', backend = 'amqp', broker = 'amqp://morten:12345@192.168.1.37/lab_host')

@app.task()
def searching(filename):

    file = filename

    searchword = ['han', 'hon', 'hen', 'den', 'det', 'denna', 'denne', 'zahl']

    total = {}
    for i in searchword:
        total[i] = 0

    with open('/home/ubuntu/Downloads/data/' + file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line == "":
                tweet = json.loads(line)
                if 'retweeted_status' in tweet:
                    continue
                text = (tweet['text'])

                total['zahl'] = total['zahl'] + 1

                # count occurence and save in total
                for word in searchword:
                    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word.upper()), text.upper()))
                    total[word] = total[word] + count
                    count = 0
    return total


