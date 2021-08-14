import dropbox
import cv2
import random
import time

starttime = time.time()

def takesnapshot():
    number = random.randint(0, 100)
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(True):
        ret,frame = videocaptureobject.read()
        imageName = 'img'+str(number)+'.png'
        cv2.imwrite(imageName,frame)
        starttime = time.time
        result = False
    return imageName
    print('snapshot taken')
    videocaptureobject.release()
    cv2.destroyAllWindows()

def uploadfile(imageName):
    accesstoken = 'sl.A2gJFtZzmtTp9YVZlek_D2KzL64T8j2T4tSkx0O96CAUyiJ9-0PWeB3lEp0lvijDw9cXUC88QeAaqXX-qvtZPwB39RuJRwt1TSVY5tG4V_MZXbe1WInj2VsHnoLobEkQrZ2AyZdA4uCK'
    file = imageName
    filefrom = file
    fileto = '/newfolder/'+imageName
    dbx = dropbox.Dropbox(accesstoken)
    with open(filefrom,'rb')as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print('file uploaded')

def main():
    while(True):
        if((time.time()-starttime)>=30):
            name = takesnapshot()
            uploadfile(name)

main()
