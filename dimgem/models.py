from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from .const import DIM, GEM, PAGINATE_BY


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
    dim = models.BooleanField(default=None)
    categories = models.ForeignKey(Category)
    old_text = models.TextField(null=True, blank=True)
    picture = models.ImageField(
        upload_to='post_pictures', null=True,  blank=True)
    is_approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    @property
    def votes_up(self):
        return Vote.objects.filter(post=self, vote=True).count()

    @property
    def votes_down(self):
        return Vote.objects.filter(post=self, vote=False).count()

    @property
    def url(self):

        dct = {
            'dim': {
                'Gramatyka': 'dim_grammar',
                'Słownictwo': 'dim_vocabulary',
                'Ciekawostki': 'dim_curiosities',
                'False friends': 'dim_false_friends'
            },
            'gem': {
                'Gramatyka': 'gem_grammar',
                'Słownictwo': 'gem_vocabulary',
                'Ciekawostki': 'gem_curiosities',
                'False friends': 'gem_false_friends'
            }
        }
        dimgem_type = DIM if self.dim else GEM
        category = self.categories.name
        view_name = dct[dimgem_type][category]

        url = reverse(view_name)
        dim = True if dimgem_type == DIM else False
        posts = Post.objects.filter(dim=dim, categories__name=category,
                                    is_approved=True, id__gte=self.id)
        number_of_posts_lte_self = posts.count()
        paginate_by = PAGINATE_BY
        page_number = number_of_posts_lte_self // paginate_by
        if number_of_posts_lte_self % paginate_by != 0:
            page_number += 1
        if page_number == 1:
            url += '#{}'.format(self.id)
        else:
            url += '?page={}#{}'.format(page_number, self.id)
        return url


class Vote(models.Model):
    ip = models.IPAddressField()
    vote = models.BooleanField(default=None)
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
    is_accepted = models.BooleanField(default=None)
    accept_date = models.DateField(null=True, blank=True)
    accept_superuser = models.ForeignKey(User, null=True, blank=True,
        related_name=u'superuser_corrected_post')
    refusal_reason = models.TextField(null=True, blank=True)
    is_refused = models.BooleanField(default=False)
