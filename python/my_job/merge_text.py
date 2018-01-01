#!/usr/bin/python
#-*- coding: utf-8 -*-

import os

if os.path.isfile("merge_id.txt") == True:
    os.remove("merge_id.txt")

with open("peer_id.txt", "r") as f1:
    peer_id = f1.read().splitlines()

with open("route_id.txt", "r") as f2:
    route_id = f2.read().splitlines()

for num in range(len(peer_id)):
    if peer_id[num] != 'null':
        with open("merge_id.txt", "a") as f3:
            if num == len(peer_id) - 1:
                f3.write(route_id[num] + ' ' + peer_id[num])
            else:
                f3.write(route_id[num] + ' ' + peer_id[num] + "\n")