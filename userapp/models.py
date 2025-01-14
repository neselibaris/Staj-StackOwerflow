from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from profileApp.models import CustomUser, Badge
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Count


class Tags(models.Model):
    tagler = models.CharField(("Tagler"), max_length=10)
    tagDescription = models.TextField(("Açıklma"), max_length=100,null=True)
    view = models.IntegerField(("Görüntülenme Sayısı"), default=0)


    def __str__(self):
        return self.tagler

class Post(models.Model):
    title = models.CharField(("Başlık"), max_length=50, null=True)
    description = models.TextField(("Açıklama"), max_length=500, null=True)
    createdAt = models.DateTimeField(("Oluşturma tarihi"), auto_now=True)
    viewed = models.IntegerField(("Görüntülenme Sayısı"), default=0)
    like = models.IntegerField(("Beğeni Sayısı"), default=0)
    comment = models.IntegerField(("Yorum Sayısı"), default=0)
    user = models.ForeignKey(CustomUser, verbose_name=("Yazarı"), on_delete=models.CASCADE)
    tagleri = models.ManyToManyField(Tags,("Tagleri"))
    kodalanı = RichTextField("Kod Bloğu", max_length=1500, null=True)
    answerCount = models.IntegerField(("Görüntülenme Sayısı"), default=0)



    def __str__(self):
        return self.title
class Answer(models.Model):
    post = models.ForeignKey(Post, verbose_name=("Post"), on_delete=models.CASCADE)
    description = models.TextField(("Açıklama"), max_length=500, null=True)
    createdAt = models.DateTimeField(("Oluşturma tarihi"), auto_now=True)
    like = models.IntegerField(("Beğeni Sayısı"), default=0)
    comment = models.IntegerField(("Yorum Sayısı"), default=0)
    user = models.ForeignKey(CustomUser, verbose_name=("Yazarı"), on_delete=models.CASCADE)
    kodalanı = RichTextField("Kod Bloğu", max_length=1500, null=True)
    def __str__(self):
        return self.description    


class Comments(models.Model):
    post = models.ForeignKey(Post, verbose_name=("Post"), on_delete=models.CASCADE)
    description = models.TextField(("Açıklama"), max_length=500, null=True)
    createdAt = models.DateTimeField(("Oluşturma tarihi"), auto_now=True)
    user = models.ForeignKey(CustomUser, verbose_name=("Yazarı"), on_delete=models.CASCADE)
    def __str__(self):
        return self.description
class Comments2(models.Model):
    answer = models.ForeignKey(Answer, verbose_name=("Post"), on_delete=models.CASCADE)
    
    description = models.TextField(("Açıklama"), max_length=500, null=True)
    createdAt = models.DateTimeField(("Oluşturma tarihi"), auto_now=True)
    user = models.ForeignKey(CustomUser, verbose_name=("Yazarı"), on_delete=models.CASCADE)

    def __str__(self):
        return self.description    
    
@receiver(post_save, sender=Post)
def check_questions_and_award_badge(sender, instance, created, **kwargs):
        like_count = instance.like
        user = instance.user
        badgecount = instance.user.badgecount

        if like_count == 1:
            badge_id = 1
            badge = Badge.objects.get(pk=badge_id)
            user.badge.add(badge)
            badgecount += 1
            instance.user.badgecount = badgecount
            instance.user.save()
              # Bronze Badge
        elif like_count == 2:
            badge_id = 2
            badge = Badge.objects.get(pk=badge_id)
            user.badge.add(badge) 
            badgecount += 1
            instance.user.badgecount = badgecount
            instance.user.save() # Silver Badge
        elif like_count == 3:
            badge_id = 3
            badge = Badge.objects.get(pk=badge_id)
            user.badge.add(badge) 
            badgecount += 1
            instance.user.badgecount = badgecount
            instance.user.save() # Gold Badge


@receiver(post_save, sender=Answer)
def check_answers_and_award_badge(sender, instance, created, **kwargs):
        like_count = instance.like
        user = instance.user
        badgecount = instance.user.badgecount

        if like_count == 1:
            badge_id = 4
            badge = Badge.objects.get(pk=badge_id)
            user.badge.add(badge)
            badgecount += 1
            instance.user.badgecount = badgecount
            instance.user.save()  # Bronze Badge
        elif like_count == 2:
            badge_id = 5
            badge = Badge.objects.get(pk=badge_id)
            user.badge.add(badge)
            badgecount += 1
            instance.user.badgecount = badgecount
            instance.user.save()  # Silver Badge
        elif like_count == 3:
            badge_id = 6
            badge = Badge.objects.get(pk=badge_id)
            user.badge.add(badge) 
            badgecount += 1
            instance.user.badgecount = badgecount
            instance.user.save() # Gold Badge
            
class PostLikes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)    

class PostDislike(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)    

class AnswerLikes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)    

class AnswerDislike(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)    

class Goruntulenme(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class SavedQuestion(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_saved = models.DateTimeField(auto_now_add=True)

class UserBadge(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)    

    def __str__(self):
        return f"{self.user.username}'ın {self.badge.name} Rozeti"