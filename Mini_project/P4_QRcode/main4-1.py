import qrcode

qr_data = 'news.naver.com'
qr_img = qrcode.make(qr_data)

save_path = 'P4_QRcode\\' + qr_data + '.png'
qr_img.save(save_path)