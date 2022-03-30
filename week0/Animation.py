import time

# terminal print commands
ANSI_CLEAR_SCREEN =  lambda: print('\n' * 150)
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u""
SHIP_COLOR = u"\u001b[34m"
RESET_COLOR = u"\u001b[34m"

def AP(position):
    print('\n' * 100)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "  __^__")
    print(sp + " /|_||_\`.__")
    print(sp + "=`-(_)--(_)-'")
    print(RESET_COLOR)

def animation():
    
    start = 0  
    distance = 52 
    step = 2  
  
    for position in range(start, distance, step):
        AP(position)  
        time.sleep(.1)
# if __name__ == "__main__":
#   AP()
#   animation()

