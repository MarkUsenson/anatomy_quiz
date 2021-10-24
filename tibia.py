import random

clavicula = [0, 
'Tibia',
'eminentia intercondylaris', 
'condylus med.',
'condylus lat.', 
'facies articularis fibularis', 
'tuberositas tibiae', 
'linea musculi solei', 
'malleolus med.', 
'sulcus malleolaris', 
'facies articularis malleoli medialis']

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
        