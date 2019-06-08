#!/usr/bin/python3

import sys
from lightwave.lightwave import LWLink

#print('Number of arguments:', len(sys.argv), 'arguments.');
#print('Argument List:', str(sys.argv));

if len(sys.argv) < 3:
        print("Usage: lwrf <command> <dev> [<brightness>]")
        sys.exit()

cmd = sys.argv[1].upper();
dev = sys.argv[2];

lwLink = LWLink('192.168.1.96')

if cmd=='ON':
    print('On')
    lwLink.turn_on_light(dev, "")
elif cmd=='SWITCHON':
    print('SwitchOn')
    lwLink.turn_on_switch(dev, "")
elif cmd=='OFF':
    print('Off')
    lwLink.turn_off(dev, "")
elif cmd=="BRIGHT":
        print("Brightness")
        if len(sys.argv) != 4:
                print("Usage: lwrf <command> <dev> [<brightness>]")
                sys.exit()
        else:
                bright= sys.argv[3]
                lwLink.turn_on_with_brightness(dev, "", int(bright))
else:
        print("error, ", cmd)
