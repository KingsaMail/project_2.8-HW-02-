from objects import GameBoard, Player, Compucter
from game_play import GamePlay


if __name__ == "__main__":
    flag = True
    while flag:  #цикл инициализации.
        initial = GameBoard()
        initial.board_drow('расстановки кораблей')
        print('\n На доске должно находится следующее количество кораблей:\n',\
            ' 1 корабль на 3 клетки;\n',\
            ' 2 корабля на 2 клетки;\n',\
            ' 4 корабля на одну клетку.\n',\
            'Корабли должны находится на расстоянии минимум одной клетки друг от друга.\n',
            'Введите координаты короблей в формате 1абв или а123 (пример для коробля на три клетки).')
        #initial.installation_ship() # ставим корабли
        #initial.board_drow('восстанавливаем клетки')
        #comp = Compucter()                                  #!!!!!!!!!!удалить после отладки
        plaer = Player(initial.installation_ship())   #исправить после отладки comp Compucter.initial_ship_comp()
        computer = Compucter()
        computer.initial_ship_comp()
        raund = GamePlay(plaer, computer)
        raund.run()
        flag = True if input("Сыграем ещё? (Y/y)") in ['Y', 'y'] else False
        
                
        break
        