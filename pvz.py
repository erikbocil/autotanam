import os, pyautogui, time
time.sleep(3)

lokasi = [[605, 511], [387, 359], [705, 500], [702, 434], [754, 429],
          [652, 575], [490, 290], [487, 571], [547, 502]]
seedloc = [[453, 99], [507, 107], [561, 105], [613, 106], [664, 108],
           [714, 108], [767, 108], [819, 108], [868, 105]]
baris1 = [[420, 189], [500, 189], [580, 189], [660, 189], [750, 189],
          [825, 189], [900, 189], [988, 189], [1071, 189]]
baris2 = [[420, 289], [500, 289], [580, 289], [660, 289], [750, 289],
          [825, 289], [900, 289], [988, 289], [1071, 289]]
baris3 = [[420, 389], [500, 389], [580, 389], [660, 389], [750, 389],
          [825, 389], [900, 389], [988, 389], [1071, 389]]
baris4 = [[420, 479], [500, 479], [580, 479], [660, 479], [750, 479],
          [825, 479], [900, 479], [988, 479], [1071, 479]]
baris5 = [[420, 555], [500, 555], [580, 555], [660, 555], [750, 555],
          [825, 555], [900, 555], [988, 555], [1071, 555]]
baris6 = [[420, 625], [500, 625], [580, 625], [660, 625], [750, 625],
          [825, 625], [900, 625], [988, 625], [1071, 625]]


def tanamjamur(baris):
    print('Tanam Jamur')
    for i in range(7, 4, -1):
        #jamur
        pyautogui.click(x=seedloc[6][0], y=seedloc[6][1])
        pyautogui.click(x=baris[i][0], y=baris[i][1])
        #upgrade jamur
        pyautogui.click(x=seedloc[7][0], y=seedloc[7][1])
        pyautogui.click(x=baris[i][0], y=baris[i][1])
        #biji kopi
        pyautogui.click(x=seedloc[8][0], y=seedloc[8][1])
        pyautogui.click(x=baris[i][0], y=baris[i][1])
    print('tanam Jamur Selesai')


def tanambawang(baris):
    print('Tanam bawang')
    pyautogui.click(x=seedloc[0][0], y=seedloc[0][1])
    pyautogui.click(x=baris[8][0], y=baris[8][1])
    print('tanam bawang Selesai')


def tanammagnet(baris):
    print('Tanam Magnet')
    pyautogui.click(x=seedloc[4][0], y=seedloc[4][1])
    pyautogui.click(x=baris[4][0], y=baris[4][1])
    pyautogui.click(x=seedloc[5][0], y=seedloc[5][1])
    pyautogui.click(x=baris[4][0], y=baris[4][1])
    print('tanam Magnet Selesai')


def tanamlilypad(baris):
    print('Tanam Lilypad')
    for i in range(6):
        pyautogui.click(x=seedloc[1][0], y=seedloc[1][1])
        pyautogui.click(x=baris[i][0], y=baris[i][1])
    print('tanam Lilypad Selesai')


def tanamlabu():
    print('Tanam Labu')
    yay = 189
    for i in range(6):
        if i == 1 or i == 4:
            pyautogui.click(x=seedloc[3][0], y=seedloc[3][1])
            pyautogui.click(x=988, y=yay)
        else:
            pyautogui.click(x=seedloc[3][0], y=seedloc[3][1])
            pyautogui.click(x=824, y=yay)
        yay += 80
    print('tanam Labu Selesai')

def tanambunga(baris):
    print('Tanam Bunga')
    for i in range(6):
        pyautogui.click(x=seedloc[2][0], y=seedloc[2][1])
        pyautogui.click(x=baris[i][0], y=baris[i][1])
    print('tanam Bunga Selesai')


def tanambunga2(baris):
    print('Tanam Bunga')
    for i in range(4):
        pyautogui.click(x=seedloc[2][0], y=seedloc[2][1])
        pyautogui.click(x=baris[i][0], y=baris[i][1])
    print('tanam Bunga Selesai')

def pilihbiji(lokasibiji):
    print('Pilih Biji')
    for i in range(9):
        pyautogui.click(x=lokasi[i][0], y=lokasi[i][1])
        time.sleep(0.5)
    print('Pilih Biji Selesai')








pilihbiji(lokasi)
pyautogui.click(x=573, y=625, clicks=2)
time.sleep(5)
tanamlilypad(baris3)
time.sleep(1)
tanamlilypad(baris4)
time.sleep(1)
tanambawang(baris2)
time.sleep(1)
tanambawang(baris5)
time.sleep(1)
tanamjamur(baris2)
time.sleep(1)
tanamjamur(baris5)
time.sleep(1)
tanamlabu()
time.sleep(1)
tanammagnet(baris2)
time.sleep(1)
tanammagnet(baris5)
time.sleep(1)
tanambunga(baris1)
time.sleep(1)
tanambunga2(baris2)
time.sleep(1)
tanambunga(baris3)
time.sleep(1)
tanambunga(baris4)
time.sleep(1)
tanambunga2(baris5)
time.sleep(1)
tanambunga(baris6)
time.sleep(1)
