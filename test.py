import re
file1 = open("data_csv/input1.jpg.txt","r+")
data1 = str(file1.read())
data = re.sub(' +', ' ',data1)
data = data.split(' ')
data_no = re.sub(' +', ' ',data1).replace('\n','').replace('$','')
data_no = data_no.split(' ')
words = []
prices = []
avoids = ['tax','total','phone','price','discount','amount','amex','visa','change',':']
for j in range(len(data)):
    try:
        float(data[j])
        if str(float(data_no[j]))[-3] == '.':
            word = ''
            price = data_no[j]
            for i in np.arange(1,j):
                if '\n' not in data[(j-i)]:
                    word = word + " " + data_no[(j-i)]
                else:
                    words.append(word[1:])
                    print(word)
                    break
    except:
        x = 1

for i in range(len(words)):
    for avoid in avoids:
        if avoid in words[i].lower():
            words.pop(i)
print(words)
