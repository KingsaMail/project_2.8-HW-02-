from random import randint

class Ship:
    """Класс коробля."""
    
    def __init__(self, cord:list) -> None:
        self.__cord:list = cord
        #self.__life:int = life
        
    @property
    def cord(self):
        return self.__cord
    
        
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
            total_list_num = [] #список для цифровой составляющ
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
            player_ships.append(Ship(ship_cord)) #, ship_list[0][1]
            GameBoard.board_drow(self, 'расстановка кораблей')
            ship_list.pop(0)
        for i in range(6):
            for j in range(6):
                self.player_field[i][j] = self.player_field[i][j].upper()        
        
        return player_ships       
                        

class Player:
    """Класс игрока."""        
    
    def __init__(self, ship_list:list=None) -> None:
        self._ship_list:list = ship_list # должны получить список кораблей, как класов 
        
    @property
    def ship_list(self):
        return self._ship_list
    
    @ship_list.setter
    def ship_list(self, ship_list:list):
        self._ship_list:list = ship_list
        
    def ships_list_set(self):
        """Если корабль потоплен, то он удаляется из списка."""
        for i in self._ship_list:
            if not i.cord:    #shep_cord:
                self._ship_list.remove(i)
        
        
class Compucter():
    "Класс компьютер."
    
    def __init__(self) -> None:        
        self.field_start = [['O']*8 for i in range(8)]
        self.field_c = [['O']*6 for i in range(6)]
        self.ships_list:list = [] #список кораблей, как классов
        
    def ships_list_set(self):
        """Если корабль потоплен, то он удаляется из списка."""
        for i in self.ships_list:
            if not i.cord:
                self.ships_list.remove(i)
        
    def player_field_c_set(self):
        self.field_c = self.field_start[1:7][:]
        var = 0
        for i in self.field_c:
            self.field_c[var] = self.field_c[var][1:7]
            var+=1
        
    #рисуем игровое поле компьютера (метод для отладки игры)    
    def board_drow(self, name:str): #name - это или игрока или компьютера
        print(f'\n    Поле {name}')
        print(f"        {1}   {2}   {3}   {4}   {5}   {6}")
        my_list = [' а(f)', ' б(,)', ' в(d)', ' г(u)', ' д(l)', ' е(t)']
        for i, lit in zip(self.field_c, my_list):
            print(lit, end="")
            for j in i:
                print(' |', j, end='')
            print(' |')
            
            
            
    def initial_ship_comp(self):
        #ставим корабли компютера.
        ship_list_project = [['первый', 3], ["второй", 2], ["третий", 2], ["четвёртый", 1], ["пятый", 1], ["шестой", 1], ["седьмой", 1]]
        count = 0
        while ship_list_project:
            count+=1 # счётчик контроля зацикливания
            #генерим точку и направление для стартовой позиции корабля
            x, y, vec = randint(1,6), randint(1,6), randint(0,3)
            
            #если зацикливается, сбрасываем поле и генерируем заново
            if count == 50: 
                ship_list_project = [['первый', 3], ["второй", 2], ["третий", 2], ["четвёртый", 1], ["пятый", 1], ["шестой", 1], ["седьмой", 1]]
                count = 0
                self.field_start = [['O']*8 for i in range(8)]
                self.ships_list = []
                continue
            
            # если нельзя ставить в это место корабль, то перезапускаем итерацию                
            if self.field_start[x][y] != 'O':
                continue
            
            # временный список, для координат кораблей
            ship_var = []
            ship_var.append((x,y))                      
            for i in range(ship_list_project[0][1]-1):  
                # добавляем координаты если выпало по вертикали              
                if (vec==0) and (i==0):
                    if (x-1)>0:
                        xi = x - 1
                    else:
                        xi = x + 1
                        vec = 2
                    ship_var.append((xi,y))                    
                if (vec==2) and (i==0):
                    if (x+1)<7:
                        xi = x + 1
                    else:
                        xi = x - 1
                        vec = 0
                    ship_var.append((xi,y))                    
                if (vec==0) and (i==1):
                    xi = xi - 1 if (xi-1)>0 else xi + 2
                    ship_var.append((xi,y))                    
                if (vec==2) and (i==1):
                    xi = xi + 1 if (xi+1)<7 else xi - 2
                    ship_var.append((xi,y))                    
                # добавляем координаты если выпало по горизонтали
                if (vec==1) and (i==0):
                    if (y-1)>0:
                        yi = y - 1
                    else:
                        yi = y + 1
                        vec = 3
                    ship_var.append((x,yi))                    
                if (vec==3) and (i==0):
                    if (y+1)<7:
                        yi = y + 1
                    else:
                        yi = y - 1
                        vec = 1
                    ship_var.append((x,yi))                    
                if (vec==1) and (i==1):
                    yi = yi - 1 if (yi-1)>0 else yi + 2
                    ship_var.append((x,yi))                    
                if (vec==3) and (i==1):
                    yi = yi + 1 if (yi+1)<7 else yi - 2
                    ship_var.append((x,yi))                    
                else:
                    continue
            
            #если в этих координатах нельзя ставить корабль, то список кораблей не меняется
            #и корабль создаётся заново
            flag = True
            for i in ship_var:
                if self.field_start[i[0]][i[1]] != "O":
                    flag = False
            
            
            if flag:
                #окружаем все точки корабля запретной зоной
                for i in ship_var:
                    self.field_start[i[0]][i[1]+1] = "o"
                    self.field_start[i[0]+1][i[1]+1] = "o"
                    self.field_start[i[0]+1][i[1]] = "o"
                    self.field_start[i[0]+1][i[1]-1] = "o"
                    self.field_start[i[0]][i[1]-1] = "o"
                    self.field_start[i[0]-1][i[1]-1] = "o"
                    self.field_start[i[0]-1][i[1]] = "o"
                    self.field_start[i[0]-1][i[1]+1] = "o"
                
                #ставим корабль
                for i in ship_var:
                    self.field_start[i[0]][i[1]] = '#'                
                
                #уменьшаем координаты на 1, в обеех плоскостях
                ship_var_ = []
                for i in ship_var:
                    ship_var_.append((i[0]-1, i[1]-1))
                
                #print(ship_var_)
                #добавляем в список жизни
                #ship_var.append(ship_list_project[0][1])           
                #берём следующий по списку корабль                
                
                self.ships_list.append(Ship(ship_var_))  # ship_list_project[0][1]
                ship_list_project.pop(0)                
                
                
        #возвращаем список кораблей, через метод экземпляра
               
        Compucter.player_field_c_set(self)   
       
        
if __name__ == '__main__':
    comp = Compucter()        
    comp.initial_ship_comp()
    comp.board_drow('инициализации')