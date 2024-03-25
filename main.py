from display import Window, Line, Point

def main():
    win = Window(800, 600)
    
    point_one = Point(0, 0)
    point_two = Point(50, 50)
    
    win.draw_line(Line(point_one, point_two), "blue")
    
    win.wait_for_close()
    
main()

    