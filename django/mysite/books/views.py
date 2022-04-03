from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .models import select_book

def index(request):
    all_book_lists = select_book.objects.order_by('id')
    context = {'all_book_lists': all_book_lists}
    return render(request, 'books/index.html', context)

def add(request):
    booklist = select_book()
    booklist.category = request.POST['category']
    booklist.title = request.POST['title']
    booklist.writer = request.POST['writer']

    booklist.save()

    # insert 후에는 꼭 redirect 처리!
    return HttpResponseRedirect('/books/')


def delBook(request):

    try:
        booklist = select_book.objects.get(id=request.POST['id'])
    except (KeyError, select_book.DoesNotExist):
        print("case0:::::")
        # 에러 메세지와 함께 폼을 다시 디스플레이합니다.
        return render(request, '/books/index.html', {
            'error_message': "id에해당하는 도서가 없어요.",
        })
    else:
        if request.POST['pw'] == "skandmltna0":
                print("case1:::::")
                booklist.delete()

                # insert 후에는 꼭 redirect 처리!
                return HttpResponseRedirect('/books/')

        else:
            print("case2:::::")
            return render(request, 'books/index.html', {
                'error_message': "비밀번호가 틀렸습니다.",
            })