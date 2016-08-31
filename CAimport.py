import csv
import glob

caDataOut = {}

caFiles = glob.glob('.\\in\\*USER_LOG_DATA*.csv')

for fn in caFiles:
    print("[ " + fn + " ]")
    caFileIn = open(fn, "r")
    caReaderIn = csv.reader(caFileIn)
    caData = list(caReaderIn)

    caDataOut[0] = caData[0]

    sn = 0.0
    sni = 0
    snc = 0
    flight = False
    for i in range(1,len(caData)):
        if sn < float(caData[i][0]) and len(caData[i]) == len(caData[0]):
            if caData[i][3]:
                sni = sni + 1
                sn = float(caData[i][0])
                caDataOut[sni] = caData[i]
                #print(i)
                if caData[i][18]:
                    if float(caData[i][18]) > 50:
                        flight = True
        else:
            if flight:
                snc = snc + 1
                print(flight, snc, i, len(caDataOut), caDataOut[1])
                print(flight, snc, i, caDataOut[1])
                print(flight, snc, i, caDataOut[sni])
                print()


                caFo = open(".\\out\\ca{}.csv".format(caDataOut[1][3].replace(":","-")), 'w', newline='')
                caFoWriter = csv.writer(caFo)
                for j in range(0,sni):
                    caFoWriter.writerow(caDataOut[j])
                caFo.close()

            flight = False
            sni = 0
            sn = 0.0
            caDataOut.clear()
            caDataOut[0] = caData[0]
    print("[ next file ]")
    print()

