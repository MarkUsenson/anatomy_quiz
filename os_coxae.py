import random

clavicula = [0, 
'Cingulum membri inferioris',
'Os coxae ',
'Os ilium ',
'Os ischii',
'Os pubis',
'acetabulum', 
'facies lunata', 
'fossa acetabuli', 
'corpus ossis ilii', 
'ala ossis ilii', 
'crista iliaca', 
'spina iliaca anterior superior', 
'spina iliaca posterior superior', 
'spina iliaca anterior inferior', 
'spina iliaca posterior inferior',  
'fossa iliaca', 
'facies auricularis', 
'tuberositas iliaca', 
'linea arcuata', 
'facies glutea', 
'corpus ossis pubis', 
'foramen obturatum', 
'ramus superior ossis pubis', 
'ramus inferior ossis pubis',
'facies symphisialis', 
'pecten ossis pubis', 
'ramus ossis ischii', 
'tuber ossis ischii', 
'incisura ischiadica minor', 
'incisura ischiadica major', 
'incisura acetabuli',
'spina ischiadica'
]

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
        