#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@youngsummerlight
'''


# import threading

import os
from multiprocessing.pool import ThreadPool
from time import sleep

p = ThreadPool(10)
spisok = []

with open('hosts.txt', 'r') as f:
    spisok = f.read().splitlines()


def get_ping(ipaddr):
    response = os.system("ping -c 1 " + ipaddr + "> /dev/null")
    if response == 0:
        print(ipaddr + "Host is up!")
#        sleep(120)
    else:
        print(ipaddr + "Host is down")
#        sleep(5)



# for nomer, ipaddr in enumerate(urls):
#     threading.Thread(target = get_ping, args = [nomer+1, ipaddr]).start()

for ipaddr in spisok:
	p.apply_async(get_ping, args=(ipaddr,))


p.close()
p.join()
