---
title: Common Scripts
author: miles
date: 2024-05-21 20:30:00 +0800
categories: [Note]
tags: [scripts]     # TAG names should always be lowercase
---
# Common Scripts

## bundle
preview

```text
bundle exec jekyll s
```

## proxy
powershell auto
<https://zhuanlan.zhihu.com/p/666960686>

powershell manual

```text
$env:http_proxy='http://127.0.0.1:7890'
$env:https_proxy='https://127.0.0.1:7890'
```

wsl auto
```text
#!/bin/bash
host_ip=$(cat /etc/resolv.conf |grep "nameserver" |cut -f 2 -d " ")
export ALL_PROXY="http://$host_ip:7890"
```

