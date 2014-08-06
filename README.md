editor_asis
===========

############################################################
# FrameName:Editor-Assassin								   #
# Usage:											       #
# Description:Xday exploit for Website editors			   #
# FileDirection:Every exploit live with its dic each folder#
# Create Date:Fri Jan 10th,2014							   #
############################################################
Update time:2014.08.06.
url.txt里的内容为扫描器（如御剑）扫描好的路径，形式如下：
www.baidu.com/fckeditor/
www.baidu.com/ewebeditor/

基本字典文件：
url.txt(需用户配置)
username.txt(默认字典可更改)
password.txt(默认字典可更改)

根目录主程序文件：attack.py
扫描完以后会在根目录生成一个文件：result.html，会覆盖已有文件。

在程序启动前会出现输入编辑器类型的选项，可输入多项，以逗号分割开，形式如下：
fckeditor,ewebeditor
目前编辑器支持类型：
types=["fckeditor","ewebeditor","kindeditor"]
