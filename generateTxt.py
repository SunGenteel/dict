import json


with open('book/GaoZhongluan_2.json', 'r') as f:
  lines = f.read().strip().split('\n')
  print(len(lines))


def transform(line):
    data = json.loads(line)
    content = data['content']['word']['content']

    phone = content.get('usphone')
    if phone is None:
        phone = content.get('phone')
    if phone is None:
        # phone = content.get('ukphone')
    # if phone is None:
        phone = ''
    # transEn = '';
    # transCn = ''
    # if content.get('trans'):
    #     for trans in content['trans']:
    #         if trans.get('tranOther'):
    #             transEn += trans['tranOther'];
    #         if trans.get('tranCn'):
    #             transCn += trans['tranCn'];
    # wordDict['transEn'] = transEn
    # wordDict['transCn'] = transCn

    # print(data['headWord'] + ", " + phone + ", " + transEn + ", " + transCn + "\n")
    # print(data['headWord'] + ", " + phone + "\n")
    return str(data['headWord']).ljust(10) + str("   [" + phone+"]").ljust(25)






# open file in write mode
wordsInOneLine = 3;
count=0;
with open(r'book-gen/GaoZhongluan_2.csv', 'w') as fp:
    for line in lines:
        # write each item on a new line
        count = count + 1
        if count % 3 ==0 :
            fp.write( transform(line) + "\n" )
        else:
            fp.write(transform(line) + ",")
    print('Done')

# f = open("book-txt/GaoZhongluan_2.txt", "a")
# f.write(wordList)
# f.close()