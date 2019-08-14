import subprocess

result = subprocess.run("../joy/bin/joy bidir=1 bidir=1 classify=1 ../pcap/133d773a8ca64c24bd81b594cf5240dd.pcap > mal.gz",  shell=True)
print(result.returncode)