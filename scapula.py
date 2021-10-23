import random

clavicula = [0, 
'Margo lateralis',
'Margo medialis',
'Margo superior',
'Angulus superior',
'Angulus inferior',
'Facies costalis',
'Facies dorzalis',
'Spina scapulae',
'Fossa supraspinata',
'Fossa infraspinata',
'Acromion',
'Processus coracoideus ',
'Cavitas glenoidalis ',
'Tuberculum supraglenoidale ',
'Tuberculum infraglenoidale ',
'Incisura scapulae']

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
        