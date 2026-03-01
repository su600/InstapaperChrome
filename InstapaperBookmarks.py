'''
    Instapaper API程序，自动获取Instapaper列表
    2020年初创建，查看列表，删除，存档
    部署在阿里云服务器，后台运行
    nohup python Instapaper/InstapaperBookmarks.py >/dev/null 2>&1 &
    su600.cn:1000端口，或者 https://su60.cn/instapaper

    2022-3-26，结合IFTTT，将存档按钮改为收藏并存档
    收藏后自动通过IFTTT同步到OneNote快速笔记里，并默认存档，从列表中删除
'''

import os
import sys
from flask import Flask, render_template, request, redirect, url_for, flash
import instapaper

CONSUMER_KEY = os.environ.get("INSTAPAPER_CONSUMER_KEY", "")
CONSUMER_SECRET = os.environ.get("INSTAPAPER_CONSUMER_SECRET", "")
USERNAME = os.environ.get("INSTAPAPER_USERNAME", "")
PASSWORD = os.environ.get("INSTAPAPER_PASSWORD", "")
FLASK_SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "")

_missing = [
    name for name, val in [
        ("INSTAPAPER_CONSUMER_KEY", CONSUMER_KEY),
        ("INSTAPAPER_CONSUMER_SECRET", CONSUMER_SECRET),
        ("INSTAPAPER_USERNAME", USERNAME),
        ("INSTAPAPER_PASSWORD", PASSWORD),
        ("FLASK_SECRET_KEY", FLASK_SECRET_KEY),
    ] if not val
]
if _missing:
    print(f"ERROR: Missing required environment variables: {', '.join(_missing)}", file=sys.stderr)
    sys.exit(1)

I = instapaper.Instapaper(CONSUMER_KEY, CONSUMER_SECRET)
I.login(USERNAME, PASSWORD)

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

BOOKMARK_LIMIT = 30

ACTION_LABELS = {
    "Archive": "存档",
    "Star": "收藏并存档",
    "Delete": "删除",
}


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        form = request.form.to_dict()
        bookmark_id = form.get("id")
        action = form.get("Action")
        if bookmark_id and action in ACTION_LABELS:
            try:
                bm = instapaper.Bookmark(I, {'bookmark_id': bookmark_id})
                if action == "Archive":
                    bm.archive()
                elif action == "Star":
                    bm.star()
                    bm.archive()
                elif action == "Delete":
                    bm.delete()
                flash(f"✅ 操作成功：{ACTION_LABELS[action]}", "success")
            except Exception as e:
                flash(f"❌ 操作失败：{e}", "danger")
        # Post/Redirect/Get：避免刷新时重复提交表单
        return redirect(url_for("home"))

    try:
        bookmarks = I.bookmarks(limit=BOOKMARK_LIMIT)
    except Exception as e:
        flash(f"❌ 获取书签失败：{e}", "danger")
        bookmarks = []

    return render_template("instapaper.html", list=bookmarks)


if __name__ == "__main__":
    app.run("0.0.0.0", port=1000)
