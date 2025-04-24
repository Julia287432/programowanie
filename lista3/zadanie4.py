import qrcode
import cv2

def generate_qr(data, filename):
    img = qrcode.make(data)
    img.save(filename)

def read_qr(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)
    return data


generate_qr('https://example.com', 'qr.png')
print(read_qr('qr.png'))