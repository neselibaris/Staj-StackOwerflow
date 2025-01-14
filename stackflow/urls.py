
from django.contrib import admin
from django.urls import path
from userapp.views import *
from profileApp.views import * 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="home"),
    path("profile/<uuid:user_uuid>/", profile, name="profile"),
    path("questions", questions, name="questions"),
    path("questionsDetail/<questionId>", questionDetails, name="questionDetails"),
    path("tags", tags, name="tags"),
    path("tagDetail/<tagId>", tagDetail, name="tagDetail"),
    path("users", users, name="users"),
    path("login", Login, name="login"),
    path("error", error, name="404"),
    path('register', register, name='register'),
    path('logout', cikis,name='logout'),
    path('profile/activity', activity, name="activity"),
    path("edit_profile", edit_profile, name="edit_profile"),
    path("createpost", createpost, name="createpost"),
    path("createComment/<questionId>", commentCreate, name="commentCreate"),
    path("createComment2/<answerId>/<questionId>", commentCreate2, name="commentCreate2"),    
    path("postlike/<userId>/<postId>", addLike, name="postlike"),    
    path("postdislike/<userId>/<postId>", dislike, name="dislike"),        
    path("answerlike/<userId>/<answerId>", answerlike, name="answerlike"),    
    path("answerdislike/<userId>/<answerId>", answerdislike, name="answerdislike"),
    path("user/<uuid:user_uuid>", userProfile, name="userProfile"),
    path('follow/<uuid:user_uuid>', follow_view, name='follow'),
    path('unfollow/<uuid:user_uuid>', unfollow_view, name='unfollow'),
    path('save_question/<int:questionId>/',save_question, name='save_question'),
    path('user-activity/<uuid:user_uuid>',userActivity, name="userActivity")
       

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
