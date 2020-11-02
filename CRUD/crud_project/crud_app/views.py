from django.shortcuts import render, redirect
from .models import Post

def new(request):
    #html파일을 리턴해주는 render함수
    return render(request, 'new.html')

#게시글 작성 완료 창
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # Post 클래스가 입력 내용을 불러와서 title, content에 담아 post에 저장.
    post = Post(title=title, content=content)
    post.save() #db에 저장
    #post방식은 html을 반환하지 않기 때문에 render말고 redirect를 사용함.
    #board(새끼폴더의 url폴더에서 연결되는 app-url폴더의 별명)
    #{post.pk}: 글 번호. post의 primary key
    return redirect(f'/board/{post.pk}')

#메인 페이지
def main(request):
    return render(request, 'main.html')

#게시글 목록
def index(request):
    #db에 저장된 모든 값(objects.all)을 불러옴. posts
    posts = Post.objects.all()
    #{키:값} 모든 post값을 posts의 키 이름으로 불러온다.
    return render(request, 'index.html', {'posts':posts})

#게시글 보기
def detail(request, post_id) :
    post = Post.objects.get(pk=post_id)
    return render(request, 'detail.html', {'post':post})

#게시글 삭제
# 삭제 기능
# 1. detail.html 에서 삭제 버튼을 누르면 /board/{{post.pk}}/delete 로 url 요청
# 2. 요청된 url과 매핑된 delete 함수 실행
# 3. 함수 내용대로 전달받은 프라이머리키의 글을 삭제하고 /board/index로 리다이렉트
# 4. 요청된 url과 매핑된 index 함수 실행하여 게시글 목록(index)을 보여줌
def delete(request, post_id):
    post = Post.objects.get(pk=post_id)     #pk로 글 번호를 받음.
    post.delete()
    return redirect('/board/index')         #작업 후 연결될 창.index목록

#게시글 삭제
def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'edit.html', {'post':post})

#게시글 수정
def update(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.save()
    return redirect(f'/board/{post_id}/')      #수정한 내용 반영