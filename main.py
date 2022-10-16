import classNode as cn
from generateMaze import generateMaze

example = 0

if __name__ == 'main':
    maze = generateMaze((21, 21)) #Odd numbers only
    
    instance = cn.Node((1,1))
    print(instance.coordinates)
