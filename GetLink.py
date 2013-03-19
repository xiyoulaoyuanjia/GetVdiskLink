#!/usr/bin/env python
# -*- coding: utf-8 -*-


from vdisksdk import * 
import os

client = VDiskAPIClient('xiyoulaoyuanjia@gmail.com', 'yuanjia')
client.post.auth__get_token()
dir_id=client.post.dir__get_dirid_with_path(path = '/GetLink')['data']['id'] 

curl="curl -F file=@"+"lianxi1.txt" + " -F token="+client.access_token+ " -F cover=yes " + "-F dir_id="+dir_id+" \"http://openapi.vdisk.me/?m=file&a=upload_file\""

#print curl
os.system(curl)
# 这块有问题？
#	print	client.post.file__upload_file(file='lianxi1.txt',cover='yes',dir_id=0)	

#if __name__ =='__main__':
#	client = VDiskAPIClient('xiyoulaoyuanjia@gmail.com', 'yuanjia')
#	client.post.auth__get_token()
#	print	client.post.dir__get_dirid_with_path(path = '/GetLink') 
#	print	client.post.file__upload_file(file='lianxi1.txt',cover='yes',dir_id=0)	
#	print client.access_token
