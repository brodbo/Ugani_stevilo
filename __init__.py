n = 0
import random
stevilo = random.randint (1,10)
stej = 0
while n < 3:
    ugani = raw_input ("Vnesi stevilo od 1-10: ")
    if int(ugani) > 10:
        print "Stevilo %s je vecje od 10" % ugani
    elif int(stevilo) == int(ugani):
        stevilo = random.randint (1,10)
        n = n + 1
        print "Bravo, stevilo %s je pravo!" %ugani
        i = 3 - n
        if i == 0:
            print "Trikrat si uganil pravo stevilo "
        else:
            print "Ugani stevilo se %s x" % i
    else:
        print "Stevilo %s ni pravo." % ugani
    stej = stej + 1
print "Za to si potreboval %s poizkusov" %stej

