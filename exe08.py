import qrcode

qr = qrcode.QRCode(version=1, box_size=10, border =5)

data = 'hrrps://www.google.com'
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color='white')

#salvar imagem
img.save('qr_code.png')
