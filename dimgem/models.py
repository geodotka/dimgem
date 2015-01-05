from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    icon = models.ImageField('Ikonka Kategorii', upload_to='icons',
                              blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    posted_date = models.DateField()
    author = models.CharField(max_length=50)
    text = models.TextField()
    dim = models.BooleanField()
    categories = models.ForeignKey(Category)
    old_text = models.TextField(null=True, blank=True)
    picture = models.ImageField(
        upload_to='post_pictures', null=True,  blank=True)
    is_approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return self.title

    @property
    def votes_up(self):
        return Vote.objects.filter(post=self, vote=True).count()

    @property
    def votes_down(self):
        return Vote.objects.filter(post=self, vote=False).count()


class Vote(models.Model):
    ip = models.IPAddressField()
    vote = models.BooleanField()
    post = models.ForeignKey(Post)


class NoteToPost(models.Model):
    """
    if is_accepted == False, note is not seen by superuser
    if is_accepted == True and is_refused == False, note is seen and accpeted
        by superuser
    if is_accepted == True and is_refused == True, note is seen and refused
        by superuser
    """
    post_id = models.ForeignKey(Post)
    author = models.ForeignKey(User, null=True, blank=True,
                               related_name=u'note_to_post')
    anon_author = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    submited_date = models.DateField()
    text = models.TextField(verbose_name=u'Treść')
    is_accepted = models.BooleanField()
    accept_date = models.DateField(null=True, blank=True)
    accept_superuser = models.ForeignKey(User, null=True, blank=True,
        related_name=u'superuser_corrected_post')
    refusal_reason = models.TextField(null=True, blank=True)
    is_refused = models.BooleanField(default=False)
