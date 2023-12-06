class GamePlay:
    """Класс игровой логики."""
    

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
        self._plaer_dict[key_var] = item_var
        
    #меняем значение на поле компьютера    
    def comp_dict_set(self, key_var:tuple, item_var:str):
        self._comp_dict[key_var] = item_var
        
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