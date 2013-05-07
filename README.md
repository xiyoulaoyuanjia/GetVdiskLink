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

>* client = VDiskAPIClient(decrypt(user), decrypt(passwd)) 

decrypt(user) decrypt(passwd) 更改为自己新浪微博的用户名与密码    


>* 命令行下使用


>>* ubuntu 11.10 gnome 环境下测试

    ./GetLink.py test/lianxi2.png

>>* 之后上传的链接已经复制到剪贴板中可以直接复制到第三方中使用


>* 桌面环境下nautilus 下测试成功


![](http://openapi.vdisk.me/?m=file&a=download_share_file&ss=f457XZ1lUiUPNvsw9wn0TaI97RU7lAaGjvEyLWmXRq05n--2FWlz2JQCOBn7QliJ2bdkwr51REF--2FMa5A4UQZstf6UO6LPCM)

>>* 成功弹出下图

![](http://openapi.vdisk.me/?m=file&a=download_share_file&ss=2368kEgo7mhGSyJIP2LSTqYnjgtGjPfSqAMIM16HqsvQ4LzbhH9r7H94aBnIh3cDtn--2Fa5U9tsWC7VWrF)
>>*  失败弹出下图

![](http://openapi.vdisk.me/?m=file&a=download_share_file&ss=c8abn--2Bm7LYab4OeNM--2FFhiy0VokcP7jx0IHgDllvq--2FYTecbPkf6Yho--2BNHxFruu07l--2F8slNRka9S4yxNNZX2pn1Q9j--2FOkp)

**todo**

>* 支持 web下上传获得链接方式
>* 桌面环境下支持 fedora 17 右键发送
>* 写一个安装脚本
>* 增加传入正确删除图片的功能




