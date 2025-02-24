# 介绍
> lywt 是一个个人自用的小工具合集（当然也可以供广大网友共同使用）。

> 该合集目前包括了音乐爬虫（musicEnjoy）、大文件分割（fileCut）、文件内容 MD5 校验（fileMD5_gui）等功能。

> 同时，该合集也在持续更新中，欢迎网友们提出新的需求，本人会酌情进行添加。


# 代码运行
直接运行根目录下的 main.py

# 打包代码发布pypi
> 打包命令:
> python setup.py sdist build

> 发布命令:
> twine upload dist/lywt-0.1.1.tar.gz

# 打包软件
> 打包成单文件格式
> pyinstaller lywt-F.spec

> 打包成目录格式
> pyinstaller lywt.spec



# cli 接口安装

## 完整安装 lywt

> 你可以在 dist 目录里下载到最新的和老版本的 lywt

> 同时你可以使用命令行 pip install lywt 在你当前的 python 环境中安装 lywt 的所有工具或选择性安装部分工具。



## 安装部分工具

示例：$ pip install lywt.musicEnjoy











# 工具集合



## musicEnjoy
### 使用实例简介
> 相信大家都有这样一种经历，在不经意间听到别人放的某一首歌，并对此极其感兴趣。由于仅仅记住了一些歌词，于是打开百度搜索这首歌，找到了歌名后，打开网抑云搜索这首歌。

> 然后经典来了，“正在试听「xxx」歌曲片段，开通 VIP 畅听完整版” 血压瞬间上来了有木有啊（如果你是土豪，当我没说，如果你有各个音乐平台的VIP，请立即退出这个页面，以免浪费宝贵的时间）。

> 作为一个资深的 ”白嫖“ 网民，我只能自己动手。于是就有了这个简单的小工具。既然网抑云有版权，我们可以去 b站 搜索相关视频，听听这首歌，但是想要随时随刻得带上耳机畅享，总不能一直后台开着 b站 吧？这样也不利于听别的歌。于是有一个思路：把 b站 的歌爬下来，导入网易云云盘。这样就真正“畅听“了~~~

> 通过以上思路，目前本工具集成了 bilibili 的视频音频独立下载、酷狗音乐的音频下载等功能。

[]()

## 使用示例







## 正在开发的功能

暂无



# fileCut

## 简介





## 使用示例





## 正在开发的功能

暂无



# fileMD5_gui

## 简介



## 使用实例





## 正在开发的功能

暂无





# nobody

## 简介





## 使用实例





## 正在开发的功能

暂无
