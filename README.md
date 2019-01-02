# 163MusicSpider
基于Python3.6 +PhantomJS开发 （i5-5200u 2.2GHz(2.7GHz) 4G DDR3L 1600MHz ）

实现了根据歌手名下载歌曲的功能

目前存在的问题是没有使用多线程，会影响更新数据的速度

仅支持华语相关歌曲下载,待更新......

数据包请解压到相应的文件夹里，或者选择自己在程序里更新（更新有点慢）

特别注意，该程序仅限于学习交流之用，请勿用于其它用途。支持正版！！！

##  ##################2018/12/07###############
新增批量下载歌曲按照歌手名分类


## ##################2018/12/31###############
在移植到树莓派的时候发现了一个坑(debian)过程一波三折，phantomjs总是出错，百度之后了解到Debian软件源的phantomjs是个残次品？？？

以下是解决方案：

BEGIN

sudo apt install firefox-esr  （到目前debian软件源的最新版本为52.9.0）

然后在https://github.com/mozilla/geckodriver/releases/ 选择版本0.15下载

解压：tar -xzvf xxxx

授权：sudo chmod -R 777 xxxx

复制到/usr/bin  sudo cp xxxx /usr/bin/xxxx 

END

## #################2019/01/03#################
更新数据采用多线程，比之前较快（但该程序在更新数据时消耗大量资源，一般情况下约占本机CPU 55% 内存18%）

