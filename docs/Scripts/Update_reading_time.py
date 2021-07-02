import os
import re
from datetime import datetime
import numpy as np
import markdown

Folder_list = ['../Dessert','../Main_Course']

Post_list = []

for folder in Folder_list:
    for root, directories, files in os.walk(folder, topdown=False):
        for name in files:
            print(os.path.join(root, name))
            if '.md' in name:
                Post_list.append(os.path.join(root, name))
                
for post in Post_list:
    f = open(post, 'r')
    htmlmarkdown="".join(f.readlines())
    match = re.search(r'\d{4}-\d{2}-\d{2}', post.split('/')[-1])
    date = datetime.strptime(match.group(), '%Y-%m-%d').date()
    htmlmarkdown = re.sub(r"发布于\d+-\d+-\d+，阅读时间", "发布于{}，阅读时间".format(date), htmlmarkdown)
    chinese_word = re.findall(r'[\u4E00-\u9FFF]',htmlmarkdown)
    print(len(chinese_word))
    htmlmarkdown = re.sub(r"阅读时间：约\d+分钟", "阅读时间：约{}分钟".format(int(len(chinese_word)/200)), htmlmarkdown)
    
    with open(post, 'w') as new_file:    
        new_file.write(htmlmarkdown)