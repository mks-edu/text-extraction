import unittest
import easyocr

class MyTestCase(unittest.TestCase):
    def test_readtext(self):
        '''
        See https://www.kaggle.com/code/badhansen/text-extraction-from-images-easyocr-pytesseract
        :return:
        '''
        reader = easyocr.Reader(['vi', 'en'])

        img_path = r'G:\Projects\AIC-2024\Mr.Gia\AllKeyFrameTest\V1_037.jpg'
        img_text = reader.readtext(img_path)
        final_text = ""

        for _, text, __ in img_text:  # _ = bounding box, text = text and __ = confident level
            print(text)

        # self.assertEqual(True, False)  # add assertion here

if __name__ == '__main__':
    unittest.main()
