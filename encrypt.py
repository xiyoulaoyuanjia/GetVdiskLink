#!/usr/bin/python

from Crypto.PublicKey import RSA



def encrypt(text="abcd"):
	pub = open("/home/yuanjia/.ssh/id_rsa.pub").read()	
	key = RSA.importKey(pub)
	return key.encrypt(text,None)[0]

def decrypt(cipher_text='"EE\xa0\xd3\xdbyy$TL\x1d\x02T\xb2\xe7\n\'\xb34@\x82C\xf8}"\x9f0\xeb\x92\x11\x90\x00%\xbd\xfb\xd2\x0f\xfcd\xf13\xa0b`\x96\xfdI\xac,\x85\xd3\xd7\xb7;\x08\xab\xc5\x15d\xf7\xe4\x82\xfd\xaaI\xaf\xa7\x0eI\x84O\x1b\xda\xea-\x9d@\x89\xc8\xa3\x19\xd9\x9f\xac\xaf\xdf\xa0\xed\x80\xd0\xaff\x03QJ1\x9c\x90;\xde\xf3\xa2R\xb4R\x08e\x1d\xfd\xcd/}\xb8V\xab\x9e\x10G\xb5\xa8\xd7\xaeM\x8b\x92\x06>\xeawnG=\xf6&\xff\x1e\x14\x15\xe13\xd8&\xd1\x7fB\xf1w%\x07Y%\xbe4y\xf7\r\xb1\x00q@# \x85_\x95\xcf\xd8\x89\xaf\xbc\xf9`\xb7\x8d0t\x049\xbe\x02\xe7\xa46KS\xbd\x02m_R\x16f6Q\xee\xa0E\xc1w#\x81{r\xbb\x7f\xa2Q\xc4"\x84\x7f\ru\xb6\xd3$\t]\x8b\x16\xc2n\x86\x9cI\xc6\xc5\x90\xaa7S\x91\xe2/W\x83A\x8aq\xb6\x13\xab\x81` (P\x16\x1f\xf0j\xc4\x95\xe5d\x9f"'):
	id_rsa = open("/home/yuanjia/.ssh/id_rsa").read()
	cipher=RSA.importKey(id_rsa)
	return cipher.decrypt(cipher_text)

if __name__ == '__main__':
	text="\x88\x85\xda\xef\xc3\xfa^=\x99\xbf\x9c==0\xae@\xc7jcs9\x7f\x99N\x19o\xce\xd9\x01\xd7P\xe1%r.<\x04\xf6\xf9\xc3\xcb\xf4/\x86\xa5\xb6Ndm\xeeE\xa1\xfd>L\xcb's\x1d\x03i\xe9x\x00\xe9\xc2ETu\xa6f\xc3\xeb\x9b\x05v\x07g,\x1c5JK@\x16\x99Y\x14\xb0\x81\xf0AS>?\xd9;o\xfdS\x14^\xd2\xf6VFV\xa9FoD\x8b:\xf3\xe9\xbe\xfe\xae\xe9C\xe0\xb7w~+N\xd8\xff\xba\x99\rO\xffp\xa5e8+u\x90ok<dq\x95\x9b\xe8\xc8\xec\x13Mkf\x82?\xc2\x98\xfd\xe6\xea\xb7\xfd\xd2\x0f\xf4\xdfH\xcd\x0bL\x0bE\xeb\xbfq\x85usA\xf2\xef\x95Ha\xf9\x0f\xac\xce\n5\xc0\xfb\x87\x8f\x8c\xc7\x07|\x15\x81\xab!`t\x0e\xb4H\x05p\xc3\xd2\xbb{.\x95\x13\x07\xa0de\x81\xa9\xf0\x97=\xd3\xc4\xccR2\xcb\x03Z\xea\n^\xc4\xb0;\xcf\x92\xf1\xcc\xa1\xb8\xd4\x063F\xf0\xcca\x87\xc1\x89"
	print decrypt(text)
