from .models import Post
import django_filters
 
 
class BookFilter(django_filters.FilterSet):
 
    class Meta:
        model = Post
        fields = '__all__'