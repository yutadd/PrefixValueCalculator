def get_network_bits(*ips):
    bins = [''.join(format(int(x), '08b') for x in ip.split('.')) for ip in ips]
    minlen = min(len(b) for b in bins)
    networkbits=0
    for i in range(minlen):
        model_bit=bins[0][i]
        for _bin in bins:
            if model_bit!=_bin[i]:
                return networkbits
        networkbits+=1
    return networkbits

ips = []
while True:
    ip = input("アドレスを入力してください（終了する場合は空白を入力）:").strip()
    if ip:
        ips.append(ip)
    else:
        break

print(get_network_bits(*ips))
