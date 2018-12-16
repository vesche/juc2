"""juc2.art.symbols"""

arrow_down = r'''
     .
       .
   . ;.
    .;
     ;;.
   ;.;;
   ;;;;.
   ;;;;;
   ;;;;;
   ;;;;;
   ;;;;;
   ;;;;;
 ..;;;;;..
  ':::::'
    ':`
'''

arrow_left = r'''
    .
  .;;............ ..
.;;;;::::::::::::..
 ':;;:::::::::::: . .
   ':
'''

arrow_right = r'''
                .
 .. ............;;.
  ..::::::::::::;;;;.
. . ::::::::::::;;:'
                :'
'''

arrow_up = r'''
     .
   .:;:.
 .:;;;;;:.
   ;;;;;
   ;;;;;
   ;;;;;
   ;;;;;
   ;:;;;
   : ;;;
     ;:;
   . :.;
     . :
   .   .

      .
'''


class _Meta:
    def __init__(self, x=0, y=0, transparent=False):
        self.x = x
        self.y = y
        self.transparent = transparent
    
    def display(self):
        return self.figure


class Symbols:

    class ArrowDown(_Meta):
        author = 'unknown'
        figure = arrow_down

    class ArrowLeft(_Meta):
        author = 'unknown'
        figure = arrow_left

    class ArrowRight(_Meta):
        author = 'unknown'
        figure = arrow_right
    
    class ArrowUp(_Meta):
        author = 'unknown'
        figure = arrow_up
