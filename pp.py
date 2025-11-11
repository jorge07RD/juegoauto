import pyautogui
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

def explorar_imagen(ruta_imagen=None ,region_screenshot=None):
    """
    Abre una imagen y muestra coordenadas al hacer clic
    Si no se pasa ruta, captura la pantalla
    """
    img = None
    if ruta_imagen:
        img = Image.open(ruta_imagen)

    if region_screenshot:
        img = pyautogui.screenshot(region=region_screenshot)  
    if not ruta_imagen and not region_screenshot:
        img = pyautogui.screenshot()      
    
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.imshow(img)
    ax.set_title("Haz clic en la imagen para ver coordenadas y color\nPresiona 'q' para salir")
    
    def onclick(event):
        if event.xdata is not None and event.ydata is not None:
            x, y = int(event.xdata), int(event.ydata)
            try:
                color = img.getpixel((x, y))
                hex_color = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
                print(f"Posición: ({x}, {y}) | RGB: {color} | HEX: {hex_color}")
            except:
                print(f"Posición fuera de rango: ({x}, {y})")
    
    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()

if __name__ == "__main__":
    # Opción 1: Explorar una captura guardada
    # explorar_imagen("captura.png")
    
    # Opción 2: Capturar y explorar
    explorar_imagen(region_screenshot=(460, 300, 400, 600))