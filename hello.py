import pyautogui
import keyboard
# from pywinauto import Desktop
# Configuración de PyAutoGUI

# app = Desktop(backend="uia").window(title="Calculadora")
pyautogui.FAILSAFE = True  # Mover mouse a esquina superior izquierda para abortar
pyautogui.PAUSE = 0.1  # Pausa entre cada acción

from ppa import resolver_objetivo
from get_objetivo import get_objetivo
import time

cero_location = (70, 380)  # Coordenadas del botón '0'
uno_location = (78, 280)    # Coordenadas del botón '1'
dos_location = (171, 305)   # Coordenadas del botón '2'
tres_location = (230, 272)  # Coordenadas del botón '3'
cuatro_location = (86, 184)  # Coordenadas del botón '4'
cinco_location = (172, 222)  # Coordenadas del botón '5'
seis_location = (269, 205)   # Coordenadas del botón '6'
siete_location = (72, 108)   # Coordenadas del botón '7'
ocho_location = (177, 136)   # Coordenadas del botón '8'
nueve_location = (267, 129)  # Coordenadas del botón '9'

dividir_location = (365, 102)
multiplicar_location = (372, 182)
restar_location = (369, 247)
sumar_location = (359, 334)
igual_location = (367, 390)

# Mapeo de símbolos a coordenadas (fuera de la función)
locations_map = {
    '0': cero_location,
    '1': uno_location,
    '2': dos_location,
    '3': tres_location,
    '4': cuatro_location,
    '5': cinco_location,
    '6': seis_location,
    '7': siete_location,
    '8': ocho_location,
    '9': nueve_location,
    '/': dividir_location,
    '*': multiplicar_location,
    '-': restar_location,
    '+': sumar_location,
    '=': igual_location
}

def hacer_clicks(expresion, locations_map):
    """
    Realiza clicks en orden basado en la expresión.
    
    Args:
        expresion: tupla/lista como ('1', '+', '1')
        locations_map: diccionario que mapea símbolos a coordenadas
    """
    print(f"\n🖱️ Iniciando secuencia de clicks para: {expresion}")
    
    for i, simbolo in enumerate(expresion):
        if simbolo in locations_map:
            x, y = locations_map[simbolo]
            click_x = 460 + x
            click_y = 300 + y
            
            print(f"\n[{i+1}/{len(expresion)}] Símbolo: '{simbolo}'")
            print(f"  📍 Moviendo a: ({click_x}, {click_y})")
            
            # Mover el mouse primero
            pyautogui.moveTo(click_x, click_y, duration=0.2)
            time.sleep(0.2)
            
            # Verificar posición
            pos = pyautogui.position()
            print(f"  ✓ Mouse en: {pos}")
            
            # Hacer click con mouseDown y mouseUp explícito
            pyautogui.mouseDown(button='left')
            time.sleep(0.05)
            pyautogui.mouseUp(button='left')
            
            print(f"  ✅ Click realizado")
            time.sleep(0.5)
        else:
            print(f"⚠️ Símbolo '{simbolo}' no encontrado en el mapa")

def get_botones(objetivo=int):
    print("Hello from juegoauto!")
    # Capturar región específica (x, y, ancho, alto)
    screenshot = pyautogui.screenshot(region=(460, 300, 400, 600))

    # Ahora para sacar el color en un área específica
    cero = screenshot.getpixel(cero_location)
    uno = screenshot.getpixel(uno_location)
    dos = screenshot.getpixel(dos_location)
    tres = screenshot.getpixel(tres_location)
    cuatro = screenshot.getpixel(cuatro_location)
    cinco = screenshot.getpixel(cinco_location)
    seis = screenshot.getpixel(seis_location)
    siete = screenshot.getpixel(siete_location)
    ocho = screenshot.getpixel(ocho_location)
    nueve = screenshot.getpixel(nueve_location)

    dividir = screenshot.getpixel(dividir_location)
    multiplicar = screenshot.getpixel(multiplicar_location)
    restar = screenshot.getpixel(restar_location)
    sumar = screenshot.getpixel(sumar_location)
    igual = screenshot.getpixel(igual_location)

    ACTIVE = (112, 112, 112)
    INACTIVE = (28, 28, 28)

    # Cambiar: usar índices o tuplas (color, símbolo)
    numeros = [cero, uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve]
    numeros_con_simbolos = [
        (cero, '0'), (uno, '1'), (dos, '2'), (tres, '3'), 
        (cuatro, '4'), (cinco, '5'), (seis, '6'), 
        (siete, '7'), (ocho, '8'), (nueve, '9')
    ]
    numeros_activo = [simbolo for color, simbolo in numeros_con_simbolos if color == ACTIVE]
    
    operaciones_con_simbolos = [
        (dividir, '/'), (multiplicar, '*'), 
        (restar, '-'), (sumar, '+')
    ]
    operaciones_activo = [simbolo for color, simbolo in operaciones_con_simbolos if color == ACTIVE]
    
    # Debug: print actual colors to see what's being detected
    print(f"Debug - dividir: {dividir}, multiplicar: {multiplicar}, restar: {restar}, sumar: {sumar}")
    print(f"Debug - ACTIVE color: {ACTIVE}")
    print(f"Operaciones activas: {operaciones_activo} ({len(operaciones_activo)} de 4)")
    print(f"Números activos: {numeros_activo} ({len(numeros_activo)} de 10)")

    screenshot.save("captura.png")
    
    respusta = resolver_objetivo(objetivo, numeros_activo, operaciones_activo, verbose=True)
    print("Resultado final:", respusta)
    
    # Si se encontró una respuesta, hacer clicks
    if respusta:
        print("Haciendo clicks en la calculadora...")
        time.sleep(2)  # Pausa antes de empezar a hacer clicks
        # Extraer la expresión del diccionario
        expresion = respusta['expresion']
        hacer_clicks(expresion, locations_map)

def play_game():
    print("Iniciando juego automático...")
    while True:
        objetivo = get_objetivo()
        if objetivo is not None:
            get_botones(objetivo)
            time.sleep(1)  # Esperar antes de la siguiente iteración
   
            x, y = igual_location
            click_x = 460 + x
            click_y = 300 + y
            pyautogui.moveTo(click_x, click_y, duration=0.2)
            pyautogui.mouseDown(button='left')
            time.sleep(0.05)
            pyautogui.mouseUp(button='left')
        else:
            print("No se pudo obtener el objetivo. Reintentando en 5 segundos...")
        time.sleep(5)  # Esperar antes de la siguiente iteración
        #si prexiono 'q' salir
        if keyboard.is_pressed('q'):
            print("Saliendo del juego automático...")
            break

if __name__ == "__main__":
    # get_botones(7)    
    # get_botones(get_objetivo())  
    play_game()  
