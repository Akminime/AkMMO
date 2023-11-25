import pyglet

window = pyglet.window.Window()
background = pyglet.image.load("resources/images/background1.png")
backgroundsprite = pyglet.sprite.Sprite(background)
backgroundsprite.scale = 3
playerimage = pyglet.image.load("resources/images/bard1.png")
player = pyglet.sprite.Sprite(playerimage)
player.position = (500, 250, 0)

@window.event
def on_draw():
    window.clear()
    backgroundsprite.draw()
    player.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == 119:
        print("Key W Pressed, Moving Up")
        backgroundsprite.position = (
            backgroundsprite.x, backgroundsprite.y - 10, 0
        )
        print(f"New Background Sprite POS: {backgroundsprite.x}, {backgroundsprite.y}")
    
    elif symbol == 97:
        print("Key A Pressed, Moving Left")
        backgroundsprite.position = (
            backgroundsprite.x + 10, backgroundsprite.y, 0
        )
        print(f"New Background Sprite POS: {backgroundsprite.x}, {backgroundsprite.y}")

    elif symbol == 115:
        print("Key S Pressed, Moving Down")
        backgroundsprite.position = (
            backgroundsprite.x, backgroundsprite.y + 10, 0
        )
        print(f"New Background Sprite POS: {backgroundsprite.x}, {backgroundsprite.y}")

    elif symbol == 100:
        print("Key D Pressed, Moving Right")
        backgroundsprite.position = (
            backgroundsprite.x - 10, backgroundsprite.y, 0
        )
        print(f"New Background Sprite POS: {backgroundsprite.x}, {backgroundsprite.y}")



    else:
        print(f"Key {symbol} pressed but it has no mapped function")


@window.event
def on_mouse_motion(x, y, dx, dy):
    print(f"Mouse Moved to ({x}, {y})")

pyglet.app.run()