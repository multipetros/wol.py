# wol.py - version 1.1
Copyright (c) 2013 - Petros Kyladitis

---

Description
===========
A simple Python cli magic packet sender for WOL enabled devices.
For more info and updates see at <http://www.multipetros.gr/>.

Usage
=====
`wol.py [-h] [-b BROADCAST_ADDRESS] [-p PORT_NUM] MAC_ADDRESS`

Manual
======
Send WOL magic packet to the selected MAC destination

Positional arguments
--------------------
* `MAC_ADDRESS`
  => The MAC address of the machine you want to send the magic packet. Digits could be separated by `:` or `-`

Optional arguments
------------------
* `-h`, `--help` 
  => show help message and exit
* `-b BROADCAST_ADDRESS`, `--broadcast BROADCAST_ADDRESS`
  => The network broadcast address, in dotted format: www.xxx.yyy.zzz
* `-p PORT_NUM`, `--port PORT_NUM`
  => The listening port usually 7 or 9. (By default, the program use port 9)

Lisence
=======
This program is free software distributed under the FreeBSD license,
for license details see at 'LICENSE' file, distributed with
this program, or see at <http://www.multipetros.gr/freebsd-license/>.