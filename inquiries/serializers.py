from rest_framework import serializers
from inquiries.models import Inquiry, Comment


# class CommentSerializer(serializers.ModelSerializer):
#      class Meta:
#         model = Comment
#         fields = "__all__"

# class CommentCreateSerializer(serializers.ModelSerializer):
#      class Meta:
#         model = Comment
#         fields = ("cmt_content",)