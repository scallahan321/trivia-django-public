from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer, ViewStatsSerializer
from .logic import GameSetup
from .models import Stats


def index(request):
    hello = {"hello": "world"}
    return JsonResponse(hello)


class UserCreateView(generics.CreateAPIView):
    model = get_user_model()
    parser_classes = [MultiPartParser, JSONParser]
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def questions(request):
    data = request.data
    category = data["category"]
    game = GameSetup(category)
    questions = game.load_questions()
    return JsonResponse(questions)


@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def LeaderBoardView(request):
    data = request.data
    category = data["category"]
    scores = []
    stats = Stats.objects.all()
    for s in stats:
        username = s.user_ref.username
        percent = s.percent_correct(category)
        scores.append([username, percent])

    ranked = sorted(scores, key=lambda x: x[1], reverse=True)
    leaders = {}
    leaders['first'] =  {"username": ranked[0][0], "percent": ranked[0][1]}
    leaders['second'] = {"username": ranked[1][0], "percent": ranked[1][1]}
    leaders['third'] = {"username": ranked[2][0], "percent": ranked[2][1]}
    return JsonResponse(leaders)


class ViewUserStats(generics.ListAPIView):
    serializer_class = ViewStatsSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Stats.objects.all()

    def get(self, request):
        headers = request.headers
        token = headers['Authorization'][6:]
        user_instance = Token.objects.filter(key=token).first().user
        stats_instance = Stats.objects.filter(user_ref = user_instance).first()
        if not stats_instance:
            return Response({'questions_attempted'})
        serializer = ViewStatsSerializer(stats_instance)
        return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def UpdateStats(request):
    data = request.data
    headers = request.headers
    token = headers['Authorization'][6:]
    user_instance = Token.objects.filter(key=token).first().user
    stats_instance = Stats.objects.filter(user_ref = user_instance).first()
    if stats_instance:
        stats_instance.update(data)
        stats_instance.save()
    else:
        stats_instance = Stats.objects.create(user_ref = user_instance)
        stats_instance.update(data)
        stats_instance.save()

    return Response({"success": f"Stats '{stats_instance}' updated successfully"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def LogoutView(request):
    data = request.data
    username = data['username']
    headers = request.headers
    #slice authorization string after "Token "
    token = headers['Authorization'][6:]
    token_instance = Token.objects.filter(key=token).first()
    #delete token
    token_instance.delete()
    return Response(f"{username} is logged out.")
