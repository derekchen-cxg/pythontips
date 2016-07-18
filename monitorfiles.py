#/usr/bin/env python
import re
import logging
log_filename='monitorgateway_log'
log_format='%(asctime)s [%(filename)s] %(message)s'
logging.basicConfig(filename=log_filename,filemode='a',format=log_format,datefmt='%Y-%m-%d %H:%M:%S %p',level=logging.DEBUG)
f_w=open('gateway.txt','a')
f_z=open('gateway.txt','r+')
l=['192.168.121.1\n','192.168.122.1\n']
count_g1=0
count_g2=0
for line in open('1.txt'):
    g1=re.findall('192.168.121.1',line)
    g2=re.findall('192.168.122.1',line)
    count_g1=count_g1 + len(g1)
    count_g2=count_g2 + len(g2)
if count_g1==0 and count_g2==0:
    f_z.writelines(l)
    f_z.close()
    logging.warn('gateway.txt add 192.168.121.1,192.168.122.1')
elif count_g1==0 and count_g2>0:
    f_w.write('192.168.121.1\n')
    f_w.close()
    logging.warn('gateway.txt add 192.168.121.1')
elif count_g1>0 and count_g2==0:
    f_w.write('192.168.122.1\n')
    f_w.close()
    logging.warn('gateway.txt add 192.168.122.1')