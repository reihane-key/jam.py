temp=input('vazn ra varaed kon')
vazn=int(temp)
temp=input('mozd sakht ra varaed kon')
mozd=int(temp)
temp=input('malit ra varaed kon')
maliat=int(temp)
temp=input('gheimt roozra varaed kon')
gheimat=int(temp)
temp=input('sood ra varaed kon')
sood=int(temp)
gheimatkham=vazn*gheimat
soodtala=gheimatkham*sood/100
mozdsakht=gheimatkham*mozd/100
meghdarmaliat=(sood+mozdsakht)*maliat/100
majmoo=gheimatkham+soodtala+mozdsakht+meghdarmaliat
print(f"jamkol{majmoo:,}")
