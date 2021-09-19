import qrcode
from qrcode import constants
from PIL import Image


class QR:
    def __init__(self, link, background, fill_color):
        self.link = link
        self.background = background
        self.fill_color = fill_color

    def define_qr(self):
        code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=30,
            border=2,
        )
        code.make(fit=True)
        code.add_data(self.link)
        image = code.make_image(fill_color=self.fill_color, back_color=self.background)
        image.save("qr.png")


while True:

    try:
        select = int(input("1.Create QR,\n2.Exit\nSelect: "))
        if select == 1:

            link = str(input("Enter a link or any text you want: "))
            background = str(input("Background color: "))
            fill_color = str(input("Fill color: "))
            qr = QR(link, background, fill_color)
            qr.define_qr()
            print("Your QR has been created, check your current folder.")
        elif select == 2:
            print("Closing the program")
            print("...")
            break
        elif select != 1 or select != 2:
            print("Enter the number 1 or 2 to proceed.")

    except:
        print("Enter the number 1 or 2 to proceed.")
