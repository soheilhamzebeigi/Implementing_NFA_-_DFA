from graphics import *
import random
from math import floor

from Models import *


class DrawGraph:
    def __init__(self, stateList, transitionList, winTitle='Draw Graph'):
        super().__init__()
        self.state_list = stateList
        self.transition_list = transitionList
        self.cellWidth = 100
        self.cellHeight = 400
        self.circleRadius = 30
        self.finalCircleRadius = 35
        self.win = None
        self.winTitle = winTitle
        self.takenPasses = []

    def _setNewWindow(self):
        self.win = GraphWin(self.winTitle, width=self.cellWidth *
                            len(self.state_list), height=self.cellHeight)

    def _DrawState(self, state_name, isFinal, state_index):
        # for being final
        if isFinal:
            p3 = Point(state_index*self.cellWidth -
                       self.cellWidth/2,  self.cellHeight/2)
            cir = Circle(p3, self.circleRadius+5)
            cir.draw(self.win)
        # its own circle
        p3 = Point(state_index*self.cellWidth -
                   self.cellWidth/2, self.cellHeight/2)
        cir = Circle(p3, self.circleRadius)
        cir.setFill('white')
        cir.draw(self.win)
        # for naming state
        message = Text(Point(state_index*self.cellWidth -
                             self.cellWidth/2, self.cellHeight/2), state_name)
        message.draw(self.win)

    def _DrawStartTransition(self):
        l1 = Line(Point(
            0, self.cellHeight/2),
            Point(
            self.cellWidth/2-self.finalCircleRadius, self.cellHeight/2))
        l1.setArrow('last')
        l1.draw(self.win)

    def _DrawTransition(self, transition: Transition, height, isTop):
        s_index = self.state_list.index(transition.starting_state)
        e_index = self.state_list.index(transition.ending_state)

        if s_index == e_index:
            cir = Circle(Point(s_index * self.cellWidth +
                               self.cellWidth/2, self.cellHeight/2 - self.finalCircleRadius - 20), 20)
            text = Text(Point(s_index * self.cellWidth +
                              self.cellWidth/2, self.cellHeight/2 - self.finalCircleRadius - 20), transition.alphabet)
            cir.draw(self.win)
            text.draw(self.win)
            p0 = Point(s_index * self.cellWidth +
                       self.cellWidth/2, self.cellHeight/2 - self.finalCircleRadius)
            p1 = Point(s_index * self.cellWidth +
                       self.cellWidth/2 + 1, self.cellHeight/2 - self.finalCircleRadius)
            l1 = Line(p0, p1)
            l1.setArrow('last')
            l1.draw(self.win)
            return
        elif s_index+1 == e_index:
            # if e_index > s_index:
            p3 = Point(s_index * self.cellWidth +
                       self.cellWidth/2 + self.finalCircleRadius, self.cellHeight/2)
            p4 = Point(e_index * self.cellWidth+self.cellWidth /
                       2 - self.finalCircleRadius, self.cellHeight/2)
            # else:
            #     p3 = Point(s_index * self.cellWidth +
            #                self.cellWidth/2 - self.finalCircleRadius, self.cellHeight/2)
            #     p4 = Point(e_index * self.cellWidth+self.cellWidth /
            #                2 + self.finalCircleRadius, self.cellHeight/2)
            p1 = p3
            p2 = p4
            text = Text(Point((s_index * self.cellWidth + e_index * self.cellWidth +
                               self.cellWidth)/2, self.cellHeight/2-10), transition.alphabet)
        elif isTop:
            p1 = Point(s_index * self.cellWidth +
                       self.cellWidth/2, self.cellHeight/2 - self.finalCircleRadius)
            p2 = Point(s_index * self.cellWidth+self.cellWidth /
                       2, self.cellHeight/2 - height - self.finalCircleRadius)
            p3 = Point(e_index * self.cellWidth+self.cellWidth /
                       2, self.cellHeight/2 - height - self.finalCircleRadius)
            p4 = Point(e_index * self.cellWidth +
                       self.cellWidth/2, self.cellHeight/2 - self.finalCircleRadius)
            text = Text(Point((s_index * self.cellWidth + e_index * self.cellWidth +
                               self.cellWidth)/2, self.cellHeight/2 - height - self.finalCircleRadius-10), transition.alphabet)
            isTop = not isTop
        else:
            p1 = Point(s_index * self.cellWidth +
                       self.cellWidth/2, self.cellHeight/2 + self.finalCircleRadius)
            p2 = Point(s_index * self.cellWidth+self.cellWidth /
                       2, self.cellHeight/2 + height + self.finalCircleRadius)
            p3 = Point(e_index * self.cellWidth+self.cellWidth /
                       2, self.cellHeight/2 + height + self.finalCircleRadius)
            p4 = Point(e_index * self.cellWidth +
                       self.cellWidth/2, self.cellHeight/2 + self.finalCircleRadius)
            text = Text(Point((s_index * self.cellWidth + e_index * self.cellWidth +
                               self.cellWidth)/2, self.cellHeight/2 + height + self.finalCircleRadius+10), transition.alphabet)
            isTop = not isTop
        color = self.genRandomColor()
        line1 = Line(p1, p2)
        line2 = Line(p2, p3)
        line3 = Line(p3, p4)
        line1.setFill(color)
        line2.setFill(color)
        line3.setFill(color)
        line1.setWidth(2)
        line2.setWidth(2)
        line3.setWidth(2)
        line1.draw(self.win)
        line2.draw(self.win)
        line3.setArrow("last")
        line3.draw(self.win)
        text.draw(self.win)
        return isTop

    def genRandomColor(self):
        r = floor(random.random()*255)
        g = floor(random.random()*100)
        b = floor(random.random()*100)
        return color_rgb(r, g, b)

    def DrawWin(self):
        self._setNewWindow()
        # draw states
        for index, item in enumerate(self.state_list):
            self._DrawState(item.state_name, item.is_final, index+1)

        # draw transition
        isTop = True
        height = 10
        self._DrawStartTransition()

        for index, item in enumerate(self.transition_list):
            if isTop:
                height = 0
            else:
                height = 10
            isTop = self._DrawTransition(
                item, height=index*10+height, isTop=isTop)
