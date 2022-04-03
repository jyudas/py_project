import os
import shutil

files = os.listdir("downloads")

for file in files:
    filename, extension = os.path.splitext(file)

    if extension == ".pptx" or extension == ".docx" or extension == ".hwp":
        file_path = r"downloads/{}".format(file)
        usb_path = r"usb/docs/{}".format(file)
        shutil.copy(file_path, usb_path)
        print('{} -> docs로 복사'.format(file))
    elif extension == ".png" or extension == ".jpg" or extension == ".svg":
        if "screenshot" in filename:
            file_path = r"downloads/{}".format(file)
            usb_path = r"usb/screenshots/{}".format(file)
            shutil.copy(file_path, usb_path)
            print('{} -> screenshots로 복사'.format(file))
        else:
            file_path = r"downloads/{}".format(file)
            usb_path = r"usb/images/{}".format(file)
            shutil.copy(file_path, usb_path)
            print('{} -> images로 복사'.format(file))
    else:
        file_path = r"downloads/{}".format(file)
        usb_path = r"usb/etc/{}".format(file)
        shutil.copy(file_path, usb_path)
        print('{} -> etc로 복사'.format(file))

# 출력 포맷
print('{} -> <이동할 디렉토리>로 복사'.format(file))
