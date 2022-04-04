from rest_framework import serializers

from api.models import Book

class BookSerializer(serializers.ModelSerializer):

    # publish = serializers.CharField(source='publish.name')

    class Meta:
        model = Book
        # fields = '__all__'
        # depth = 1
        fields = ('name', 'price', 'author', 'author_list', 'publish', 'publish_name')

        extra_kwargs = {
            'publish':{'write_only':True},
            'publish_name':{'read_only':True},
            'author':{'write_only':True},
            'author_list':{'read_only':True},
        }