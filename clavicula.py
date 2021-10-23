import random

clavicula = [0, 'Corpus claviculae',
'Extremitas sternalis',
'Facies articularis sternalis',
'Extremitas acromialis',
'Facies articularis acromialis',
'Tuberositas ligamenti coracoclavicularis',
'Tuberculum conoideum']

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
        