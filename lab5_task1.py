import math
class point():
    def __init__(self):
        self.x1=int(input('please input a int :'))
        self.x2=int(input('please enter a nuber'))
        self.y1 = int(input('please enter a nuber'))
        self.y2 = int(input('please enter a nuber'))
    def distance_between_points(self):
        dx = self.x1-self.x2
        dy = self.y1-self.y2
        dis = math.sqrt(dx**2+dy**2)
        return dis

point().distance_between_points()

