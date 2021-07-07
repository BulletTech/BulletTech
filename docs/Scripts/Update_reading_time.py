# Dependencies
import os
import re
from datetime import datetime


# Post list
Folder_list = ['docs/Dessert','docs/Main_Course']

Post_list = []

for folder in Folder_list:
    for root, directories, files in os.walk(folder, topdown=False):
        for name in files:
            print(os.path.join(root, name))
            if '.md' in name:
                Post_list.append(os.path.join(root, name))


qr_pic_path = """https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png"""
    
ending_pic = """
<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>
"""
                
# Update the reading time
for post in Post_list:
    f = open(post, 'r')
    markdown="".join(f.readlines())

    match = re.search(r'\d{4}-\d{2}-\d{2}', post.split('/')[-1])
    date = datetime.strptime(match.group(), '%Y-%m-%d').date()

    markdown = re.sub(r"发布于\d+年\d+月\d+日，阅读时间", "发布于{}，阅读时间".format(date), markdown)
    markdown = re.sub(r"发布于\d+-\d+-\d+，阅读时间", "发布于{}，阅读时间".format(date), markdown)

    chinese_words = re.findall(r'[\u4E00-\u9FFF]',markdown)
    markdown = re.sub(r"阅读时间：约\d+分钟", "阅读时间：约{}分钟".format(int(len(chinese_words)/200)), markdown)
    
    if qr_pic_path not in markdown:
        markdown += ending_pic

    with open(post, 'w') as new_file:
        new_file.write(markdown)
    print('{} is updated.'.format(post))
