def get_network_bits(*ips):
    bins = [''.join(format(int(x), '08b') for x in ip.split('.')) for ip in ips]
    minlen = min(len(b) for b in bins)
    network_bits = sum(all(b[i] == bins[0][i] for b in bins) for i in range(minlen))
    return network_bits

ips = []
while True:
    ip = input("アドレスを入力してください（終了する場合は空白を入力）:")
    if ip:
        ips.append(ip)
    else:
        break

print(get_network_bits(*ips))
