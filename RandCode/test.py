#!/usr/bin/env python
# coding:utf8
import RandCode

r = RandCode.RandCode('385511200000000000', '315c4c6c0810e6c3701e5565d12e1c2b')
s = r.send('18907310000', 'http://open.189.cn/rand_code.php', '3')
if s == True:
	print 'succeed'
else:
	print 'failed'
