import qrcode #è necessario installare questa libreria. pip install qrcode
import os

data = 'link del qrcode'

qr = qrcode.QRCode(version=5, box_size=10, border=5) #misure geometriche del qr

qr.add_data(data) #aggiunta del link

qr.make(fit=True) #creazione del qr

img = qr.make_image(fill_color= 'red', back_color= 'black') #inserisce il qr dentro uno sfondo. puoi scegliere i colori

save_path = os.path.expanduser('~/Documenti/programmi/python/__pycache__/myqrcode.png') #scelta del path (cambialo a piacimento)
img.save(save_path) #salvataggio


