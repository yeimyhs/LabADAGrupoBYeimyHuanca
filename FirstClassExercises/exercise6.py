#name = input('What is your name?\n')
print("ejercicio6")
word = input("word:")
simb='*'
marco ='*'
relleno = '*'
num= int(input("number:"))
#marco=(simb*len(word))+(num*simb)+(simb*2)
for j in range(len(word)+((num)*2)):
  marco+='*'
marco+=simb
for i in range(len(word)+((num)*2)):
  relleno+=' '
relleno+=simb
relleno+=('\n'+relleno)*(num-1)
word = simb+(' '*num)+word+(' '*num)+simb

print (marco)
print (relleno)
print (word)
print (relleno)
print (marco)