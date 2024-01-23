# We had to install "pillow" which is used by qrcode in the background
import qrcode

image = qrcode.make('https://127.0.0.1:8000')
image.save('qr.png')
