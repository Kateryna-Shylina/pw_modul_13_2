from django.forms import ModelForm, CharField, TextInput, ModelChoiceField, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import Tag, Authors, Qoutes


class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(ModelForm):

    fullname = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    born_date = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    born_location = CharField(min_length=5, max_length=150, required=True, widget=TextInput())
    description = CharField(min_length=10, max_length=5000, required=True, widget=TextInput())

    class Meta:
        model = Authors
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):

    author = ModelChoiceField(queryset=Authors.objects.all(), required=True)
    quote = CharField(min_length=10, max_length=5000, required=True, widget=TextInput())

    class Meta:
        model = Qoutes
        fields = ['author', 'quote']
        exclude = ['tags']