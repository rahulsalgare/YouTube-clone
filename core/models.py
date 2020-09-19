from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Channel(models.Model):
    channel_owner = models.OneToOneField('UserProfile',null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Video(models.Model):
    video_title = models.CharField(max_length=50)
    video_description = models.TextField()
    published_date = models.DateField(auto_now=True)
    video_owner = models.ForeignKey(Channel, on_delete=models.CASCADE)
    video_file= models.FileField(upload_to='videos/', null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/',null=True)
    # likers = models.ManyToManyField(UserProfile,through='Like')


    # def increment(self):
    #     self.likes += 1
    #     self.save()

    def __str__(self):
        return self.video_title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='profilepic/default.png', upload_to='profilepic/', null=True)
    cover_pic = models.ImageField(default='coverpic/default.jpg', upload_to='coverpic/',null=True)
    # liked_videos = models.ForeignKey('Video', null=True, on_delete=CASCADE)
    liked_videos = models.ManyToManyField(Video, null=True)

    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse('core:profile',kwargs={'user':user})

class Comment(models.Model):
    comment_text = models.TextField(max_length=300)
    comment_datetime = models.DateTimeField(blank=False, null=False)
    comment_owner = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    commented_video = models.ForeignKey('Video', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text

# class Like(models.Model):
#     userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     video = models.ForeignKey(Video,on_delete=models.CASCADE)
