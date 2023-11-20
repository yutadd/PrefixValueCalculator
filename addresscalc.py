one=input("一つ目のアドレス:")
two=input("二つ目のアドレス:")
splited_one=one.split(".")
splited_two=two.split(".")
bin_one= [format(int(x),'b') for x in splited_one]
bin_two=[format(int(x),'b') for x in splited_two]
stacked_one=""
stacked_two=""
for o in bin_one:
    stacked_one+=o
for o in bin_two:
    stacked_two+=o
minlen=min([len(stacked_two),len(stacked_one)])
network_bits=0

for i in range(minlen):
    if(stacked_one[i]!=stacked_two[i]):
        break
    else:
        network_bits+=1
print(network_bits)