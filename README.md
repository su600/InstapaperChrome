# Instapaper ChromeExtension

> Note: beta version, Python program running on Aliyun ECS, just for me.
> 

## Based on great job by rsgalloway https://github.com/rsgalloway/instapaper

Get bookmark urls from Instapaper, Archive or Delete,It's very useful to sync Readlist between iPhone/Android and Chrome.

* Together with Instapaper App:
  
    ![iPhone](https://raw.githubusercontent.com/su600/InstapaperChrome/master/iphone.jpg)

*  Chrome Extension, get your Instapaper Bookmarks url like this:

    ![Chrome](https://raw.githubusercontent.com/su600/InstapaperChrome/master/chrome.png)

---

## 当前版本 / Current Version

基于 Flask + Bootstrap 5 重构，新增以下功能：

- **收藏并存档**（⭐ Star）：收藏书签，并通过 IFTTT 自动同步到 OneNote，同时存档
- **存档**（📂 Archive）：将书签移入存档
- **删除**（🗑 Delete）：从列表中删除书签
- CSRF 保护，防止跨站请求伪造攻击
- Post/Redirect/Get 模式，防止刷新页面时重复提交表单
- Flash 消息提示操作结果

Current web UI screenshot:

![screencapture](https://raw.githubusercontent.com/su600/InstapaperChrome/master/screencapture.png)

