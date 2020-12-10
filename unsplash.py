import requests
import json
import time
import os
num = int(input("你想下载几页图片（每页12张）:"))
print("下载开始".center(30,"-"))
start = time.perf_counter()
g_count = 1
root = "./"
def getHtml(url):
    r = requests.get(url,verify=False)
    jls = json.loads(r.text)
    list = []
    for i in jls:
        t = i['urls']['raw']
        list.append(t)
    global g_count
    for i in list:
        path = root + str(g_count) + '.jpg'
        g_count += 1
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(i,verify=False)
            with open(path,'wb') as f:
                f.write(r.content)
                dur = time.perf_counter() - start
            print("\r正在下载第{}张图片，总用时{:.2f}s".format(g_count-1,dur),end = "")
for i in range(1,num+1):
    url = "https://unsplash.com/napi/photos?page=" + str(num) + "&per_page=12"
    getHtml(url)
    print("\n" + "第%d页下载结束".center(30, "-") % i)