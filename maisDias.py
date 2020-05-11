from datetime import datetime
#definindo datas com int
print('Este programa calcula os dias de vida de uma pessoa')
print()


dia=input('Digite data de nascimento : \ndd/mm/aaaa   : ')
vetor_dia=dia.split('/')
data_hoje=datetime.today()

#primeiro calculo qtd de dias pela diferença de anos
dias_anos=(int(data_hoje.year)-int(vetor_dia[2])-1)*365

#somando dias para anos bissextos
count=0
for i in range(int(vetor_dia[2]),int(data_hoje.year)):
    if i%4==0:
        #print(i)
        count+=1
#print(dias_anos)        
dias_anos+=count

#print(dias_anos)
count=0
#definindo qtd dias mes nasc
dias_mes_nasc=0
if int(vetor_dia[1])==1 or int(vetor_dia[1])==3 or int(vetor_dia[1])==5 or int(vetor_dia[1])==7 or int(vetor_dia[1])==8 or int(vetor_dia[1])==10 or int(vetor_dia[1])==12 :
    dias_mes_nasc=31-int(vetor_dia[0])+1
elif int(vetor_dia[1])==4 or int(vetor_dia[1])==6 or int(vetor_dia[1])==9 or int(vetor_dia[1])==11 :
    dias_mes_nasc=30-int(vetor_dia[0])+1
else:
    if int(vetor_dia[2])%4==0:
        dias_mes_nasc=29-int(vetor_dia[0])+1 
    else:
        dias_mes_nasc=28-int(vetor_dia[0])+1    

#calculando dias por meses ano nascimento
dias=0
for i in range(int(vetor_dia[1])+1,13):
    if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12 :
        dias+=31
        #print(31)
    elif i==4 or i==6 or i==9 or i==11 :
        dias+=30
        #print(30)
    else:
        if int(vetor_dia[2])%4==0:
            dias+=29
            #print(29) 
        else:
            dias+=28                 

#calculando dias corridos do ano atual
maisDias=0
for i in range(1,int(data_hoje.month)):
    if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12 :
        maisDias+=31
        #print(31)
    elif i==4 or i==6 or i==9 or i==11 :
        maisDias+=30
        #print(30)
    else:
        if int(data_hoje.year)%4==0:
            maisDias+=29
            #print(29) 
        else:
            maisDias+=28       

#qtd de dias de vida é a soma dos resultados de :
#dias_anos - qtd de dias entre ano Nasc e ano At
#dias_mes_nasc - qtd de dias vividos no mes de nascimento
#dias - qtd de dias somando qtd de meses vividos no ano de nascimento
#maisDias - dias vividos nos meses do ano At
#diaAt - dias do mes corrente
dias_de_vida = dias_anos + dias_mes_nasc + dias + maisDias + int(data_hoje.day)

#definindo dias até o aniversario
niver=366-(maisDias+int(data_hoje.day))-(dias+dias_mes_nasc)
if int(data_hoje.month)<3 and int(data_hoje.day)<29 and int(data_hoje.year)%4==0:
    niver+=1

print()
print('Vc tem '+str(dias_de_vida)+' dias de vida!!')
#deifindo e printando horas vividas
print('Vc viveu '+str(dias_de_vida*24)+' horas ')
#definindo e printando minutos vividos
print('E '+str((dias_de_vida*24)*60)+' minutos')
print('Faltam '+str(niver)+' dias para seu niver')
print('Fim do programa')
print()