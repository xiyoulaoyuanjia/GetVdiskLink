#!/usr/bin/env python
# -*- coding: utf-8 -*-


from vdisksdk import * 
from encrypt import *
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
### 
    user="\x88\x85\xda\xef\xc3\xfa^=\x99\xbf\x9c==0\xae@\xc7jcs9\x7f\x99N\x19o\xce\xd9\x01\xd7P\xe1%r.<\x04\xf6\xf9\xc3\xcb\xf4/\x86\xa5\xb6Ndm\xeeE\xa1\xfd>L\xcb's\x1d\x03i\xe9x\x00\xe9\xc2ETu\xa6f\xc3\xeb\x9b\x05v\x07g,\x1c5JK@\x16\x99Y\x14\xb0\x81\xf0AS>?\xd9;o\xfdS\x14^\xd2\xf6VFV\xa9FoD\x8b:\xf3\xe9\xbe\xfe\xae\xe9C\xe0\xb7w~+N\xd8\xff\xba\x99\rO\xffp\xa5e8+u\x90ok<dq\x95\x9b\xe8\xc8\xec\x13Mkf\x82?\xc2\x98\xfd\xe6\xea\xb7\xfd\xd2\x0f\xf4\xdfH\xcd\x0bL\x0bE\xeb\xbfq\x85usA\xf2\xef\x95Ha\xf9\x0f\xac\xce\n5\xc0\xfb\x87\x8f\x8c\xc7\x07|\x15\x81\xab!`t\x0e\xb4H\x05p\xc3\xd2\xbb{.\x95\x13\x07\xa0de\x81\xa9\xf0\x97=\xd3\xc4\xccR2\xcb\x03Z\xea\n^\xc4\xb0;\xcf\x92\xf1\xcc\xa1\xb8\xd4\x063F\xf0\xcca\x87\xc1\x89"
    passwd='\xa0<J5\x18\x8a\x19FNA\x9a\x8c>\t\xcfv\x98\x99/\x8c\xf7\xac2\xc4\x98 k\xee+W\xb1pX\x98c$\xbd3}F\xf7/\xe6nH\xd4\xf8&\x8b\xa5\xd3,>\xdd%+s4]Yp\x04\xe5\r4\x034a\x0c1tS\xb5\xdb\x02.\x95\xfdP\xf6\xc5\xab\xe9:p\x1b\x9f\x0f"\x98[I\x9d\xeb\xed\xf4H{\x11 \x13\xc0]\x80\xc3\xc8ga~ \xde\xbeV\xb0/\xae\xc8oZ\xe1\xc4\xf8\xc1\xab\xcf\xdf}V\x14\x95\x86a\xf7\x1eJ\xc6:I\xcb\x16\xaa\xbb\xe5\x8b\xfb\xfdbO\xb8h@\xa4\x1e\xacFG\xf2O\x88\x7f\xdd\x9c\xf5\x12\x1c(\xeeA?t\xd9k\xbc\xb7)\xb5k\xceO\xe8\x1b\x9a#6\x96\xfc)W\xa2L\xeeM+\xd4\xbe\xf9\x8f\x98^\x01a\xd6\xeb\xe20Gc\xfb]m&&\xe3\xc9\xa9y\r\x0c\xfat\xd8?86g\xe0\x83(zcE}\xb6F4\x9e\'E\x04ot\xf5\x1d\x88#\x865\xa1\x9f\xf6\x8f\xe4k\x83.:'
    client = VDiskAPIClient(decrypt(user), decrypt(passwd))
    client.post.auth__get_token()
    dir_id=client.post.dir__get_dirid_with_path(path = '/GetLink')['data']['id'] 
#    uid=client.upload.file__upload_file(dir_id=dir_id,file=filename,cover='yes')['data']['fid']	
#    uid=client.upload.file__upload_share_file(dir_id=dir_id,file=filename,cover='yes')['data']['fid']	
    download_page=client.upload.file__upload_share_file(dir_id=dir_id,file=filename,cover='yes')['data']['download_page'] 
## 这里只能获得图片的下载地址?
#    print client.post.file__get_file_info(fid=uid)['data']
#    s3_url=client.post.file__get_file_info(fid=uid)['data']['s3_url']
#    print client.post.file__get_file_info(fid=uid)['data']
#    url=client.post.file__get_file_info(fid=uid)['data']['url']
#    shareUrl="http://vdisk.weibo.com/share/embedImage?file="+url.split("/")[-1]
# urlparse.urlparse("http://vdisk.weibo.com/s/unRPX").path.split('/',)
    GetSrcToClipboard="echo -n \"" + download_page+"\" |" " xclip -selection CLIPBOARD"

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
