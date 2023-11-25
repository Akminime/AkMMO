import pyglet

window = pyglet.window.Window()
background = pyglet.image.load("resources/images/background1.png")
backgroundsprite = pyglet.sprite.Sprite(background)
backgroundsprite.scale = 3

@window.event
def on_draw():
    window.clear()
    backgroundsprite.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == 119:
        print("Key W Pressed, Moving Up")
        backgroundsprite.position = (
            backgroundsprite.x, backgroundsprite.y - 10, 0
        )
        print(f"New Background Sprite POS: {backgroundsprite.x}, {backgroundsprite.y}")
    
    if symbol == 97:
        print("Key A Pressed, Moving Left")
        backgroundsprite.position = (
            backgroundsprite.x + 10, backgroundsprite.y, 0
        )
        print(f"New Background Sprite POS: {backgroundsprite.x}, {backgroundsprite.y}")

    if symbol == 115:
        print("Key S Pressed, Moving Down")
        backgroundsprite.position = (
            backgroundsprite.x, backgroundsprite.y + 10, 0
        )
        print(f"New Background Sprite POS: {backgroundsprite.x}, {backgroundsprite.y}")

    if symbol == 100:
        print("Key D Pressed, Moving Right")
        backgroundsprite.position = (
            backgroundsprite.x - 10, backgroundsprite.y, 0
        )
        print(f"New Background Sprite POS: {backgroundsprite.x}, {backgroundsprite.y}")


@window.event
def on_mouse_motion(x, y, dx, dy):
    print(f"Mouse Moved to ({x}, {y})")

pyglet.app.run()