from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Board, List, Card


@login_required
def CreateBoard(request):
    if request.method == 'POST':
        board = Board.objects.create(name=request.POST.get('name'))
        board.members.add(request.user)
        board.admins.add(request.user)
        board.save()
        return render(request, 'main/index.html')
    return render(request, 'boards/create_board.html')


def CreateList(request):
    if request.method == 'POST':
        board_id = request.board_id
        board = get_object_or_404(Board, board_id=board_id)
        list1 = List.objects.create(name=request.POST.get('name'))
        board.lists.add(list1)
    return render(request, 'boards/create_list.html')


def CreateCard(request):
    if request.method == 'POST':
        list_id = request.list_id
        list1 = get_object_or_404(List, board_id=list_id)
        card = Card.objects.create(name=request.POST.get('name'))
        list1.lists.add(card)
    return render(request, 'boards/create_card.html')
