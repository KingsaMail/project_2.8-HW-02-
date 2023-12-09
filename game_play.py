from random import shuffle

class ErrorGames(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        print(f"Errors: Out of range")

class GamePlay:
    """Класс игровой логики."""
    def __init__(self, plaer, comp) -> None:
        self._plaer = plaer
        self._comp = comp
        self.drow = Drow()
    
    def run(self):
        
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
            return total[0]
                
        all_set = {'а', 'б', 'в', 'г', 'д', 'е', #разметка поля
                        '1', '2', '3', '4', '5', '6', #(возможные комбинации ввода).
                        'f', ',', 'd', 'u', 'l', 't'}
        
        #варианты ходов компьютера
        comp_list_var = []
        for i in range(6):
            for j in range(6):
                comp_list_var.append((i, j))
        shuffle(comp_list_var) #перемешиваем
        
        flag =True
        self.drow.drow() #рисуем доску
        while flag: #цикл раунда
            while True: # цикл хода игрока
                if not self._comp.ships_list:
                    print()
                    print("Поздравляем, Вы выиграли!!!")
                    flag = False
                    break
                print()
                 
                self.event = input("введите вашь ход(например 1а или а1) (q/Q выход): ")
                if self.event in ['q', 'Q']:
                    exit()
            # проверка соответствия введеных координат значениям осей.  
                if set(list(self.event)).intersection(all_set) == set(list(self.event)):                    
                    if len(self.event) != 2: #проверяем что координата одна
                        print(" так нельзя попробуйте ещё раз")                        
                        continue
                else:
                    continue
                self.event = get_cord(self.event) #получаем координаты выстрела.
                var = 'T'
                for i in self._comp.ships_list:                                        
                    for j in i.cord:                        
                        if j == self.event:
                            var = 'X'
                            i.cord.remove(j)                            
                            self._comp.ships_list_set()# удаляем подбитый корабль(секцию) из списка                    
                                
                self.drow.comp_dict_set(self.event, var) #координаты выстрела на доску
                self.drow.drow() #рисуем доску                
                
                if var == "T": # если промахнулись выходим из цикла хода игрока
                    break
            if flag == False:
                break                
            
            while True: #цикл хода компьютера
                
                if not self._plaer.ship_list:
                    print()
                    print("Вы проиграли.")
                    flag = False
                    break
                var = 'T'                
                if comp_list_var:
                    shoot = comp_list_var.pop()
                    for i in self._plaer.ship_list:                        
                        for j in i.cord:                            
                            if j == shoot:
                                var = 'X'
                                i.cord.remove(shoot)
                                self._plaer.ships_list_set()
                self.drow.plaer_dict_set(shoot, var) #координаты выстрела на доску
                self.drow.drow() #рисуем доску
                if shoot[0] == 0:
                    messeg = 'a'
                elif shoot[0] == 1:
                    messeg = 'б'
                elif shoot[0] == 2:
                    messeg = 'в'
                elif shoot[0] == 3:
                    messeg = 'г'
                elif shoot[0] == 4:
                    messeg = 'д'
                else:
                    messeg = 'е'
                print('(', messeg, shoot[1]+1, ')') 
                
                if var == "T": # если промахнулись выходим из цикла хода игрока
                    break
            
            if flag == False:
                break
    

class Drow:
    """Рисуем поле."""
    
    def __init__(self) -> None:
        self._plaer_dict:dict = {}
        self._plaer_dict = self.init_dict(self._plaer_dict)
        self._comp_dict:dict = {}
        self._comp_dict = self.init_dict(self._comp_dict)
    
    #задаём изначально пустые поля для прорисовки    
    def init_dict(self, var:dict):        
        for i in range(7):
            for j in range(7):
                var[(i,j)] = 'O'
        return var     
    
    #меняем значение на поле игрока    
    def plaer_dict_set(self, key_var:tuple, item_var:str):
        self._plaer_dict[key_var[0]+1, key_var[1]+1] = item_var
        
    #меняем значение на поле компьютера    
    def comp_dict_set(self, key_var:tuple, item_var:str):
        if self._comp_dict[key_var[0]+1, key_var[1]+1] == 'O':
            self._comp_dict[key_var[0]+1, key_var[1]+1] = item_var
        else:
            raise ErrorGames("Туда нельзя стрелять.")
        
    def drow(self):
        """рисуем игровое поле."""
        print(f'\n           Поле компьютера                         Поле игрока')
        print(f"        {1}   {2}   {3}   {4}   {5}   {6}                   {1}   {2}   {3}   {4}   {5}   {6}")
        my_list = [' а(f)', ' б(,)', ' в(d)', ' г(u)', ' д(l)', ' е(t)']
        for i, lit in zip(range(1,7), my_list):
            print(lit, end="")
            for j in range(1,7):
                print(' |', self._comp_dict[(i, j)], end='')
            print('          ', lit, end='')
            for j in range(1,7):
                print(' |', self._plaer_dict[(i, j)], end='')
            print()
            
  
if __name__ == '__main__':
    drow = Drow()
    drow.drow()