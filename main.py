basic.show_string("Hello")
basic.show_number(80)
basic.pause(2000)
basic.show_arrow(ArrowNames.SOUTH)
basic.pause(1000)
basic.show_icon(IconNames.YES)

def on_forever():
    pass
basic.forever(on_forever)
