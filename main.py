import time,os
os.system("clear")
a = int(input("1] Dec to Binary \n2] Binary to Dec\n" + "Please enter the choice: "))
if a == 1:
    while True:
        decimal = int(input("Please enter the decimal number here: "))

        def converter(n):
            return bin(n).replace("0b","")

        if __name__ == '__main__':
            print("#########################################")
            print("The convertion is done!" + "\n" + "Binary: " + str(converter(decimal)))
            number = str(converter(decimal))
            print("#########################################")
            """
            if(len(number) <= 10):
                time.sleep(11)
            else:
                time.sleep(20)
            os.system('clear')
            """
if a == 2:
    while True:
        bi = input("Please enter the binary number here: ")
        deci = 0
        for digit in bi:
            deci = deci*2 + int(digit)
        print("#########################################")
        print("The convertion is done!" + "\n" + "Binary: ", str(deci))
        #number = str(convertion(bi))
        print("#########################################")
            