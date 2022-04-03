import os

# os.makedirs(r"mkdd/aaa")
# os.rmdir("mkdd")
# os.renames("mkdd","aabb")

"""
폴더 생성하기
os.makedirs(경로)함수는 경로에 해당하는 디렉토리를 생성하는 함수입니다. 그 과정에서 만약 해당 경로에 지금 존재하지 않는 디렉토리가 있다면 그 디렉토리도 함께 만들어줍니다.
예를 들어, 현재 'codeit' 디렉토리에 있고 이 'codeit' 디렉토리는 텅 비어있다고 하겠습니다. 그 상태에서 아래 코드를 실행하면 현재 위치 아래에 'years' 디렉토리가 생기고 그 안에 '2021' 디렉토리도 생기게 됩니다.
import os

os.makedirs('years/2021') # macOS
os.makedirs('years\\2021') # windows
참고로 os.makedirs(경로) 말고도 os.mkdir(경로) 함수도 있습니다. 가장 큰 차이점은 os.mkdir(경로) 는 경로 안에 지금 존재하지 않는 디렉토리가 있다면 OSError를 발생시킨다는 점입니다. 아래 코드에서 years/2021/08/15 경로 안에 08 디렉토리는 현재 존재하지 않는 디렉토리이므로 에러가 발생합니다.
os.mkdir('years/2021/08/15') # macOS
os.mkdir('years\\2021\\08\\15') # windows
아래처럼 경로의 가장 마지막 디렉토리를 제외하고 존재하는 디렉토리라면 에러는 발생하지 않습니다.
os.mkdir('years/2021/08') # macOS
os.mkdir('years\\2021\\08') # windows
함수의 이름에서 알 수 있듯이 mkdir은 하나의 디렉토리를 만들 때, makedirs는 여러 디렉토리를 생성할 때 유용합니다.
그러면 그냥 makedirs만 사용하면 안되냐구요? 만약 우리가 생성하려는 경로가 잘못된 경로라면 어떻게 될까요? os.makedirs(경로)는 해당 경로가 잘못된 경로라고 하더라도 경로에 해당하는 모든 디렉토리를 생성합니다. 반면에 os.mkdir(경로)는 해당 경로가 존재하지 않는다면 에러를 내고 디렉토리를 생성하지 않겠죠. 그러니까 둘 중에 하나만 사용하면 된다기 보다 구현하려는 로직에 맞게 함수를 사용하는 것이 좋습니다.
빈 디렉토리 삭제하기
빈 디렉토리를 삭제하는 방법을 배워보겠습니다. os모듈의 rmdir() 함수를 사용하면 됩니다. 단, 이때 디렉터리는 비어있어야 합니다. 비어 있지 않다면 삭제가 되지 않고 오류가 납니다.
import os

os.rmdir("test_directory") # test_directory가 비어있지 않다면 삭제가 되지않습니다.
비어 있지 않은 디렉토리를 삭제하고 싶다면 shutil 모듈의 rmtree 함수를 사용하면 되는데요. 이건 뒤에서 다뤄 보도록 하겠습니다.
폴더 이름 변경하기
폴더 이름을 변경하는 방법은 파일 이름 변경하는 것과 같이 os 모듈의 rename() 함수를 활용하면 됩니다. os.rename의 첫 번째 파라미터로 바꾸고 싶은 폴더의 이름을, 두 번째 파라미터에는 새로 바꿀 이름을 넣어주면 됩니다. 아래는 test_directory를 data로 바꾸는 코드입니다.
import os

os.rename("test_directory", "data")
폴더 이동하기
폴더 이동도 마찬가지로 os 모듈의 rename를 이용하면 됩니다. rename 함수의 각각의 파라미터에는 경로가 들어간다고 설명했었죠? 이점을 이용해서 바꾸고 싶은 경로를 넣어주면 폴더 이동을 할 수 있습니다. 아래는 meeting-log의 day1 폴더를 test_directory로 이동하는 코드입니다.
import os

os.rename("meeting-log/day1", "test_directory")
"""