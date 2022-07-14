import random

print("PRESS CTRL + C TO TERMINATE THE APP")

seed = "fffddfd"
r = random.Random(seed)
# inititating the random module 

numberList = []
for i in range(100):
    numberList.append(i+1)
# making a list containing integers from 1 to 100

iterations = 0 #number of iterations
totalOutBreaks = 0 #number of iterations in which the prisoners breaks out

try:
    while True:
        iterations+=1
        # incrementing number of iterations 

        shuffledList = numberList
        r.shuffle(shuffledList)
        #randomly shuffling the numbers 

        success = False
        # checking for if the iteration is successfull 

        for prisoner in range(100):
            currentIndex = prisoner
            # index for checking the box 

            success = False

            for check in range(50):
                if prisoner+1 == shuffledList[currentIndex]:
                    # if the prisoner's number and the number in the box matches

                    success = True
                    break
                else:
                    # if the prisoner's number and the number in the box doesnt matches

                    currentIndex = shuffledList[currentIndex]-1
                    # updating the searchIndex 
            if not success:
                break
        if success:
            totalOutBreaks+=1
            # updating the success number 
            if totalOutBreaks % 100 == 0:
                # displaying the stats 
                print("Total Iterations", iterations)
                print("Total Success", totalOutBreaks)

except KeyboardInterrupt:
    # handling the quit event of the program 
    print("Seed:", seed)
    print("Quitting...")
    print("Total Iterations", iterations)
    print("Total Success", totalOutBreaks)
    print("[SUCCESS PERCENTAGE]", (totalOutBreaks/iterations)*100)
