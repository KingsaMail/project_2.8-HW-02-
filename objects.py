from random import randint

class Ship:
    """Класс коробля."""
    
    def __init__(self, cord:list, life:int) -> None:
        self.__cord:list = cord
        self.__life:int = life
        
    @property
    def cord(self):
        return self.__cord
    
    @property
    def life(self):
        return self.__life


class GameBoard:
    """Класс игрового поля."""
    
    def __init__(self) -> None:
        self.player_field = [['O']*6 for i in range(6)]
    
    #рисуем игровое поле
    def board_drow(self, name:str): #name - это или игрока или компьютера
        print(f'\n    Поле {name}')
        print(f"        {1}   {2}   {3}   {4}   {5}   {6}")
        my_list = [' а(f)', ' б(,)', ' в(d)', ' г(u)', ' д(l)', ' е(t)']
        for i, lit in zip(self.player_field, my_list):
            print(lit, end="")
            for j in i:
                print(' |', j, end='')
            print(' |')
            
    #расстановка кораблей
    def installation_ship(self)->list: # получаем список кораблей, релевантные координаты
        
        def get_cord(ship_cor:str)->list: #получаем координатыы коробля
            total_list_num = [] #список для цифровой составляющей
            total_list_alp = [] #список для буквенной составляющей
            total = [] #  список на отдачу (координаты корабля)
            for i in ship_cor: #делим строку ввода на два списка
                if i.isnumeric():
                    total_list_num.append(i)
                else:
                    total_list_alp.append(i)
            
            for i in total_list_alp: #находим координаты
                var = 'абвгдеf,dult'.find(i)
                var = var if var<6 else var-6
                for j in total_list_num:
                    total.append((var, int(j)-1))
            return total                    
        
        player_ships = [] #список короблей координаты + жизни
        all_set = {'а', 'б', 'в', 'г', 'д', 'е', #разметка поля
                        '1', '2', '3', '4', '5', '6', #(возможные комбинации ввода).
                        'f', ',', 'd', 'u', 'l', 't'}
        ship_list = [['первый', 3], ["второй", 2], ["третий", 2], ["четвёртый", 1], ["пятый", 1], ["шестой", 1], ["седьмой", 1]]
        while ship_list: # цикл расстановки кораблей
            ship_cord = input(f' куда ставим {ship_list[0][0]} корабль (длинной - {ship_list[0][1]})? ')
            # проверка соответствия введеных координат значениям осей.            
            if set(list(ship_cord)).intersection(all_set) == set(list(ship_cord)):
                
                ship_cord = get_cord(ship_cord) #получаем координаты корабля.
                if len(ship_cord) != ship_list[0][1]: #проверяем что корабль нужной длинны
                    print(" не правильная длинна корабля")
                    continue
                #проверка что в заданных координатах можно ставить корабль.
                flag = True                
                for i in  ship_cord:                                        
                    if (self.player_field[i[0]][i[1]] != 'O') and (self.player_field[i[0]][i[1]] in ['o', '#']):
                        flag = False
                        print(" Здесь корабль ставить нельзя")                                                
                        break
                if not flag:
                    continue    
                if flag: #ставим корабль (координаты валидны), помечаем доску где нельзя ставить
                    for i in ship_cord:                        
                        if i[0]==0:
                            self.player_field[i[0]+1][i[1]] = 'o'
                        elif i[0]==5:
                            self.player_field[i[0]-1][i[1]] = 'o'
                        elif (i[0]>0) and (i[0]<5):
                            self.player_field[i[0]-1][i[1]] = 'o'
                            self.player_field[i[0]+1][i[1]] = 'o'
                        if i[1]==0:
                            self.player_field[i[0]][i[1]+1] = 'o'
                        elif i[1]==5:
                            self.player_field[i[0]][i[1]-1] = 'o'
                        elif (i[1]>0) and (i[1]<5):
                            self.player_field[i[0]][i[1]-1] = 'o'
                            self.player_field[i[0]][i[1]+1] = 'o'
                        #закрываем углы
                        if (i[0]==0) and (i[1]==0): 
                            self.player_field[i[0]+1][i[1]+1] = 'o'
                        elif (i[0]==0) and (i[1]==5):
                            self.player_field[i[0]+1][i[1]-1] = 'o'
                        elif (i[0]==5) and (i[1]==0): 
                            self.player_field[i[0]-1][i[1]+1] = 'o'
                        elif (i[0]==5) and (i[1]==5): 
                            self.player_field[i[0]-1][i[1]-1] = 'o'
                        #закрываем грани
                        elif (i[0]==0): 
                            self.player_field[i[0]+1][i[1]-1] = 'o'
                            self.player_field[i[0]+1][i[1]+1] = 'o'
                        elif (i[0]==5):
                            self.player_field[i[0]-1][i[1]-1] = 'o'
                            self.player_field[i[0]-1][i[1]+1] = 'o'
                        elif (i[1]==0): 
                            self.player_field[i[0]-1][i[1]+1] = 'o'
                            self.player_field[i[0]+1][i[1]+1] = 'o'
                        elif (i[1]==5): 
                            self.player_field[i[0]-1][i[1]-1] = 'o'
                            self.player_field[i[0]+1][i[1]-1] = 'o'
                        #закрываем поле
                        else: 
                            self.player_field[i[0]-1][i[1]-1] = 'o'
                            self.player_field[i[0]-1][i[1]+1] = 'o'
                            self.player_field[i[0]+1][i[1]-1] = 'o'
                            self.player_field[i[0]+1][i[1]+1] = 'o'
                    for i in ship_cord:
                        self.player_field[i[0]][i[1]] = '#'
                        
            else:
                print(" попробуйте ещё раз")
                continue                        
            player_ships.append(Ship(ship_cord, ship_list[0][1]))
            GameBoard.board_drow(self, 'расстановка кораблей')
            ship_list.pop(0)
        for i in range(6):
            for j in range(6):
                self.player_field[i][j] = self.player_field[i][j].upper()
        
        return player_ships       
                        


class Player:
    """Класс игрока."""        
    
    def __init__(self, ship_list:list) -> None:
        self._ship_list:list = ship_list
        
    @property
    def ship_list(self):
        return self._ship_list
    
       
        
if __name__ == '__main__':
    draft = GameBoard()
    draft.board_drow('игрока')