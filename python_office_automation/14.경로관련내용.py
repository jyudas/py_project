"""

폴더 내용 가져오기
os.listdir(경로) 를 활용하면 폴더안의 내용을 문자열로 된 리스트로 가져올 수 있습니다.
import os

# data 디렉토리 안의 내용을 문자열로 이루어된 리스트로 모두 가져옵니다.
contents = os.listdir("data")  

print(contents) # <class: list> [ 모든 파일 또는 디렉토리 ]
절대 경로 알아내기
os 모듈의 abspath() 함수를 사용하면 해당 파일 또는 폴더에 대한 절대 경로를 가져올 수 있습니다.
import os

print(os.path.abspath("filename.txt")
경로가 존재하는 경로인지 확인하기
os.path.exists()를 쓰면 해당 경로가 실제로 존재하는 경로인지 확인할 수 있습니다.
import os

print(os.path.exists("data/업무 자동화.png")) # True
print(os.path.exists("data/데이터 사이언스.png")) # False

경로 쉽게 사용하기
os.path.sep
os.path.sep 을 사용하면 내가 사용하는 운영체제가 무엇인지 신경 쓰지 않고 경로 구분 기호를 쓸 수 있습니다. os.path.sep 은 현재 운영체제에서 사용하는 경로 구분 기호로 자동으로 변환됩니다.
import os

print(os.path.sep) # window라면 '\'가 출력되고, macOS라면 '/'가 출력됩니다.
os.path.join
경로를 다루다 보면 폴더가 여러개 중첩되어 있는구조를 자주 만나게 됩니다. 이때 유용하게 쓸 수 있는 것이 os.path.join() 함수인데요. os.path.join은 여러 경로를 합쳐주는 기능을 합니다. 예를 들어, 'Users' 폴더 아래 'Codeit' 폴더 안에 있는'cat.jpg'를 나타내는 경로를 표현하고 싶다면 이렇게 적어주면 됩니다. 경로 구분 기호도 운영체제에 맞게 알아서 인식하기 때문에 경로를 다룰때 조금 더 편하게 사용할 수 있습니다.
import os

file_path = os.path.join('Users', 'Codeit', 'cat.jpg')

print(file_path)
Users\Codeit\cat.jpg # windows
Users/Codeit/cat.jpg # macOS
상대경로의 활용
.은 지금 파이썬 코드가 실행되는 파일과 같은 현재 디렉토리를 의미하고, ..은 현재 워킹 디렉토리의 한 단계 위, 부모 디렉토리를 의미합니다. 예를들어 현재 파이썬 파일이 있는 현재 워킹 디렉토리가 /Users/codeit/automation 라고 하면, . 은 /Users/codeit/automation 을 의미하고,  .. 은 현재 워킹 디렉토리의 한 단계 전인 /Users/codeit 까지를 의미하게 됩니다.
모든 폴더 한 번에 살펴보기
폴더 내에 모든 내용을 살펴보기 위해서는 for문과 os.walk()를 사용하면 됩니다. os.walk()의 파라미터로 넘긴 경로 아래에 있는 모든 폴더를 반복하며 반복중인 현재 하위 디렉토리는 path에, 그 경로에 있는 모든 디렉토리는 dirs에, 파일들은 files에 담깁니다.
import os

for path, dirs, files in os.walk("/"):
    print("Path: {}".format(path))
    print("Folders: {}".format(dirs))
    print("Files: {}".format(files))
    print("-----")
파일 이동하기
파일을 이동시키고 싶다면 os.rename 함수를 이용하는 방법과 shutil.move를 이용하는 방법이 있습니다.
os.rename 이용하기
os.rename은 파일의 이름 변경 뿐만 아니라 파일 이동도 할 수 있습니다. os.rename의 두 파라미터에는 파일의 이름이 들어가는 게 아니라, 파일의 경로가 들어갑니다. 아래처럼 이동할 경로를 함께 넣어주면 해당 위치로 이동하게 됩니다.
import os

os.rename("codeit_news.txt", "news/2021_codeit.txt") # macOS
os.rename("codeit_news.txt", "news\\2021_codeit.txt") # windows
이렇게 하면 news 디렉토리 안쪽으로 codeit_news.txt 파일의 이름이 2021_codeit.txt로 바뀌어서 이동하게 됩니다.
shutil.move 이용하기
shutil.move를 이용해도 파일을 이동할 수 있습니다. 사용하는 방법은 os.rename과 똑같습니다.
import shutil

shutil.move("codeit_news.txt", "news/2021_codeit.txt") # macOS
shutil.move("codeit_news.txt", "news\\2021_codeit.txt") # windows
주의 사항
os.rename, shutil.move 모두 파일을 이동할 때 이름이 똑같은 파일이 이미 이동하려는 위치에 존재하면, 이동 시키는 파일로 원래의 파일을 덮어쓰기합니다. 예를 들어, Hello_eng.txt 에는 "Hello"라는 문자열이 있고, Hello_kor.txt 에는 "안녕하세요"가 들어있다고하면
import os
os.rename("Hello_eng.txt", "Hello_kor.txt")
import shutil
shutil.move("Hello_eng.txt", "Hello_kor.txt")
이 두 코드 모두, 실행하면 기존의 Hello_kor 내용인 "안녕하세요"가 삭제됩니다. 이럴 때는, os.path.exists를 사용해서 파일이 실제로 존재하는지 여부를 체크하면 됩니다.
import os
if not os.path.exists("Hello_kor.txt"):
    os.rename("Hello_eng.txt", "Hello_kor.txt")
"""