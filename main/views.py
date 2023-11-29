from django.shortcuts import render
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