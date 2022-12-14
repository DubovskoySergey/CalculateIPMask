import ipaddress
import sys

def getMask(diap_ip):
    masks = {1 : 32, 2 : 31, 4 : 30, 8 : 29, 16 : 28, 32 : 27, 64 : 26, 128 : 25, 255:24, 510:23, 1020:22, 2048:21, 4096:20, 8192:19, 16384:18, 32768:17, 65536:16, 131072 : 15, 262141 : 14, 524288 : 13, 1048576 : 12, 2097152 : 11, 4194304 : 10, 8388608 : 9, 16777216 : 8}
    first_ip = diap_ip.split('-')[0] 
    last_ip = diap_ip.split('-')[1] 
    
    start_ip = ipaddress.IPv4Address(first_ip) 
    end_ip = ipaddress.IPv4Address(last_ip) 
    result = int(end_ip) - int(start_ip) 
    key = list(masks.keys()) 
    ind = 0 
    while key[ind] < result: 
        ind += 1 
    
    mask = key[ind]
    result_ip = first_ip + "\\" + str(masks[mask])
    return result_ip

def readFile(file):
    with open(file) as file:
        ip = file.readlines()
    return ip

def writeFile(ip):
    with open('result.txt', 'a') as file:
        file.write(ip + "\n")

def main():
    file = sys.argv[1]
    ip_list = readFile(file)
    i = 0
    for ip in ip_list:
        ip = ip.strip("\n")
        ipMask = getMask(ip)
        writeFile(ipMask)
        print(str(i) + "\\" + str(len(ip_list)) + ":", ipMask)
        i += 1

if __name__ == "__main__":
    main()