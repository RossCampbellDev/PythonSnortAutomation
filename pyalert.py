#!/usr/bin/python3
import subprocess
import shlex
import pexpect
import re

# cmd="sudo snort -A console -c /etc/snort/snort.conf -q -i eth0"
# args=shlex.split(cmd)
cmdlist=["sudo", "snort", "-A console", "-c /etc/snort/snort.conf", "-q", "-i eth0"]
args=' '.join(cmdlist)

IPregex = '^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}$'

p = pexpect.spawn(args)

try:
  while True:
    p.expect('->') # wait for any kind of alert (the arrow is always present, showing src/dst)
    alert = p.before.decode('utf-8') # get data that came just before the expected output ('->')
    print(alert)
    IPs = re.search(IPregex, alert)
    print(IPs)
except KeyboardInterrupt:
  print("Cancelled process")
finally:
  p.close(force=True)
