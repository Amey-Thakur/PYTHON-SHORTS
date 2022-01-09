#pip install qrcode

import qrcode

img = qrcode.make("https://github.com/Amey-Thakur")

img.save("sample.jpg")

