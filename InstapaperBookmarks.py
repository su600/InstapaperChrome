from flask import Flask,render_template,request,redirect,url_for
from flask_bootstrap import Bootstrap
import instapaper

I = instapaper.Instapaper("d3e10f3296b84857aff6ce62c84d7ec1", "bc408b9151394b498b997e0bc4675b02")
I.login("su600@live.com", "greedisgood1")

# b = instapaper.Bookmark(I, {"url": "http://su600.cn"})
# b.save()

# c = I.bookmarks(limit=10)
# print(c.title)
# for a in c:
#     print(a.title)
#     print(a.url)

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def home():
    # c = I.bookmarks(limit=10)
    if request.method=="GET":
        # print("sssssssssssssssssss")
        c = I.bookmarks(limit=10)
    # elif request.method == "POST":
    #     print("sssssssssssssssssss")
    #     c=I.delete()
    #     c = I.bookmarks(limit=10)
    return render_template("instapaper.html",list=c)

app.run("0.0.0.0",port=1000)
