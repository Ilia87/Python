import graphics as gr


def build_house(windows, upper_left_corner, width):
    """function which build house"""
    height = calculate_height (width)


windows = gr.GraphWin("Russian game", 300, 300)
build_house(windows, gr.Point(100, 100), 100)

print("excellent!")
