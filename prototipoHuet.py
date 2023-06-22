from urllib.request import urlopen
import urllib.request
import numpy as np
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils


# valores constantes
PontaIndicador = 8
PontaMedio = 12
PontaPolegar = 4
PontaAnelar = 16
Pontaminimo = 20
palma = 0

# variaveis
H = 0
L = 0
ligar_lamp = 1

# mostrar texto acima na tela
st = 'Bem-vindo'

#cap = cv2.VideoCapture()

# colocar IP do ESP32-CAM
esp32cam_ip = ""
url = f'http://{esp32cam_ip}/capture'

# colocar IP do ESP8266
esp8266_ip = ""

while True:
    img_resp = urlopen(url)
    imgnp = np.asarray(bytearray(img_resp.read()), dtype="uint8")
    img = cv2.imdecode(imgnp, -1)
    img = cv2.resize(img, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
    img = cv2.flip(img, 1)
    h, w, c = img.shape
    results = hands.process(img)

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:    
            mp_draw.draw_landmarks(img, hand_landmark, mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec((0, 0, 255), 2, 2), mp_draw.DrawingSpec((0, 255, 0), 4, 2))

            lm_list = []
            for id, lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)

            # decisão da letra H (Huet)
            if ((lm_list[PontaIndicador].x > lm_list[PontaMedio].x) and (lm_list[PontaIndicador-1].x 
                > lm_list[PontaMedio-1].x) and (lm_list[PontaIndicador-2].x > lm_list[PontaMedio-2].x) and (lm_list[PontaPolegar].y < 
                lm_list[PontaAnelar-2].y) and (lm_list[PontaAnelar-2].y <
                lm_list[PontaAnelar-1].y) and (lm_list[PontaAnelar-1].y < lm_list[PontaAnelar].y) and (lm_list[PontaPolegar].y < lm_list[PontaIndicador-3].y) and (lm_list[PontaPolegar].y < lm_list[PontaMedio-3].y) and (lm_list[Pontaminimo-2].y < 
                lm_list[Pontaminimo-1].y) and (lm_list[Pontaminimo-1].y < lm_list[Pontaminimo].y) and (lm_list[PontaIndicador].y < 
                lm_list[PontaIndicador-1].y < lm_list[PontaIndicador-2].y) and (lm_list[PontaMedio].y < lm_list[PontaMedio-1].y < 
                lm_list[PontaMedio-2].y) and H == 0) or ((lm_list[PontaIndicador].x < lm_list[PontaMedio].x) and (lm_list[PontaIndicador-1].x < 
                lm_list[PontaMedio-1].x) and (lm_list[PontaIndicador-2].x < lm_list[PontaMedio-2].x) and (lm_list[PontaPolegar].y < 
                lm_list[PontaAnelar-2].y) and (lm_list[PontaAnelar-2].y < 
                lm_list[PontaAnelar-1].y) and (lm_list[PontaAnelar-1].y < lm_list[PontaAnelar].y) and (lm_list[Pontaminimo-2].y < 
                lm_list[Pontaminimo-1].y) and (lm_list[Pontaminimo-1].y < lm_list[Pontaminimo].y) and (lm_list[PontaPolegar].y < lm_list[PontaIndicador-3].y) and (lm_list[PontaPolegar].y < lm_list[PontaMedio-3].y) and (lm_list[PontaIndicador].y < 
                lm_list[PontaIndicador-1].y < lm_list[PontaIndicador-2].y) and (lm_list[PontaMedio].y < lm_list[PontaMedio-1].y < 
                lm_list[PontaMedio-2].y) and H == 0): 
                    
                st = 'Huet'
                H = 1

            # decisão da letra L (lampada)
            if ((lm_list[PontaIndicador].y < lm_list[PontaIndicador-1].y < lm_list[PontaIndicador-2].y 
                < lm_list[PontaMedio].y ) and (lm_list[PontaPolegar].x < lm_list[PontaPolegar-1].x 
                < lm_list[PontaPolegar-2].x) and (lm_list[PontaMedio].y > lm_list[PontaMedio-1].y 
                > lm_list[PontaMedio-2].y) and (lm_list[PontaAnelar].y > lm_list[PontaAnelar-1].y 
                > lm_list[PontaAnelar-2].y) and (lm_list[Pontaminimo].y > lm_list[Pontaminimo-1].y 
                > lm_list[Pontaminimo-2].y) and (lm_list[PontaMedio].x < lm_list[PontaAnelar].x 
                < lm_list[Pontaminimo].x) and (lm_list[PontaMedio-1].x < lm_list[PontaAnelar-1].x 
                < lm_list[Pontaminimo-1].x) and (lm_list[PontaMedio-2].x < lm_list[PontaAnelar-2].x 
                < lm_list[Pontaminimo-2].x) and H == 1 and L == 0) or ((lm_list[PontaIndicador].y < lm_list[PontaIndicador-1].y < lm_list[PontaIndicador-2].y 
                < lm_list[PontaMedio].y ) and (lm_list[PontaPolegar].x > lm_list[PontaPolegar-1].x 
                > lm_list[PontaPolegar-2].x) and (lm_list[PontaMedio].y > lm_list[PontaMedio-1].y 
                > lm_list[PontaMedio-2].y) and (lm_list[PontaAnelar].y > lm_list[PontaAnelar-1].y 
                > lm_list[PontaAnelar-2].y) and (lm_list[Pontaminimo].y > lm_list[Pontaminimo-1].y 
                > lm_list[Pontaminimo-2].y) and (lm_list[PontaMedio].x > lm_list[PontaAnelar].x 
                > lm_list[Pontaminimo].x) and (lm_list[PontaMedio-1].x > lm_list[PontaAnelar-1].x 
                > lm_list[Pontaminimo-1].x) and (lm_list[PontaMedio-2].x > lm_list[PontaAnelar-2].x 
                > lm_list[Pontaminimo-2].x) and H == 1 and L == 0): 
                
                # ligar lâmpada
                if ligar_lamp == 1:
                    contents = urllib.request.urlopen("http://{esp8266_ip}/acender").read()
                    st = 'Lampada acesa'
                    ligar_lamp = 0
                    L = 0
                    H = 0

                # desligar lâmpada    
                elif ligar_lamp == 0:
                    contents = urllib.request.urlopen("http://{esp8266_ip}/apagar").read()
                    st = 'Lampada desligada'
                    ligar_lamp = 1
                    L = 0
                    H = 0

            cv2.putText(img, st, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("Prototipo Huet", img)

    # interromper ao pressionar "esc"
    if cv2.waitKey(5) & 0xFF == 27:
      break