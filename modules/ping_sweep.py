# Attempts to ping sweep the specified CIDR addres space
modes = [""]

def name():
    return "ping-sweep"

def args():
    return ["address"]

def run(args):
    from subprocess import run, DEVNULL, PIPE
    proc = run(["nmap", "-PS", "-n", args.address], stdout=PIPE, stderr=PIPE)
    print(proc.stdout.decode("utf-8"))