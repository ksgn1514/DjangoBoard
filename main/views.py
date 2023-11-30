from django.utils import timezone
from django.utils.timezone import localtime
from django.shortcuts import redirect, render
# View에 Model(Post 게시글) 가져오기
from .models import Post

# Create your views here.
# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request, 'main/index.html')

# board.html 페이지를 부르는 board 함수
def board(request):
    # DB에 있는 모든 Post를 가져와 postlist에 저장
    postlist = Post.objects.all()
    # postlist를 'postlist'라는 이름으로 board.html에 전달
    return render(request, 'main/board.html', {'postlist': postlist})

def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/posting.html', {'post':post})

def new_post(request):
     # POST 요청일 경우, 새로운 Post 게시글을 작성하고 저장
    if request.method == 'POST':
        if bool(request.FILES.get('mainphoto',False))==True:
            new_article = Post.objects.create(
                title = request.POST['title'],
                content = request.POST['content'],
                mainphoto = request.FILES['mainphoto'],
                pub_date = localtime(timezone.now())
            )
        else:
            new_article = Post.objects.create(
                title = request.POST['title'],
                content = request.POST['content'],
                pub_date = localtime(timezone.now())
            )
        # 작성한 글의 상세 페이지로 이동
        return redirect('posting', new_article.pk)
    return render(request, 'main/new_post.html')

def delete_post(request, pk):
    # 삭제할 Post의 pk를 이용해 해당 Post 검색
    post = Post.objects.get(pk=pk)
    # POST 요청일 경우, 해당 Post 삭제
    if request.method == 'POST':
        post.delete()
        # 삭제 완료 후, 메인 페이지로 이동
        return redirect('board')
    return render(request, 'main/delete_post.html', {'post':post})    

