from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('article-list/', views.article_list, name='article-list'),

    # 文章详情
    path('article-detail/<int:id>/', views.article_detail, name='article-detail'),

    # 写文章 修改文章
    path('article-create-update/<int:id>/', views.article_create_update, name='article-create-update'),

    # 删除文章
    path('article-delete/<int:id>/', views.article_delete, name='article-delete'),

]
