from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from serializers import PostSerializer
from pbox_backend.models import Post

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def index(request):
    posts = Post.objects.all()[:12]
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)