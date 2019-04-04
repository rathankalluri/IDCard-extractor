import os
import cv2
import textract

def process_img(path):
	img = cv2.imread(path)
	dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,30)

	filename = "{}.png".format("temp")
	cv2.imwrite(filename, dst)

	text = textract.process(filename)
	os.remove(filename)
	return text


def extract(path):
	#check if file is image 
	if path.lower().endswith(('.png', '.jpg', '.jpeg')):
		text = process_img(path)
		return ({'type':'Image','text':str(text)})
	elif path.lower().endswith(('.odt', '.doc', '.docx', '.pdf')):
		text = textract.process(path)
		return ({'type':'Document','text':str(text)})
	elif path.lower().endswith(('.ogg')):
		text = textract.process(path)		
		return ({'type':'Audio','text':str(text)})
	else:
		return ("Currently we support only: PNG,JPG,JPEG,ODT,DOC,DOCX,PDF,OGG formats")