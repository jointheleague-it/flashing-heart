def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global count
    count += 1
    basic.show_number(count)
input.on_button_pressed(Button.B, on_button_pressed_b)

count = 0
basic.show_string("Hello!")

def on_forever():
    basic.show_icon(IconNames.HAPPY)
    basic.show_icon(IconNames.SAD)
basic.forever(on_forever)
