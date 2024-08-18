import pynput.mouse as mouse
import pynput.keyboard as keyboard


def onClick(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
            print(f'x={x} and y={y}')

def onPress(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
            print(f'x={x} and y={y}')

if __name__ == "__main__":
    with mouse.Listener(on_click=onClick) as mouseListener:
        mouseListener.join()
