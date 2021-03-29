from django.urls import path, include
from .views import(BlogTagView, BlogCommentView, BlogView)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Blogs', BlogView)
router.register('Blog-Comments', BlogCommentView)
router.register('Blog-Tags', BlogTagView)


urlpatterns = [
    path('',include(router.urls))
]