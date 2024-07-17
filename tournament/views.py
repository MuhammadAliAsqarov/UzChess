from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404
from .models import Player, Tournament, Match
from .serializers import PlayerSerializer, TournamentSerializer, MatchSerializer


class PlayerViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser]

    def list(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        player = Player.objects.get(pk=pk)
        if player:
            serializer = PlayerSerializer(player)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(data={'message': 'Player not found', 'ok': False}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        player = Player.objects.get(pk=pk)
        if player is None:
            return Response(data={'message': 'Player not found', 'ok': False}, status=status.HTTP_404_NOT_FOUND)
        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        player = Player.objects.get(pk=pk)
        if player is None:
            return Response(data={'message': 'Player not found', 'ok': False}, status=status.HTTP_404_NOT_FOUND)
        player.delete()
        return Response(data={'message': 'Player deleted successfully', 'ok': True}, status=status.HTTP_204_NO_CONTENT)


class TournamentViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser]

    def list(self, request):
        tournaments = Tournament.objects.all()
        serializer = TournamentSerializer(tournaments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = TournamentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        tournament = Tournament.objects.get(pk=pk)
        if tournament is None:
            return Response(data={'message': 'Tournament not found', 'ok': False}, status=status.HTTP_404_NOT_FOUND)
        serializer = TournamentSerializer(tournament)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        tournament = Tournament.objects.get(pk=pk)
        if tournament is None:
            return Response(data={'message': 'Tournament not found', 'ok': False}, status=status.HTTP_404_NOT_FOUND)
        serializer = TournamentSerializer(tournament, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        tournament = Tournament.objects.get(pk=pk)
        if tournament is None:
            return Response(data={'message': 'Tournament not found', 'ok': False}, status=status.HTTP_404_NOT_FOUND)
        tournament.delete()
        return Response(data={'message': 'Tournament deleted successfully', 'ok': True},
                        status=status.HTTP_204_NO_CONTENT)


class MatchViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser]

    def list(self, request):
        matches = Match.objects.all()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        match = Match.objects.get(pk=pk)
        if match is None:
            return Response(data={'message': 'Match not found', 'ok': False}, status=status.HTTP_404_NOT_FOUND)
        serializer = MatchSerializer(match)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        match = Match.objects.get(pk=pk)
        if match is None:
            return Response(data={'message': 'Match not found', 'ok': False}, status=status.HTTP_404_NOT_FOUND)
        serializer = MatchSerializer(match, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        match = Match.objects.get(pk=pk)
        if match is None:
            return Response(data={'message': 'Match not found', 'ok': False}, status=status.HTTP_404_NOT_FOUND)
        match.delete()
        return Response(data={'message': 'Match deleted successfully', 'ok': True}, status=status.HTTP_204_NO_CONTENT)
