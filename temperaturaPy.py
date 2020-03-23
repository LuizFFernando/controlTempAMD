import glob   
import time
cont = 0
cont1 = 0
graus = 0
#funçao para ver o valor em  porcentagem  das temperatura
def porcentagem(number):
    output = number / 255
    output = output * 100
    #output = recebe_arg / 100
    return output
#funçao manda valor ja formulado para arq drm e seta intencidade dos cules
def manda_temp(number):
    output = number / 310 #340 
    output = int(output)
    return output

array = [ ]
temp = ''
for i in glob.glob("/sys/class/drm/card?/device/hwmon/hwmon?/pwm1_enable"): #isso iria listar diretorios e setar 1 no arq pwmi enable
    with open(i, 'w') as f:
        f.write('1')
for i in glob.glob("/sys/class/drm/card?"):      #isso ira listar diretorios conta quantas gpus tem
    i = str(i[15:23])
    print (i)
    #print (type(i))
    #cont = cont + 1
    array.append(i)
    time.sleep(1)
    cont1 = cont1 +1      
while True:

    for i in glob.glob("/sys/class/drm/card?/device/hwmon/hwmon?/temp1_input"):      #isso iria listar diretorios
        with open(i, 'r') as d:
            for y in d:
                #print (y)
                y = int(y)
                graus = str(y)
                graus = graus[0:2]
                #print (type(y))   
                temp = manda_temp(y) #funcao funçao manda valor ja formulado para arq drm e seta intencidade dos cules
                porcent = porcentagem(temp) #funçao para ver o valor em  porcentagem  das temperatura
                porcent = int(porcent)
                temp = str(temp)
               
                print('mandando dados - ', array[cont], graus,'C', ' ', 'FAN',  porcent,'%')
                cont = cont + 1
                if cont == cont1:
                    cont = 0
                i = i[0:41]
    
                with open(i+'pwm1', 'w') as f:
                    f.write(temp)
                
                    print('contando........')
                    time.sleep(5)

 