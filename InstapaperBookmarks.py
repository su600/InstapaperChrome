'''
    Instapaper API程序，自动获取Instapaper列表
    2020年初创建，查看列表，删除，存档
    部署在阿里云服务器，后台运行
    nohup python Instapaper/InstapaperBookmarks.py >/dev/null 2>&1 &
    su600.cn:1000端口，或者 https://su60.cn/instapaper

    2022-3-26，结合IFTTT，将存档按钮改为收藏并存档
    收藏后自动通过IFTTT同步到OneNote快速笔记里，并默认存档，从列表中删除
'''

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
import instapaper

I = instapaper.Instapaper(
    "d3e10f3296b84857aff6ce62c84d7ec1", "bc408b9151394b498b997e0bc4675b02")
I.login("su600@live.com", "greedisgood1")

# b = instapaper.Bookmark(I, {"url": "http://su600.cn"})
# b.save()

# # 读取10条记录
# c = I.bookmarks(limit=10)
# for a in c:
#     print(a.title)
#     print(a.url)

# # 存档最新一条
# d = I.bookmarks(limit=1)
# s=d[0].bookmark_id
# print(s)
# d = instapaper.Bookmark(I, {'bookmark_id': s})
# d.archive()
# # 如何区分不同标签的删除按钮 submit todo

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():  # 打开和刷新列表
    # c = I.bookmarks(limit=10)
    if request.method == "GET":
        # print("sssssssssssssssssss")
        c = I.bookmarks(limit=30)

    if request.method == "POST":  # 存档该条记录（非删除）

        a = request.form.to_dict()
        s = a["id"]
        d = instapaper.Bookmark(I, {'bookmark_id': s})
        # print(s)
        # print(a["Action"])
        if a["Action"] == "Archive":
            # print("存档")
            d.archive()
            c = I.bookmarks(limit=30)
        if a["Action"] == "Star":
            # print("收藏")
            d.star()
            d.archive()
            c = I.bookmarks(limit=30)
        if a["Action"] == "Delete":
            # print("删除")
            d.delete()
            c = I.bookmarks(limit=30)
    return render_template("instapaper.html", list=c)


app.run("0.0.0.0", port=1000)
