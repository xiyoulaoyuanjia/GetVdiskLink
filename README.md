README
====

**_GetVdiskLink_**

_将图片存入新浪微盘并获得图片的链接地址_

_[使用新浪官方微盘API](http://vdisk.me/api/doc)_ 

_[新浪微盘python 封装API](https://github.com/xiyoulaoyuanjia/VdiskSDK)_

**依赖**

>* ubuntu 下 gnome 桌面环境 Nautilus(sendto) 默认方式
>* fedora 下的 KDE桌面环境 的dolphin   默认方式
>* xclip 的依赖


**如何使用?**

>* 命令行下使用


>>* ubuntu 11.10 gnome 环境下测试

    ./GetLink.py test/lianxi2.png

>>* 之后上传的链接已经复制到剪贴板中可以直接复制到第三方中使用


>* 桌面环境下nautilus 下测试成功


![](http://image.data.vdisk.me/55890007/7d68096ad7dc037634b25efea2c7fbd0844f43a4?ip=1363764985,114.255.40.42&ssig=coiIt2TpB2&Expires=1363763785&KID=sae,l30zoo1wmz&fn=demo.png)

>>* 成功弹出下图

![](http://image.data.vdisk.me/55890007/9e67ae2712c3968cf413b11e507a0261b56e7e54?ip=1363779589,114.255.40.42&ssig=%2F8KoikIyvj&Expires=1363778389&KID=sae,l30zoo1wmz&fn=GetVdiskLink_ok.png)
>>*  失败弹出下图

![](http://image.data.vdisk.me/55890007/66aecc4b90d85cbd18b12e030bd64d87f7cf6697?ip=1363779243,114.255.40.42&ssig=T7SirxrwAs&Expires=1363778043&KID=sae,l30zoo1wmz&fn=GetVdiskLink_error.png)

**todo**

>* 支持 web下上传获得链接方式
>* 桌面环境下支持 fedora 17 右键发送
>* 密码安全? 修改每次上传都要隐藏密码的问题
>* 写一个安装脚本
>* 增加传入正确删除图皮的功能




