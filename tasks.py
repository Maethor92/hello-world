#!/usr/bin/env python
import json
import re
from celery import Celery

app = Celery('tasks', backend = 'amqp', broker = 'amqp://localhost//')

@app.task()
def searching(filename):

    file = filename

    searchword = ['han', 'hon', 'hen', 'den', 'det', 'denna', 'denne']

    total = {}
    for i in searchword:
        total[i] = 0

    with open('data/' + file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line == "":
                tweet = json.loads(line)
                if tweet['text'].split()[0] == 'RT':
                    continue
                text = (tweet['text'])

                # count occurence and save in total
                for word in searchword:
                    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word.upper()), text.upper()))
                    total[word] = total[word] + count
                    count = 0
    return total
