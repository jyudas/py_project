import os
import zipfile

# filenames = print(os.listdir(".")) #경로셋팅
# print(os.path.isdir("python_web_crawling"))
# print(os.path.isdir(".DS_Store"))
# print(os.path.isfile("python_web_crawling"))

"""
import os
import shutil

path = "데이터 사이언스.png"

if os.path.exists(path): # 데이터 사이언스.png 파일이 없기 때문에
    shutil.copy(path, "데이터 사이언스 심화.png") # 이 코드가 실행되지 않습니다.
"""

# print(os.listdir("python_web_crawling"))
cwd = os.getcwd()
# print(os.getcwd())
# print(os.listdir(os.getcwd()))
print(cwd)
print(os.listdir("..")) #상위폴더
print(os.listdir("../pythonProject"))

"""
import os

# 이곳에 코드를 작성해 주세요.

filenames = os.listdir(".") #경로셋팅
for i in filenames :
    if os.path.isdir(i) :
        print("{} is a folder.".format(i))
    else:
        print("{} is a file.".format(i))

경로 다루기
업무 자동화의 시작과 끝은 결국 파일과 폴더를 다루는 일이고, 그러한 파일과 폴더는 '경로'를 이용해서 접근하고 처리하게 됩니다. 이번 노트에서는 이 경로를 조금 더 쉽게 다룰 수 있는 몇 가지 방법을 알아보겠습니다.
경로 구분 기호
우리는 경로를 표현할 때 경로 구분 기호(Path Separator)를 사용해서 각각의 디렉토리를 구분합니다.
# codeit 디렉토리 안에 있는 codeit_report.txt 파일

path = 'codeit/codeit_report.txt' # macOS/Linux/Unix
path = 'codeit\\codeit_report.txt' # windows
보면 windows는 경로 구분 기호가 \\이고, 그 외 운영체제에서는 / 인 것을 알 수 있습니다. 그 중에서도 windows는 \ 가 아니라 \\ 로 되어있는데요. 사실 windows의 경로 구분 기호는 \ 입니다. 하지만 \ 다음 특정 문자가 오게 되면 그것을 \n 같은 이스케이프 문자로 처리할 수 있기 때문에 \\ 로 적어주는 것이 안전한 코딩 방법입니다. 실제로 경로를 \ 적은 것과 \\ 로 적은 것을 print 해보면 모두 \ 로 경로가 구분 되어 있는 것을 볼 수 있습니다.
path_1 = 'codeit\codeit_report.pdf'  # windows
path_2 = 'codeit\\codeit_report.pdf'  # windows

print(path_1)  # codeit\codeit_report.pdf
print(path_2)  # codeit\codeit_report.pdf
여기서 만약 파일 이름이 'codeit_report.pdf'가 가니라 'note_codeit.txt' 라면 어떻게 될까요?
path_1 = 'codeit\note_codeit.pdf'  # windows
path_2 = 'codeit\\note_codeit.pdf'  # windows

print(path_1)
print(path_2)
# 출력 결과

# print(path_1)
codeit
ote_codeit.pdf
# print(path_2)
codeit\note_codeit.pdf
보는 것처럼 \n 이 줄바꿈 문자로 인식된 것을 알 수 있습니다. 우리가 원하는 결과가 아닌거죠. 그런데 강의에서는 \ 을 사용해도 이상 없이 잘 출력됐죠? 사실 그건 우리가 경로를 지금처럼 print() 함수를 이용해서 출력하기 보다 꼭 경로를 파라미터로 받는 함수나 메서드를 사용했기 때문에 모듈이 알아서 문자열을 경로 형식으로 바꿔서 처리해 준 겁니다. 하지만 코딩을 할 때는 자신이 예측 가능한 코드를 작성하는 것이 좋은 코딩 습관이기 때문에, 앞으로 windows 환경에서의 경로 구분 기호는  \\ 을 사용하는 것이 좋습니다.
os.path.sep
경로 구분 기호가 무엇인지 또 운영체제마다 어떻게 다른지 이해했는데 사실 매번 이렇게 경로 구분 기호를 구분해서 입력하는 것은 쉬운 일이 아닙니다. 어느 순간 틀릴 수도 있고 만약 windows에서 코딩한 프로그램을 macOS에서 사용하고 싶다면 코드 상의 모든 경로 구분 기호를 다 바꿔줘야겠죠. 이럴때 os.path.sep 을 사용하면 내가 사용하는 운영체제가 무엇인지 신경 쓰지 않고 경로 구분 기호를 쓸 수 있습니다. os.path.sep 은 현재 운영체제에서 사용하는 경로 구분 기호로 자동으로 변환됩니다.
import os

print(os.path.sep) # window라면 '\'가 출력되고, macOS라면 '/'가 출력됩니다.
os.path.join
경로를 다루다 보면 폴더가 여러개 중첩되어 있는구조를 자주 만나게 됩니다. 이때 유용하게 쓸 수 있는 것이 os.path.join() 함수인데요. os.path.join은 여러 경로를 합쳐주는 기능을 합니다.
예를 들어, 'Users' 폴더 아래 'Codeit' 폴더 안에 있는'cat.jpg'를 나타내는 경로를 표현하고 싶다면 이렇게 적어주면 됩니다. 경로 구분 기호도 운영체제에 맞게 알아서 인식하기 때문에 경로를 다룰때 조금 더 편하게 사용할 수 있습니다.
import os

file_path = os.path.join('Users', 'Codeit', 'cat.jpg')

print(file_path)
Users\Codeit\cat.jpg # windows
Users/Codeit/cat.jpg # macOS
"""