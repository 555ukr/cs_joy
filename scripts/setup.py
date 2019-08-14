# import os
# f = os.popen("../joy/bin/joy bidir=1 dist=1 classify=1 \
# ../../pcap/133d773a8ca64c24bd81b594cf5240dd.pcap > malware.gz")
# now = f.read()
# print "Today is ", now

# $ ./sleuth malware.gz --select "da, dp, p_malware" --where "p_malware > 0.99"

import subprocess
# p = subprocess.Popen(["ping", "-c", "10", "www.cyberciti.biz"], stdout=subprocess.PIPE)
# output, err = p.communicate()
# print("*** Joy ***\n", output)
    # "bidir=1",
    # "dist=1",
    # "classify=1",
joy_command = [
    "../joy/bin/joy",
    "bidir=1",
    "dist=1",
    "classify=1",
    "./../pcap/133d773a8ca64c24bd81b594cf5240dd.pcap",
    ]
process = subprocess.Popen(joy_command, stdout=subprocess.PIPE,  stderr=subprocess.PIPE)
# code = process.wait()
code, err = process.communicate()
# print(err) 
# print(code) # 0