from django.forms import ModelForm, HiddenInput

from blog.models import Comment


class CommentForm (ModelForm):
    class Meta:
        model=Comment
        fields=["name","message","post"]
        widgets={"post":HiddenInput()}