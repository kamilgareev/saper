from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from .serializers import GameSerializer
from .models import Game
from .utils import game_is_won, update_field, set_field_with_mines, zero_case


class NewGame(CreateAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            if (data['mines_count'] >= data['width'] * data['height']) or (data['mines_count'] < 1):
                return Response({"message": f"Количество ячеек должно быть не менее 1 и строго меньше "
                                            f"{data['width'] * data['height']}"}, status=status.HTTP_400_BAD_REQUEST)
            return Response(data, status=status.HTTP_200_OK)
        return Response({"message": "Проверьте корректность введенных данных"}, status=status.HTTP_400_BAD_REQUEST)


class Turn(RetrieveAPIView):
    serializer_class = GameSerializer

    def post(self, request, *args, **kwargs):
        try:
            game = Game.objects.get(game_id=request.data['game_id'])
        except Game.DoesNotExist:
            return Response({"message": "Игра не найдена"},
                            status=status.HTTP_404_NOT_FOUND)
        if game.completed:
            return Response({"message": "Игра уже завершена"},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            row = request.data['row']
            col = request.data['col']
        except KeyError:
            return Response({"message": "Значения row и col должны быть указаны"},
                            status=status.HTTP_400_BAD_REQUEST)
        if row >= game.height or col >= game.width or row < 0 or col < 0:
            return Response({"message": f"Допустимые значения для row: от 0 до {game.height - 1}, "
                                        f"для col: от 0 до {game.width - 1}"},
                            status=status.HTTP_400_BAD_REQUEST)
        if not game.field_with_mines:
            game.field_with_mines = set_field_with_mines(game, row_=row, col_=col)
        if game.field[row][col] != ' ':
            return Response({"message": "Ячейка уже открыта"},
                            status=status.HTTP_400_BAD_REQUEST)
        if int(game.field_with_mines[row][col]) > 0:
            game.field[row][col] = game.field_with_mines[row][col]
            if not game_is_won(game.field, game.field_with_mines):
                game.save()
                serializer = GameSerializer(game)
                data = serializer.data
                return Response(data,
                                status=status.HTTP_200_OK)
            update_field(game, symbol='M')
            game.completed = True
            game.save()
            serializer = GameSerializer(game)
            data = serializer.data
            return Response(data,
                            status=status.HTTP_200_OK)
        if int(game.field_with_mines[row][col]) < 0:
            update_field(game, symbol='X')
            game.completed = True
            game.save()
            serializer = GameSerializer(game)
            data = serializer.data
            return Response(data,
                            status=status.HTTP_200_OK)
        if game.field_with_mines[row][col] == '0':
            zero_case(game, row=row, col=col)
            if not game_is_won(game.field, game.field_with_mines):
                game.save()
                serializer = GameSerializer(game)
                data = serializer.data
                return Response(data,
                                status=status.HTTP_200_OK)
            update_field(game, symbol='M')
            game.completed = True
            game.save()
            serializer = GameSerializer(game)
            data = serializer.data
            return Response(data,
                            status=status.HTTP_200_OK)
