from .models import Match


def generate_pairings(tournament):
    participants = list(tournament.participants.all())
    participants.sort(key=lambda player: player.rating, reverse=True)
    pairings = []

    for i in range(0, len(participants), 2):
        if i + 1 < len(participants):
            pairings.append((participants[i], participants[i + 1]))

    for round_number, (player1, player2) in enumerate(pairings, start=1):
        Match.objects.create(tournament=tournament, player1=player1, player2=player2, round_number=round_number)
