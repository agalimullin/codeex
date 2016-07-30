from django.forms import ModelForm

from goldenshop.models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review_text']
