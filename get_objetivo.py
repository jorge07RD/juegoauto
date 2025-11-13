import pyautogui
from PIL import Image
import easyocr
import re

def get_objetivo():
    # Capturar región específica
    screenshot = pyautogui.screenshot(region=(1060, 400, 400, 300))
    screenshot.save("objetivo_debug.png")
    
    # Inicializar EasyOCR (solo la primera vez es lento, luego es rápido)
    reader = easyocr.Reader(['en'], gpu=False)
    
    # Leer texto de la imagen - INCLUYE EL SIGNO NEGATIVO
    resultado = reader.readtext('objetivo_debug.png', allowlist='0123456789-')
    
    print(f"Resultados de EasyOCR: {resultado}")
    
    # Extraer números (incluyendo negativos)
    for deteccion in resultado:
        texto = deteccion[1]  # El texto detectado
        # Buscar números positivos o negativos
        numeros = re.findall(r'-?\d+', texto)
        if numeros:
            objetivo = int(numeros[0])
            print(f"✓ Objetivo detectado: {objetivo}")
            return objetivo
    
    print("❌ No se detectó ningún número")
    return None

if __name__ == "__main__":
    print("Inicializando EasyOCR (esto puede tardar un poco la primera vez)...")
    objetivo = get_objetivo()
    print(f"\nResultado final: {objetivo}")