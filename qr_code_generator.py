import qrcode
from PIL import Image
user_input = input("Enter the url or text to be encoded: ")
qr = qrcode.QRCode(
    version = 5, 
    error_correction= qrcode.constants.ERROR_CORRECT_H,
    box_size = 12,
    border = 6
)
qr.add_data(user_input)
qr.make(fit=True)
img = qr.make_image(fill_color="pink", back_color="white")
img.save("Myqrcode.png")
print("QR Code Generated Successfully!")
