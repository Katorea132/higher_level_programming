#!/usr/bin/python3
"""Modifies heap of a given process
"""
import sys


def Err_Exit():
    print("Usage: {} pid search_string replace_string". format(sys.argv[0]))
    exit(1)

if len(sys.argv) is not 4:
    Err_Exit()
pid, sstr, wstr = int(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3])
if pid <= 0 or sstr is "" or wstr is "":
    Err_Exit()

mappath, mempath = "/proc/{}/maps".format(pid), "/proc/{}/mem".format(pid)
print("[*] maps: {}\n[*] mem: {}".format(mappath, mempath))

with open(mappath, "r") as mapf:
    for line in mapf:
        w = line.split(' ')
        if w[-1][:-1] != "[heap]":
            continue
        print("[*] Found [heap]:")

        addr, perm, offs, devi, inode = w[0], w[1], w[2], w[3], w[4]
        pathi = w[-1][:-1]
        print("\tpathname = {}".format(pathi))
        print("\taddresses = {}".format(addr))
        print("\tpermisions = {}".format(perm))
        print("\toffset = {}".format(offs))
        print("\tinode = {}".format(inode))

        if "r" not in perm or "w" not in perm:
            print("No permissions for {}".format(pathi))
            break
        addr = addr.split("-")
        if len(addr) is not 2:
            print("Wrong format for address")
            break
        addrstart = int(addr[0], 16)
        addrend = int(addr[1], 16)
        print("\tAddr start [{:x}] | end [{:x}]".format(addrstart, addrend))

        with open(mempath, "rb+") as memf:
            memf.seek(addrstart)
            heap = memf.read(addrend - addrstart)
            try:
                i = heap.index(bytes(sstr, "ASCII"))
            except:
                print("Can't find '{}'".format(sstr))
                break
            print("[*] Found '{}' at {:x}".format(sstr, i))

            print("[*] Writing '{}' at {:x}".format(wstr, addrstart + i))
            memf.seek(addrstart + i)
            memf.write(bytes(wstr, "ASCII"))
