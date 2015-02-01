from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

from .models import Post, NoteToPost


class SearchingForm(forms.Form):
    word = forms.CharField(label='Wpisz szukaną frazę')


class RegisterForm(forms.Form):
    login = forms.CharField(label='login')
    password = forms.CharField(
        label='hasło',
        widget=forms.PasswordInput,
        validators=[MinLengthValidator(6)],
        error_messages={'min_length': u'Hasło musi mieć co najmniej 6 znaków'}
    )

    password2 = forms.CharField(
        label='powtórz hasło', widget=forms.PasswordInput)
    email = forms.EmailField(label='e-mail', widget=forms.EmailInput)

    def clean_login(self):
        login = self.cleaned_data.get('login')
        if User.objects.filter(username=login):
            raise forms.ValidationError(u'Podany login istnieje w bazie')
        return login

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError(u'Podane hasła nie są zgodne')
        return password2


class LoginForm(forms.Form):
    login = forms.CharField(label='login')
    password = forms.CharField(label='hasło', widget=forms.PasswordInput)

    def clean_login(self):
        login = self.cleaned_data.get('login')
        if not User.objects.filter(username=login):
            raise forms.ValidationError(u'Podany login nie istnieje w bazie')
        return login


class AddNewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'dim', 'categories', 'picture']
        labels = {
            'title': 'Tytuł',
            'text': 'Treść',
            'dim': 'Post z części włoskiej?',
            'categories': 'Kategoria',
            'picture': 'Obrazek',
        }

    def __init__(self, *args, **kwargs):
        super(AddNewPostForm, self).__init__(*args, **kwargs)
        self.fields['categories'].empty_label = None


class ReportMistakeToPost(forms.Form):
    author = forms.CharField(label='autor', required=False)
    email = forms.EmailField(label='e-mail', widget=forms.EmailInput)
    text = forms.CharField(label='opis', widget=forms.Textarea)

    def save(self, **kwargs):
        post_id = self.cleaned_data['post_id']
        post = Post.objects.get(pk=post_id)
        email = self.cleaned_data['email']
        text = self.cleaned_data['text']
        note = NoteToPost.objects.create(post_id=post, email=email,
            submited_date=datetime.now().date(), text=text, is_accepted=False)
        user_id = self.cleaned_data.get('user_id')
        if user_id:
            note.author = User.objects.get(pk=user_id)
        else:
            note.anon_author = self.cleaned_data['author']
        note.save()


class AcceptNoteToPostForm(forms.Form):
    new_text = forms.CharField(
        label='Nowa treść',
        widget=forms.Textarea,
        required=True)

    def save(self):
        note_id = self.cleaned_data['note_id']
        note = NoteToPost.objects.get(id=note_id)
        superuser = self.cleaned_data['superuser']
        today = datetime.now().date()

        note.is_accepted = True
        note.accept_date = today
        note.accept_superuser = superuser
        note.save()

        post = note.post_id
        new_text = self.cleaned_data['new_text']
        post.old_text = post.text
        post.text = new_text
        # change posted_date into today
        post.posted_date = today
        post.save()


class RefuseNoteToPostForm(forms.Form):
    refusal_reason = forms.CharField(
        label='Przyczyna odrzucenia',
        widget=forms.Textarea,
        required=True)

    def save(self):
        note_id = self.cleaned_data['note_id']
        refusal_reason = self.cleaned_data['refusal_reason']
        note = NoteToPost.objects.get(id=note_id)
        superuser = self.cleaned_data['superuser']

        note.is_accepted = True
        note.accept_date = datetime.now().date()
        note.accept_superuser = superuser
        note.refusal_reason = refusal_reason
        note.is_refused = True
        note.save()
