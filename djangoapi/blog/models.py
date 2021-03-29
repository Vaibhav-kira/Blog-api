from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
'''
Blogtags: - title and created at ......
'''
class BlogTag(models.Model):
    title = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.title
""" 
Blog : - 
    many tags
    title
    content
    Author
    Created at
    Updated at
"""
class Blog(models.Model):
    tags = models.ManyToManyField(BlogTag, related_name="Blog_tags")
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(User, related_name="Blog_author", on_delete=models.CASCADE)
    content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.title} - {self.author.username}"
"""
BlogComment
    Author: - 
    Comment:  -
    Createdat: - 
    Updated at: - 
"""
class BlogComment(models.Model):
    Blog = models.ForeignKey(Blog,related_name="Blog_comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="Blog_comments_author", on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.Blog.title} - {self.author.username}"


