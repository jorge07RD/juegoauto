# filepath: coordinate-picker/src/main.py
import pyautogui
import time

def get_coordinates():
    print("Por favor, selecciona el área de la pantalla que deseas capturar.")
    print("Tienes 5 segundos para posicionar el cursor en la esquina superior izquierda de la región.")
    time.sleep(5)
    x1, y1 = pyautogui.position()
    print("Posiciona el cursor en la esquina inferior derecha de la región.")
    time.sleep(5)
    x2, y2 = pyautogui.position()
    
    width = x2 - x1
    height = y2 - y1
    return (x1, y1, width, height)

def main():
    print("Bienvenido a la aplicación de selección de coordenadas.")
    region = get_coordinates()
    print(f"Coordenadas seleccionadas: {region}")

if __name__ == "__main__":
    main()