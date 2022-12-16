import sys
def validate(ip):
    return False not in [int(ele) in range(256) for ele in (str(ip).split("."))]

ip = input("IPV4: ")
sys.exit(validate(ip))