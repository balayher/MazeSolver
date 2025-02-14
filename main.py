from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(100, 300)
    p4 = Point(500, 250)
    l1 = Line(p1, p2)
    l2 = Line(p1, p3)
    l3 = Line(p1, p4)
    l4 = Line(p2, p3)
    l5 = Line(p2, p4)
    l6 = Line(p3, p4)
    win.draw_line(l1)
    win.draw_line(l2, "red")
    win.draw_line(l3, "blue")
    win.draw_line(l4)
    win.draw_line(l5, "yellow")
    win.draw_line(l6, "orange")


    win.wait_for_close()



main()