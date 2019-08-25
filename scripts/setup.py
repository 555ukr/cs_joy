import subprocess
import json

def createJson(str):
    output = []
    for line in str.split('\n'):
        try:
            print(line)
            dict = json.loads(line)
            output.append(dict)
        except ValueError:
            pass
    # print(output)

def readPcap():
    result = subprocess.run("../joy/bin/joy bidir=1 tls=1 bidir=1 classify=1 \
                ../pcap/133d773a8ca64c24bd81b594cf5240dd.pcap > mal.gz",  shell=True)
    if result.returncode == 0:
        process = subprocess.run(" ../joy/sleuth ../scripts/mal.gz \
                                --select 'da, dp, p_malware, sa' \
                                --where 'p_malware > 0.91'",
                                shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        createJson(str(process.stdout, "utf-8"))
    else:
        print("Error")

def tlsLength():
    result = subprocess.run("../joy/bin/joy bidir=1 tls=1 bidir=1 classify=1 dns=1 \
                ../pcap/capture.pcap > capture.gz",  shell=True)
    if result.returncode == 0:
        process = subprocess.run(" ../joy/sleuth ../scripts/capture.gz \
                                --select 'tls{s_cert[{signature_key_size,signature_algo}]}, da' \
                                --where 'tls{s_cert[{signature_key_size}]}<2048'",
                                shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        createJson(str(process.stdout, "utf-8"))
    else:
        print("Error")

def allFingerprint():
    result = subprocess.run("../joy/bin/joy fpx=1  \
                ../pcap/capture.pcap > full.gz",  shell=True)
    if result.returncode == 0:
        process = subprocess.run("../joy/sleuth --select 'fingerprints'  \
                full.gz > lol.json", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        createJson(str(process.stdout, "utf-8"))


if __name__ == "__main__":
    allFingerprint();
