from django.urls import path

from . import views

# 이미지 URL 설정
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("board/", views.board, name="board"),
    path("board/<int:pk>/", views.posting, name="posting"),
]   

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)