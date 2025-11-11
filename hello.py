import pyautogui

def main():
    print("Hello from juegoauto!")
    # Capturar región específica (x, y, ancho, alto)
    screenshot = pyautogui.screenshot(region=(460, 300, 400, 600))



    # Ahora para sacar el color en un área específica
    siete = screenshot.getpixel((72, 108))
    ocho = screenshot.getpixel((177, 136))
    nueve = screenshot.getpixel((267, 129))

    cuatro = screenshot.getpixel((86, 184))
    cinco = screenshot.getpixel((172, 222))
    seis = screenshot.getpixel((269, 205))

    cero = screenshot.getpixel((70, 380))
    uno = screenshot.getpixel((78, 280))
    dos = screenshot.getpixel((171, 305))
    tres = screenshot.getpixel((230, 272))

    dividir = screenshot.getpixel((365, 102))
    multiplicar = screenshot.getpixel((372, 182))
    restar = screenshot.getpixel((369, 247))
    sumar = screenshot.getpixel((359, 334))

    igual = screenshot.getpixel((367, 390))
    
    botones = [siete, ocho, nueve,
               cuatro, cinco, seis,
               uno, dos, tres,
               cero, dividir, multiplicar,
               restar, sumar, igual]

    ACTIVE = (112, 112, 112)
    INACTIVE = (28, 28, 28)
    botones_activo = []
    for boton in botones:
        if boton == ACTIVE:
            print(f"Botón activo: {botones[botones.index(boton)]}")
            botones_activo.append(boton)
    
    print(f"Botones activos: {len(botones_activo)} de {len(botones)}")

    # color = screenshot.getpixel((100, 100))
    # print(f"Color en (100, 100): {color}")

    screenshot.save("captura.png")
    # print(dir(screenshot))

if __name__ == "__main__":
    main()
