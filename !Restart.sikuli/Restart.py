x=1
setAutoWaitTimeout(2)
while x==1:
    if exists("runSikuli.png"):
        click("runSikuli.png")
    if exists("endProg-1.PNG"):
        x = 0