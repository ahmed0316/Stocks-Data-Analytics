import urllib.request   #For Web Scraping

#CHANGE AS NEEDED. ONLY ONE CAN BE TRUE ##
#f = False                               ##
#t = True                                ##
#isEPS = f                               ##
#isPE = f                                ##
#isMarketCap = f                         ##
#isVolume = f                            ##
#isDividendYield = f                     ##
#isPrice = t                             ##


#ENSURE BOOLS OK
#truecount = 0   #number of true bools
#if (isEPS is True):
#    truecount = truecount + 1
#if (isPE is True):
#    truecount = truecount + 1
#if (isMarketCap is True):
#    truecount = truecount + 1
#if (isVolume is True):
#    truecount = truecount + 1
#if (isDividendYield is True):
#    truecount = truecount + 1
#if (isPrice is True):
#    truecount = truecount + 1

#if (truecount is not 1):    #If bools invalid, don't run program and send error message
#    print("ERROR: Invalid Criteria Booleans. Exactly 1 boolean must be set to true.")
#else:                       #If bools valid, run program

filename = "input.txt"  #File Name --> name of file to get tickers from (one ticker per line, '\n' delimited)

def findEPS(length): #find eps value on site
    i = 0
    while i < length:   
        if site[i] is't':
            if site[i+1] is 'r':
                if site[i+2] is 'a':
                    if site[i+3] is 'i':
                        if site[i+4] is 'l':
                            if site[i+5] is 'i':
                                if site[i+6] is 'n':
                                    if site[i+7] is 'g':
                                        if site[i+8] is 'E':
                                            if site[i+9] is 'p':
                                                if site[i+10] is 's':
                                                    if site[i+11] is '"':
                                                        if site[i+12] is ':':
                                                            if site[i+13] is '{':
                                                                if site[i+14] is '"':
                                                                    if site[i+15] is 'r':
                                                                        if site[i+16] is 'a':
                                                                            if site[i+17] is 'w':
                                                                                if site[i+18] is '"':
                                                                                    if site[i+19] is ':':
                                                                                        return i + 20  #start of eps value
                                                                                        break
        i = i + 1

def findPE(length): #find P/E value on site
    i = 0
    while i < length:   
        if site[i] is'"':
            if site[i+1] is 't':
                if site[i+2] is 'r':
                    if site[i+3] is 'a':
                        if site[i+4] is 'i':
                            if site[i+5] is 'l':
                                if site[i+6] is 'i':
                                    if site[i+7] is 'n':
                                        if site[i+8] is 'g':
                                            if site[i+9] is 'P':
                                                if site[i+10] is 'E':
                                                    if site[i+11] is '"':
                                                        if site[i+12] is ':':
                                                            if site[i+13] is '{':
                                                                if site[i+14] is '"':
                                                                    if site[i+15] is 'r':
                                                                        if site[i+16] is 'a':
                                                                            if site[i+17] is 'w':
                                                                                if site[i+18] is '"':
                                                                                    if site[i+19] is ':':
                                                                                        return i + 20  #start of P/E value
                                                                                        break
        i = i + 1

def findMarketCap(length): #find market cap value on site
    i = 0   #data-reactid="57">
    while i < length:   
        if site[i] is'd':
            if site[i+1] is 'a':
                if site[i+2] is 't':
                    if site[i+3] is 'a':
                        if site[i+4] is '-':
                            if site[i+5] is 'r':
                                if site[i+6] is 'e':
                                    if site[i+7] is 'a':
                                        if site[i+8] is 'c':
                                            if site[i+9] is 't':
                                                if site[i+10] is 'i':
                                                    if site[i+11] is 'd':
                                                        if site[i+12] is '=':
                                                            if site[i+13] is '"':
                                                                if site[i+14] is '5':
                                                                    if site[i+15] is '7':
                                                                        if site[i+16] is '"':
                                                                            if site[i+17] is '>':
                                                                                return i + 18  #start of market cap value
                                                                                break
        i = i + 1

def findVolume(length): #find volume value on site
    i = 0 
    while i < length:   
        if site[i] is '"':
            if site[i+1] is 'r':
                if site[i+2] is 'e':
                    if site[i+3] is 'g':
                        if site[i+4] is 'u':
                            if site[i+5] is'l':
                                if site[i+6] is 'a':
                                    if site[i+7] is 'r':
                                        if site[i+8] is 'M':
                                            if site[i+9] is 'a':
                                                if site[i+10] is 'r':
                                                    if site[i+11] is 'k':
                                                        if site[i+12] is 'e':
                                                            if site[i+13] is 't':
                                                                if site[i+14] is 'V':
                                                                    if site[i+15] is 'o':
                                                                        if site[i+16] is 'l':
                                                                            if site[i+17] is 'u':
                                                                                if site[i+18] is 'm':
                                                                                    if site[i+19] is 'e':
                                                                                        if site[i+20] is '"':
                                                                                            if site[i+21] is ':':
                                                                                                if site[i+22] is '{':
                                                                                                    if site[i+23] is '"':
                                                                                                        if site[i+24] is 'r':
                                                                                                            if site[i+25] is 'a':
                                                                                                                if site[i+26] is 'w':
                                                                                                                    if site[i+27] is '"':
                                                                                                                        if site[i+28] is ':':
                                                                                                                            return i + 29 #start of volume value
                                                                                                                            break
        i = i + 1

def findPrice(length): #find price value on site
    i = 0   #"larMarketPrice":{"raw":
    while i < length:
        if site[i] is 'l':
            if site[i+1] is 'a':
                if site[i+2] is 'r':
                    if site[i+3] is 'M':
                        if site[i+4] is 'a':
                            if site[i+5] is 'r':
                                if site[i+6] is 'k':
                                    if site[i+7] is 'e':
                                        if site[i+8] is 't':
                                            if site[i+9] is 'P':
                                                if site[i+10] is 'r':
                                                    if site[i+11] is 'i':
                                                        if site[i+12] is 'c':
                                                            if site[i+13] is 'e':
                                                                if site[i+14] is '"':
                                                                    if site[i+15] is ':':
                                                                        if site[i+16] is '{':
                                                                            if site[i+17] is '"':
                                                                                if site[i+18] is 'r':
                                                                                    if site[i+19] is 'a':
                                                                                        if site[i+20] is 'w':
                                                                                            if site[i+21] is '"':
                                                                                                if site[i+22] is ':':
                                                                                                    return i + 23
                                                                                                    break
        i = i + 1

def findDividendYield(length): #find dividend yield value on site
    i = 0   #"dividendYield":{"raw":
    while i < length:   
        if site[i] is'"':
            if site[i+1] is 'd':
                if site[i+2] is 'i':
                    if site[i+3] is 'v':
                        if site[i+4] is 'i':
                            if site[i+5] is 'd':
                                if site[i+6] is 'e':
                                    if site[i+7] is 'n':
                                        if site[i+8] is 'd':
                                            if site[i+9] is 'Y':
                                                if site[i+10] is 'i':
                                                    if site[i+11] is 'e':
                                                        if site[i+12] is 'l':
                                                            if site[i+13] is 'd':
                                                                if site[i+14] is '"':
                                                                    if site[i+15] is ':':
                                                                        if site[i+16] is '{':
                                                                            if site[i+17] is '"':
                                                                                if site[i+18] is 'r':
                                                                                    if site[i+19] is 'a':
                                                                                        if site[i+20] is 'w':
                                                                                            if site[i+21] is '"':
                                                                                                if site[i+22] is ':':
                                                                                                    return i + 23 #start of volume value
                                                                                                    break
        i = i + 1

#READ TEXT FILE
file = open(filename, "r")       #read file with tickers
filecontent = file.read()           #make readable

#CONVERT TEXT FILE TO LIST
tickers = []                           #list to convert to

suffix=".TO"
ticker=""
for char in filecontent:          #for each character
    if char is not None and char is not "" and char is not " " and char is not "\n" and char is not ",":
        if char is ".":     #replace "." with "-"
            char = "-"
        ticker = ticker + char
    else:
        tickers.append(ticker+suffix)
        ticker = ""
tickers.append(ticker+suffix)      #append last ticker (doesn't run else code)
#print(tickers)


#CONVERT TICKERS TO YAHOO FINANCE URLS
URLS = []                                       #list of URLs for the constituents
site = "https://www.finance.yahoo.com/quote/"   #yahoo finance start of link
for ticker in tickers:              #for each ticker
    URLS.append(site+ticker)
#print(URLS)

for j in range(6):      #For Each Value

    isEPS = False
    isPE = False
    isMarketCap = False
    isDividendYield = False
    isVolume = False
    isPrice = False

    if j is 0:          #1st loop
        isEPS = True
    if j is 1:          #2nd loop
        isPE = True
    if j is 2:          #etc
        isMarketCap = True
    if j is 3:
        isVolume = True
    if j is 4:
        isDividendYield = True
    if j is 5:
        isPrice = True

    print("Loading... (Please Wait). Output will be available in a text file located within the script's folder.")
    print()

    OUTPUT = ""

    #READ EACH URL AND EXTRACT VALUE
    for URL in URLS:          #for each URL, extract EPS value

        print(URL)
        #read site
        while(True):        #keep requesting until it is successful
            try:
                siteBytes = urllib.request.urlopen(URL).read()  #open url
                break
            except Exception:
                print("Retrying...")
        #except (httplib.IncompleteRead) as e:               #if open fails for whatever reason
         #   siteBytes = e.partial                           #then try again
          #  print("Retrying Request...")
        site = siteBytes.decode("utf8")                     #decode page
#        urlReader.close()

        length = len(site)      #length of html page

        if isEPS is True:
            x = findEPS(length)         #find start of EPS value
        elif isPE is True:
            x = findPE(length)          #find start of P/E value
        elif isMarketCap is True:
            x = findMarketCap(length)   #find start of market cap value
        elif isVolume is True:
            x = findVolume(length)
        elif isDividendYield is True:
            x = findDividendYield(length)
        elif isPrice is True:
            x = findPrice(length)

        if x is not None:
            val = ""
            val = val + site[x]         #write first value
            while site[x+1] is not '.' and ( site[x+1].isdigit() or site[x+1] is '-'):   #write values up to the decimal point
                x = x + 1
                val = val + site[x]
            val = val + "."         
            x = x + 1
            #Write Up To 5 Decimal Places
            for i in range(1,6):    #for i = 1 to i = 6
                if site[x+i].isdigit() is True or site[x+i] is 'B' or  site[x+i] is 'M': #if val is numeric or is a 'B' or 'M'
                    val = val + site[x+i]                                         #save it
                else:
                    if i is 1:      
                        val = val + "0"       #.0 instead of . if no decimal places needed
                    break

        else:
            val = "N/A"

        OUTPUT = OUTPUT + val + '\n'

        if isEPS is True:
            print("EPS: "+val)
        elif isPE is True:
            print("P/E: "+val)
        elif isMarketCap is True:
            print("Market Cap: "+val)
        elif isVolume is True:
            print("Volume: "+val)
        elif isDividendYield is True:
            print("Dividend Yield: "+val)
        elif isPrice is True:
            print("Price: "+val)
        print()

    #OUTPUT TO TEXT FILE
    if isEPS is True:
        newFile = open('EPS.txt', 'w+')
    elif isPE is True:
        newFile = open('PE.txt', 'w+')
    elif isMarketCap is True:
        newFile = open('Market Cap.txt', 'w+')
    elif isVolume is True:
        newFile = open('Volume.txt', 'w+')
    elif isDividendYield is True:
        newFile = open('Dividend Yield.txt', 'w+')
    elif isPrice is True:
        newFile = open('Price.txt', 'w+')

    newFile.write(OUTPUT)
    newFile.close()
print("Complete.")
