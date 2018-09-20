mock_show_vrf = '''
  Name                             Default RD            Protocols   Interfaces
  MGMT                             <not set>             ipv4        Gi0/0
'''

mock_show_ip_arp = '''
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.121.1           0   5254.00a4.4ed8  ARPA   GigabitEthernet0/0
Internet  192.168.121.221         -   5254.0023.79f0  ARPA   GigabitEthernet0/0
'''

mock_show_interfaces = '''
GigabitEthernet0/0 is up, line protocol is up 
  Hardware is iGbE, address is 5254.0023.79f0 (bia 5254.0023.79f0)
  Description: vagrant-management
  Internet address is 192.168.121.221/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 171/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto Duplex, Auto Speed, link type is auto, media type is RJ45
  output flow-control is unsupported, input flow-control is unsupported
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 1000 bits/sec, 2 packets/sec
  5 minute output rate 1000 bits/sec, 1 packets/sec
     982 packets input, 80623 bytes, 0 no buffer
     Received 559 broadcasts (0 IP multicasts)
     1094 runts, 0 giants, 0 throttles 
     1094 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     391 packets output, 52753 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     1 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
GigabitEthernet0/1 is administratively down, line protocol is down 
  Hardware is iGbE, address is 28b7.ada8.3874 (bia 28b7.ada8.3874)
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto Duplex, Auto Speed, link type is auto, media type is RJ45
  output flow-control is unsupported, input flow-control is unsupported
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
'''

mock_show_ip_protocols_summary = '''
0     connected
1     static
2     application
*** IP Routing is NSF aware ***
'''

mock_show_ip_route = '''
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR

Gateway of last resort is 192.168.121.1 to network 0.0.0.0

S*    0.0.0.0/0 [254/0] via 192.168.121.1
      1.0.0.0/32 is subnetted, 1 subnets
S        1.1.1.1 [1/0] via 192.168.121.1
      9.0.0.0/32 is subnetted, 1 subnets
S        9.9.9.9 is directly connected, GigabitEthernet0/0
      192.168.121.0/24 is variably subnetted, 3 subnets, 2 masks
C        192.168.121.0/24 is directly connected, GigabitEthernet0/0
S        192.168.121.1/32 [254/0] via 192.168.121.1, GigabitEthernet0/0
L        192.168.121.221/32 is directly connected, GigabitEthernet0/0
'''

mock_show_ip_route_static = '''
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR

Gateway of last resort is 192.168.121.1 to network 0.0.0.0

S*    0.0.0.0/0 [254/0] via 192.168.121.1
      1.0.0.0/32 is subnetted, 1 subnets
S        1.1.1.1 [1/0] via 192.168.121.1
      192.168.121.0/24 is variably subnetted, 3 subnets, 2 masks
S        192.168.121.1/32 [254/0] via 192.168.121.1, GigabitEthernet0/0
'''

mock_show_version = '''
Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.6(1)T, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2015 by Cisco Systems, Inc.
Compiled Fri 20-Nov-15 13:39 by prod_rel_team


ROM: Bootstrap program is IOSv

iosv uptime is 19 minutes
System returned to ROM by reload
System image file is "flash0:/vios-adventerprisek9-m"
Last reload reason: Unknown reason



This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

Cisco IOSv (revision 1.0) with  with 484609K/37888K bytes of memory.
Processor board ID 9F5AD57IY1430DLTI5483
2 Gigabit Ethernet interfaces
DRAM configuration is 72 bits wide with parity disabled.
256K bytes of non-volatile configuration memory.
2097152K bytes of ATA System CompactFlash 0 (Read/Write)
0K bytes of ATA CompactFlash 1 (Read/Write)
0K bytes of ATA CompactFlash 2 (Read/Write)
0K bytes of ATA CompactFlash 3 (Read/Write)



Configuration register is 0x0
'''

mock_dir = '''
Directory of flash0:/

    1  drw-           0  Jan 30 2013 00:00:00 +00:00  boot
  264  drw-           0  Oct 14 2013 00:00:00 +00:00  config
  267  -rw-   142648944  Nov 20 2015 00:00:00 +00:00  vios-adventerprisek9-m
  270  -rw-      524288   May 7 2018 06:12:56 +00:00  nvram
  271  -rw-          19   May 7 2018 06:13:24 +00:00  e1000_bia.txt

2142715904 bytes total (1994932224 bytes free)
'''

