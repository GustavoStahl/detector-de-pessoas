import os
import time

from datetime import datetime
from datetime import date

while(1):

    horario = datetime.now()
    
    if horario.hour == 18 and horario.minute == 56 and horario.second == 30:
        data = datetime.now()
        dia = data.day - 1
        mes = data.month
        ano = data.year

        os.system('mkdir Banco/"%s-%s-%s"' % (dia, mes, ano))
        os.system('mkdir Banco/"%s-%s-%s"/"0-6"' % (dia, mes, ano))
        os.system('mkdir Banco/"%s-%s-%s"/"6-12"' % (dia, mes, ano))
        os.system('mkdir Banco/"%s-%s-%s"/"12-18"' % (dia, mes, ano))
        os.system('mkdir Banco/"%s-%s-%s"/"18-24"' % (dia, mes, ano))

        os.system('find ./YOLO/"0-6"/ -type f -name *.jpg -exec mv {} Banco/"%s-%s-%s"/"0-6" \;' % (dia, mes, ano))
        os.system('find ./YOLO/"6-12"/ -type f -name *.jpg -exec mv {} Banco/"%s-%s-%s"/"6-12" \;' % (dia, mes, ano))
        os.system('find ./YOLO/"12-18"/ -type f -name *.jpg -exec mv {} Banco/"%s-%s-%s"/"12-18" \;' % (dia, mes, ano))
        os.system('find ./YOLO/"18-24"/ -type f -name *.jpg -exec mv {} Banco/"%s-%s-%s"/"18-24" \;' % (dia, mes, ano))
        time.sleep(5)

        



