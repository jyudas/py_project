import os

# target_dir = "data"
# files = os.listdir(target_dir)
# total_size = 0
#
# for file in files:
#     file_path = os.path.join(target_dir, file)
#     file_size = os.path.getsize(file_path)
#
#     print("{}의 용량은 {}byte입니다.".format(file, file_size))
#     total_size += file_size
#
# print("총 용량은 {}byte입니다.".format(total_size))
# 모든폴더 검색
# for path, dirs, files in os.walk("."):
#     print("path:{}".format(path))
#     print("folders:{}".format(dirs))
#     print("files:{}".format(files))
#     print("--------")

# 모든 파일 폴더 갯수 세기
# import os
#
# count = 0
# target_path = "data"
#
# for path, dirs, files in os.walk(target_path):
#     for dir in dirs:
#         count += 1
#         print("{}/폴더/{}".format(count, dir))
#
#     for file in files:
#         count += 1
#         print("{}/파일/{}".format(count, file))
#
# print("총 파일 및 폴더 개수: {}".format(count))

# 경로다루기과제
import os

# 이곳에 코드를 작성해주세요.
target_path = "mycodeit"

for path, dirs, file in os.walk(target_path):
    print("디렉토리: {}".format(path))
    if dirs:
        print("하위 디렉토리: {}".format(",".join(dirs)))
    else:
        print("하위 디렉토리: 없음")

# 파일이동
files = os.listdir("data")

for file in files:
    file_path = os.path.join("data", file)
    new_path = os.path.join("images", file)
    os.rename(file_path, new_path)

# 채점 코드
print(os.path.getsize("images"))

# 아래와 같은 출력 포맷을 사용하면 됩니다.
# print("디렉토리: {}".format(path))
# print("하위 디렉토리: {}".format(dirs))

"""
파일 이동하기
이제 경로에 대해 배웠으니까 경로를 이용해서 파일 이동을 해 볼게요. 우리가 배운 내용을 이용해서 파일을 이동하는 방법에는 두 가지가 있습니다. 하나는 os 모듈을 이용하는거고 다른 하나는 shutil 모듈을 이용하는 건데요. 먼저 os 모듈을 이용하는 방법 부터 알아볼게요.
os.rename 이용하기
앞에서 우리가 파일의 이름을 바꿀때 os.rename을 사용했었죠? 그런데 이 rename은 파일의 이름 변경 뿐만 아니라 파일 이동도 할 수 있습니다.
앞에서 우리는 이런식으로 rename을 사용했었는데요.
import os

os.rename("codeit_news.txt", "2021_codeit_news.txt")
사실 rename의 두 파라미터에는 파일의 이름이 들어가는 게 아니라, 파일의 경로가 들어갑니다. 그래서 위 코드처럼 이름만 적어줘도, 상대 경로로 인식이 되어서 지금 있는 디렉토리안에 있는 파일로 동작이 됐던거죠. 그래서 아래처럼 이동할 경로를 함께 넣어주면 해당 위치로 이동하게 됩니다.
import os

os.rename("codeit_news.txt", "news/2021_codeit.txt")
이렇게 하면 news 디렉토리 안쪽으로 codeit_news.txt 파일의 이름이 2021_codeit.txt로 바뀌어서 이동하게 됩니다.
shutil.move 이용하기
그리고 앞에서 배운 shutil 모듈에도 파일을 이동할 수 있는 함수가 있습니다. 바로 shutil.move 인데요. 사용하는 방법은 os.rename과 똑같습니다.
import shutil
shutil.move("codeit_news.txt", "news/2021_codeit.txt")
자, 그러면 os.rename과 shutil.move는 어떤 차이점이 있을까요? 가장 큰 차이점은 os.rename이 실패할 수 있는 작업을 shutil.move는 성공적으로 할 수 있다는 것입니다. 예를 들어 우리가 이동하려는 위치가 현재 내가 있는 C 드라이브가 아닌 D 드라이브, 즉 다른 드라이브에 있을 수도 있고, 아니면 파일 시스템이 다를 수도 있습니다. 여기서 파일 시스템이란 운영 체제가 파일을 다루는 기본 형식을 말하는데, 윈도우라면 NTFS, FAT32등의 형식입니다. 한 번쯤 보신 적이 있으시죠? 만약 파일 시스템에 대해 더 자세히 알고 싶다면 다음 링크를 참조해보세요.
자, 이렇게 이동하려는 곳이 특수한 상황일때 os.rename은 파일 이동을 실패할 수 도 있지만 shutil.move는 실패하지 않습니다. 왜냐하면 shutil.move는 복사하려는 대상이 같은 파일 시스템인지 여부를 확인하고 만약 동일한 파일시스템이라면 파일 이동을, 다른 시스템이라면 먼저 대상 위치로 파일을 복사하고 그다음에 원본 파일을 지우는 방식이 적용되어 있기 때문입니다.
둘 중에 무엇이 더 뛰어난 방식이라고 얘기할 수는 없습니다. 결국 shutil.move도 내부적으로는 os.rename 방식을 사용하고 있거든요. 자신이 작성하는 코드가 어느 수준에서 동작하는지를 이해하고 사용하면 됩니다. 이어지는 레슨들에서는 하나의 드라이브 내에서 이동하는 경우가 대부분이기 때문에 강의에서는 os.rename을 사용할게요.
주의 사항
자 여기서 주의해야 할 점이 하나 있습니다. os.rename, shutil.move 모두 파일을 이동할 때 이름이 똑같은 파일이 이미 이동하려는 위치에 존재하면, 이동 시키는 파일로 원래의 파일을 덮어쓰기 한다는 점입니다.
예를들어, Hello_eng.txt 에는 "Hello"라는 문자열이 있고, Hello_kor.txt 에는 "안녕하세요"가 들어있다고하면
import os
os.rename("Hello_eng.txt", "Hello_kor.txt")
import shutil
shutil.move("Hello_eng.txt", "Hello_kor.txt")
이 두 코드 모두, 실행하면 기존의 Hello_kor 내용인 "안녕하세요"가 삭제됩니다. 이럴 때는, os.path.exists를 사용해서 파일이 실제로 존재하는지 여부를 체크하면 됩니다.
import os
if not os.path.exists("Hello_kor.txt"):
    os.rename("Hello_eng.txt", "Hello_kor.txt")

"""