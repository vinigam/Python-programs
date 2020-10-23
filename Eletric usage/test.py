flag = True
flag_home = False
flag_res = False
vezes = 0
consumidor = []
quilo_total = 0
quilo_total_res_home = 0
while(flag):
  codigo, quilowatts = map(int, input().split())

  if codigo == 0 :
    flag = False
  else:
    
    if codigo == 1 :
      vezes = vezes + 1
      if flag_home == False:
        flag_home = True
      if quilowatts > 200:
        consumidor.append(0.85*quilowatts)
        quilo_total = quilo_total + quilowatts
        quilo_total_res_home = quilo_total_res_home + quilowatts
       
      else:
        quilo_total = quilo_total + quilowatts
        consumidor.append(0.60*quilowatts)
        quilo_total_res_home = quilo_total_res_home + quilowatts
  
    if codigo == 2:
      vezes = vezes + 1
      if flag_res == False:
        flag_res = True
      if quilowatts > 800:
        quilo_total = quilo_total + quilowatts
        consumidor.append(0.83*quilowatts)
        quilo_total_res_home = quilo_total_res_home + quilowatts
      else:
        quilo_total = quilo_total + quilowatts
        consumidor.append(0.72*quilowatts)
        quilo_total_res_home = quilo_total_res_home + quilowatts

    if codigo == 3 :
   
      if quilowatts >3000:
        quilo_total = quilo_total + quilowatts
        consumidor.append(0.80*quilowatts)          
        
      else:
        quilo_total = quilo_total + quilowatts
        consumidor.append(0.75*quilowatts)
    

for x in consumidor:
  print("%.2f"%x)
if flag_res == True and flag_home == True:
  print("{:.1f} {:.0f}\n".format(quilo_total, quilo_total_res_home/vezes))
else:
  print("{:.1f} 0 \n".format(quilo_total))