#!/usr/bin/env python
# -*- coding: utf-8 -*-


from vdisksdk import * 
import os

import sys

from Gui import MessageGui

def _guess_image_type(fp):
    '''
    猜测图片类型
    '''
    _JPEG=1
    _BMP=2
    _GIF=3
    _PNG=4
    _NotImage=0
    f = file(fp, 'rb')
    data = f.read(10).encode('hex')
    ftype = _NotImage
    if data.startswith('ffd8'):
        ftype = _JPEG
    if data.startswith('424d'):
        ftype = _BMP
    if data.startswith('474946'):
        ftype = _GIF
    elif data.startswith('89504e470d0a1a0a'):
        ftype = _PNG
    return ftype


if len(sys.argv) ==2:
    filename=sys.argv[1]
else:
	filename="test/lianxi2.png"

### 验证图片是否存在 与格式是否为图片
if _guess_image_type(filename) == 0:
    MessageGui.GetLinkExeGui(MessageGui.MessageGui_Error_IsNotImage)
    sys.exit()

#os.system("echo "+filename+">> /tmp/tem.txt")


try :
### 这里需要一种隐藏密码的方式
    client = VDiskAPIClient('xiyoulaoyuanjia@gmail.com', 'yuanjia')
    client.post.auth__get_token()
    dir_id=client.post.dir__get_dirid_with_path(path = '/GetLink')['data']['id'] 

    uid=client.upload.file__upload_file(dir_id=dir_id,file=filename,cover='yes')['data']['fid']	

## 这里只能获得图片的下载地址?
    s3_url=client.post.file__get_file_info(fid=uid)['data']['s3_url']
    GetSrcToClipboard="echo \"" + s3_url+"\" |" " xclip -selection CLIPBOARD"

#print GetSrcToClipboard
###########
    os.system(GetSrcToClipboard)
    MessageGui.GetLinkExeGui(MessageGui.MessageGui_Right)
except:
    MessageGui.GetLinkExeGui(MessageGui.MessageGui_Error)		
sys.exit()

######利用其图形外壳Nautilus(对于GNOME有用)可以实现这一功能
#~/.gnome2/nautilus-scripts
## Nautilus 定义的一些变量
#NAUTILUS_SCRIPT_SELECTED_FILE_PATHS：用新行分开的所选文件的路径(除非是本地文件)
#NAUTILUS_SCRIPT_SELECTED_URIS：用新行分开的所选文件的 URI
#NAUTILUS_SCRIPT_CURRENT_URI：当前位置的 URI
#NAUTILUS_SCRIPT_WINDOW_GEOMETRY：当前窗口的位置和大小

#if __name__ =='__main__':
#	client = VDiskAPIClient('xiyoulaoyuanjia@gmail.com', '')
#	client.post.auth__get_token()
#	print	client.post.dir__get_dirid_with_path(path = '/GetLink') 
#	print	client.post.file__upload_file(file='lianxi1.txt',cover='yes',dir_id=0)	
#	print client.access_token
