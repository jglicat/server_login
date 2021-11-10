# 自动登录系统
基于selenium模拟点击，并采用pyotp生成二次验证  
## 环境配置
在windows（linux改一改应该也行）下安装谷歌浏览器，并下载对应版本的[chromedriver](http://npm.taobao.org/mirrors/chromedriver/)解压后扔到环境目录下，如`C:\Windows`  
pip install -r requirements.txt  
## 启动
填写`line 48`中的`username`, `pwd`, `key`  
key的获取可参考 https://github.com/viljoviitanen/freeotp-export  
python main.py  
## xshell一键脚本
将`gpu01.vb`中的所有`username`, `pwd`替换成真实值，下载到本地  
在xshell上方选项卡的`查看->快速命令`中打开`快速命令栏`，然后添加按钮，类型选择`运行脚本`，选用`gpu01.vb`,添加完成后单击即可运行  
`gpu01.vb`是在初始界面登录到`gpu01`的脚本，登录到其他gpu以及自动激活环境等功能，可以自行更改