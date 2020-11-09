from django.shortcuts import render, redirect
from .models import Post
#models.py에 선언한 스키마 Comment를 import 함
from .models import Post, Comment

#게시글 작성 창
def new(request):
    #html파일을 리턴해주는 render함수
    return render(request, 'new.html') #연결될 html로 연결.

#게시글 작성 완료 창
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # Post 클래스가 입력 내용을 불러와서 title, content에 담아 post에 저장.
    post = Post(title=title, content=content)
    post.save() #db에 저장
    #★post방식은 html을 반환하지 않기 때문에 render말고 redirect를 사용함.
    #board(새끼폴더의 url폴더에서 연결되는 app-url폴더의 별명)
    #{post.pk}: 글 번호. post의 primary key
    return redirect('board:detail', post.pk) #url 요청

#메인 페이지
def main(request):
    return render(request, 'main.html')

#게시글 목록
def index(request):
    #db(Post)에 저장된 모든 값(objects.all)을 불러옴. posts에 저장.
    posts = Post.objects.all()
    #{키:값} 모든 post값을 posts의 키 이름으로 불러온다.
    #db에서 불러온 내용을 posts(바로 위)에 저장하고,
    # 이 내용을 index.html의 posts(다름 주의)에 저장한다.
    return render(request, 'index.html', {'posts':posts}) #render가 index.html을 뿌려준다.

#게시글 보기
def detail(request, post_id) : #(url에서 요청하는 post_id가 detail의 매개변수로 들어오면서
    post = Post.objects.get(pk=post_id) #그 post_id에 해당하는 내용(객체형태)이 post에 저장됨.
    return render(request, 'detail.html', {'post':post}) #post에 저장된 해당 글 내용을 html에서 함께 보여준다.

#게시글 삭제
# 삭제 기능
# 1. detail.html 에서 삭제 버튼을 누르면 /board/{{post.pk}}/delete 로 url 요청
# 2. 요청된 url과 매핑된 delete 함수 실행
# 3. 함수 내용대로 전달받은 프라이머리키의 글을 삭제하고 /board/index로 리다이렉트
# 4. 요청된 url과 매핑된 index 함수 실행하여 게시글 목록(index)을 보여줌
def delete(request, post_id):
    post = Post.objects.get(pk=post_id)     #pk로 글 번호를 받음.
    post.delete()
    return redirect('board:index')
    #작업 후 연결될 url(index목록)을 요청한다.
    #app-url에서 index로 가서 views.index로 가서 render가 결과창html을 뿌려준다.
    #redirect는 요청한다. render가 뿌려준다.

#게시글 삭제
def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'edit.html', {'post':post})

#게시글 수정
def update(request, post_id):
    post = Post.objects.get(pk=post_id)     #글번호에 해당하는 정보를  post에 담는다.
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.save()
    return redirect('board:detail', post.pk)
    #app-url에서 board:detail로 연결, views.detail로 연결되어
    # 글번호에 해당하는 내용이 수정, 반영되어 render가 뿌려줌.

#댓글 작성창 생성
def comments_create(request, post_id):
    #post_id로 댓글을 달 게시물에 대한 정보 가져오기
    post = Post.objects.get(pk=post_id)
    #form 태그에서 넘어온 댓글 내용 가져오기
    content = request.POST.get('content')

    #댓글 생성 및 저장
    comment = Comment(post=post, content=content)
    comment.save()

    #댓글 생성후, 디테일 페이지로 redirect시킴
    return redirect('board:detail', post.pk)

#댓글 삭제 기능 구현
def comments_delete(request, post_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()

    return redirect('board:detail', post_id)