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