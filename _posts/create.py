from datetime import datetime
import os

# 从用户输入获取标题和类别
title = input("Input title: ")
category = input("Input category: ")

# 获取当前时间
time = datetime.now()

# 构建文件名
filename = "{0}-{1:02d}-{2:02d}-[{3}]{4}.md".format(time.year, time.month, time.day, category, title)

# 构建文件路径
file_path = os.path.join("D:\Projects\whilemiles.github.io\_posts", filename)
# 构建文件内容
content = f"""---
title: {title}
author: miles
date: {time.strftime("%Y-%m-%d %H:%M:%S")} +0800
categories: [{category}]
tags: []
---
# {title}
"""

# 将内容写入文件
with open(file_path, "w") as file:
    file.write(content)

# 输出文件路径
print(f"已在当前文件夹下创建新文件: {file_path}")
