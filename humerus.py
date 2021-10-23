import random

clavicula = [0, 
'Caput humeri',
'Collum anatomicum humeri' ,
'Tuberculum majus' ,
'Tuberculum minus',
'Collum chirurgicum humeri' ,
'Sulcus intertubercularis' ,
'Corpus humeri',
'Tuberositas deltoidea',
'Sulcus nervi radialis ',
'Epicondylus medialis ',
'Epicondylus lateralis ',
'Trochlea humeri (ulna) ',
'Capitulum humeri (radius)' ,
'(Fossa radialis)',
'(Fossa coronoidea)' ,
'Sulcus nervi ulnaris',
'Fossa olecrani',
'130° ',
'20° vzad']

while True: 
    i = random.randrange(1, len(clavicula))
    if (clavicula[i]==0):
        continue
    print(i,end='')
    input('')
    print(clavicula[i])
    ot = input('')
    print('------------------------')
    if (ot == ''):
        clavicula[i]=0
    if (ot == 'no'):
        print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();print(); print();
        