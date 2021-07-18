# Projeto 01  Detetive

per1 = input('"Você telefonou para a vítima?\n S/N: ')
per2 = input('Você esteve no local do crime?\n S/N: ')
per3 = input('"Você mora perto da vítima?\n S/N: ')
per4 = input('Você devia para a vítima?\n S/N: ')
per5 = input('Você já trabalhou com a vítima?\n S/N: ')

per1_ref = per1.strip().replace(' ','').replace('s','S').replace('n','N').replace('a','ã')
per2_ref = per2.strip().replace(' ','').replace('s','S').replace('n','N').replace('a','ã')
per3_ref = per3.strip().replace(' ','').replace('s','S').replace('n','N').replace('a','ã')
per4_ref = per4.strip().replace(' ','').replace('s','S').replace('n','N').replace('a','ã')
per5_ref = per5.strip().replace(' ','').replace('s','S').replace('n','N').replace('a','ã')

val_res1 = 0
val_res2 = 0
val_res3 = 0
val_res4 = 0
val_res5 = 0

if per1_ref == 'Sim':
    val_res1= 1
elif per1_ref == 'Não':
    val_res1 = 0
if per2_ref == 'Sim':
    val_res2 = 1
elif per2_ref == 'Nâo':
    val_res2 = 0
if per3_ref == 'Sim':
    val_res3= 1
elif per3_ref == 'Nâo':
    val_res3 = 0
if per4_ref == 'Sim':
    val_res4 = 1
elif per4_ref == 'Nâo':
    val_res4 = 0
if per5_ref == 'Sim':
    val_res5 = 1
elif per5_ref == 'Nâo':
    val_res5 = 0
else:
    print('Apenas responda o que eu te perguntei e seja totalmente sincero.')

soma = (val_res1+val_res2+val_res3+val_res4+val_res5)
print()
if soma <= 1:
    print('Eu sabia, você é inocente')
elif soma == 2:
    print('Você é suspeito(a)')
elif soma == 3 and 4:
    print('Você é suspeito(a)')
elif soma == 5:
    print('Eu tinha certeza que você era o(a) assasino(a)')

print()
print('Fim da investigação')
