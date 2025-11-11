import pyautogui
import time

def get_coordinates():
    print("Por favor, selecciona un área en la pantalla.")
    print("Tienes 5 segundos para posicionar el cursor en la esquina superior izquierda de la región.")
    time.sleep(5)
    
    x1, y1 = pyautogui.position()  # Esquina superior izquierda
    print(f"Coordenadas de la esquina superior izquierda: ({x1}, {y1})")
    
    print("Ahora, mueve el cursor a la esquina inferior derecha de la región.")
    time.sleep(5)
    
    x2, y2 = pyautogui.position()  # Esquina inferior derecha
    print(f"Coordenadas de la esquina inferior derecha: ({x2}, {y2})")
    
    width = x2 - x1
    height = y2 - y1
    region = (x1, y1, width, height)
    
    print(f"Región capturada: {region}")
    return region

if __name__ == "__main__":
    get_coordinates()