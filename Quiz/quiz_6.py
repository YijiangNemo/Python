# Creates 3 classes, Point, Line and Parallelogram.
# A point is determined by 2 coordinates (int or float).
# A line is determined by 2 distinct points.
# A parallelogram is determined by 4 distint lines,
# two of which having the same slope, the other two having the same slope too.
# The Parallelogram has a method, divides_into_two_parallelograms(), that determines
# where a line, provide as arguments, can split the object into two smaller parallelograms.
#
# Written by *** for COMP9021


from collections import defaultdict


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

class Line:
    def __init__(self,pt_1,pt_2):
        self.pt_1 = Point(pt_1.x,pt_1.y)
        self.pt_2 = Point(pt_2.x,pt_2.y)
        #print(self.pt_1)
        check = True
        if pt_1.x == pt_2.x and pt_1.y == pt_2.y:
            print('Cannot create line')
##            check = False
##            
##        if check == True:
##            self.k = float((pt_1.x - pt_2.x)/(pt_1.y - pt_2.y))
##            print(self.k)
##            self.b = pt_1.y - self.k*pt_1.x
##            print(self.b)
    # Replace pass above with your code


class Parallelogram:
    
    def __init__(self,line_1,line_2,line_3,line_4):
##        self.line_1 = Line(line_1.pt_1,line_1.pt_2)
##        self.line_2 = Line(line_2.pt_1,line_2.pt_2)
##        self.line_3 = Line(line_3.pt_1,line_3.pt_2)
##        self.line_4 = Line(line_4.pt_1,line_4.pt_2)
##        
        check = False
        if line_1.pt_1.x == line_1.pt_2.x:
            k1 = None
            b1 = line_1.pt_1.x
        else:
            k1 = (line_1.pt_1.y -line_1.pt_2.y)/(line_1.pt_1.x - line_1.pt_2.x)
            b1 = line_1.pt_1.y -k1*line_1.pt_1.x
        if line_2.pt_1.x == line_2.pt_2.x:
            k2 = None
            b2 = line_2.pt_1.x
        else:
            k2 = (line_2.pt_1.y -line_2.pt_2.y)/(line_2.pt_1.x - line_2.pt_2.x)
            b2 = line_2.pt_1.y -k2*line_2.pt_1.x
        if line_3.pt_1.x == line_3.pt_2.x:
            k3 = None
            b3 = line_3.pt_1.x
            
        else:
            k3 = (line_3.pt_1.y -line_3.pt_2.y)/(line_3.pt_1.x - line_3.pt_2.x)
            b3 = line_3.pt_1.y -k3*line_3.pt_1.x
        if line_4.pt_1.x == line_4.pt_2.x:
            k4 = None
            b4 = line_4.pt_1.x
        else:
            k4 = (line_4.pt_1.y -line_4.pt_2.y)/(line_4.pt_1.x - line_4.pt_2.x)
            b4 = line_4.pt_1.y -k4*line_4.pt_1.x
        self.l = []
        if (k1==k3 and k2==k4 and b1!=b3 and b2!=b4):
            check = True
            self.l.append([k1,max(b1,b3),min(b1,b3)])
            self.l.append([k2,max(b2,b4),min(b2,b4)])
  
        if(k1==k2 and k3==k4 and b1!=b2 and b3!=b4) :
            check = True
            self.l.append([k1,max(b1,b2),min(b1,b2)])
            self.l.append([k3,max(b3,b4),min(b3,b4)])
        if(k1==k4 and k2==k3 and b1!=b4 and b2!=b3):
            check = True
            self.l.append([k1,max(b1,b4),min(b1,b4)])
            self.l.append([k2,max(b2,b3),min(b2,b3)])
        if check == False:
            print('Cannot create parallelogram')
##        self.line_1 = (k1,b1)
##        self.line_2 = (k2,b2)
##        self.line_3 = (k3,b3)
##        self.line_4 = (k4,b4)
        

##        else:
##            l = []
            
            
            


    def divides_into_two_parallelograms(self, line):
        if self.l == []:
            return False
        self.line = Line(line.pt_1,line.pt_2)
        if line.pt_1.x == line.pt_2.x:
            k = None
            b = line.pt_1.x
        else:
            k = (line.pt_1.y -line.pt_2.y)/(line.pt_1.x - line.pt_2.x)
            b = line.pt_1.y -k*line.pt_1.x
        
        if k == self.l[0][0] and self.l[0][1]> b > self.l[0][2]:
            return True
        if k == self.l[1][0] and self.l[1][1]> b > self.l[1][2]:
            return True
        
        return False
        # Replace pass above with your code
        
    
