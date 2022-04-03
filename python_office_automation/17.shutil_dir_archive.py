import shutil
import os

# 생성 삭제
# os.mkdir("aaaa")
# shutil.copytree("aaaa","bbbb")
# shutil.rmtree("bbbb")

# 압축
# shutil.make_archive("zzz","zip","aaaa")
# shutil.unpack_archive("zzz.zip","unpack")

"""
shutil 모듈
폴더 복사
폴더를 다른 위치로 복사하고 싶다면 shutil 모듈의 copytree() 함수를 사용하면 됩니다. 함수의 이름에서도 알 수 있듯, 복사하는 폴더 안에 다른 폴더가 있는 일종의 '폴더 트리' 형식이어도 모두 한 번에 복사합니다.  copytree()의 첫번째 파라미터로 복사 대상 폴더를 넣어주고, 두번째 파라미터로 목적 폴더의 경로를 넣어주면 됩니다. 예를 들어, "data" 폴더 안의 내용을 파일과 폴더 상관없이 모두 "copy_of_data" 폴더로 복사하려면 아래와 같이 하면 됩니다.
import shutil
shutil.copytree("data", "copy_of_data")
내용이 있는 폴더 삭제
내용이 있는 폴더를 삭제하기 위해서는 shutil.rmtree() 함수를 사용하면 됩니다. rmtree() 함수의 파라미터로 삭제할 폴더의 경로를 적어주면 됩니다.
import shutil

shutil.rmtree("폴더 경로")
예를 들어, 내용 유무와 상관없이 test_directory 폴더를 삭제하려면 아래와 같이 하면 됩니다.
import shutil

shutil.rmtree("test_directory")
폴더 압축
폴더 전체를 압축하는 방법을 배워보겠습니다. shutil 모듈의 make_archive() 함수를 사용하면 됩니다. make_archive() 함수의 첫 번째 파라미터로 만들어질 압축 파일의 이름을, 두 번째 파라미터로 압축 방식을, 세 번째 파라미터로는 압축할 폴더의 경로를 넣으면 됩니다.
import shutil

shutil.make_archive("생성되는 압축 파일 이름", "zip", "압축 대상 폴더")
그럼 data 폴더를 압축해볼까요? 파일 이름은 archive, 압축 방식은 zip, 대상 폴더는 "data" 입니다.
import shutil

shutil.make_archive("archive", "zip", "data")
압축 해제
압축 해제하는 방법도 배워볼께요. 압축 해제는 shutil 모듈의 unpack_archive() 함수를 사용하면 됩니다. 첫 번째 파라미터는 압축을 풀 압축 파일 이름을, 두 번째 파라미터는 압축을 해제할 폴더를 적어주면 됩니다. 이전에 코드에서 압축했던 archive.zip 파일을 unpack 폴더에 푼다면 아래처럼 코드를 작성하면 됩니다.
import shutil

shutil.unpack_archive("archive.zip", "unpack")
"""