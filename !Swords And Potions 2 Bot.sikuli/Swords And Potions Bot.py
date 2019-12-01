x=1
setAutoWaitTimeout(3)
import time

druid="ShopKeeper.PNG"
druid1="ClericalMark.PNG"
druid2="ShockDarts.PNG"
druid3="SoftBoots.PNG"

blacksmith="Sorceress.PNG"
blacksmith1="MagicScrol-1.PNG"
blacksmith2="LuckyScroll.PNG"
blacksmith3="FortuneScroll.PNG"

shopkeeper="BlackSmith.PNG"
shopkeeper1="PoleAxe.PNG"
shopkeeper2="PurseOpener.PNG"
shopkeeper3="SoldierSword.PNG"

carpenter="LeatherWorker-1.PNG"
carpenter1="Barbarian Chainmail.PNG"
carpenter2="FurArmor.PNG"
carpenter3="SoldierHelmet.PNG"

doubleClick("RestartFile2.PNG")
time.sleep(6)
if exists("BigRestartErr-1.PNG"):
	click(Pattern("BigRestartErr-2.PNG").targetOffset(-1,181))

while x==1:
    if exists("AreUHuman-1.PNG"):
		click(Pattern("FireFoxOpened-2.PNG").targetOffset(579,-49))
		time.sleep(6)
		doubleClick("FireFoxBrowser-1.PNG")
		time.sleep(6)
		click(Pattern("FireFoxOpened-3.PNG").targetOffset(297,48))
		time.sleep(8)
		dragDrop(Pattern("ScrollTest-2.PNG").targetOffset(0,-100),Pattern("ScrollTest-3.PNG").targetOffset(0,27))
    if exists(Pattern("Summary.PNG").targetOffset(381,220)):
        click(Pattern("Summary.PNG").targetOffset(381,220))
    if exists("OpenShop.PNG"):
        click("OpenShop.PNG")

    if druid1 != 0:
        if exists(druid):
			click(druid)
			click(druid1)
			if exists("CompMissing.PNG"):
				click("RedX.PNG")
				if druid2 == 0:
					click("CloseMenu.PNG")
				else:
					click(druid2)
					if exists("CompMissing.PNG"):
						click("RedX.PNG")
						if druid3 == 0:
							click("CloseMenu.PNG")
						else:
							click(druid3)
							if exists("CompMissing.PNG"):
								click("RedX.PNG")
								click("CloseMenu.PNG")
    if blacksmith1 != 0:
        if exists(blacksmith):                
            click(blacksmith)
            click(blacksmith1)
            if exists("CompMissing.PNG"):
		        click("RedX.PNG")
		        if blacksmith2 == 0:
        		    click("CloseMenu.PNG")
		        if blacksmith2 != 0:
					click(blacksmith2)
					if exists("CompMissing.PNG"):
						click("RedX.PNG")
						if blacksmith3 == 0:
							click("CloseMenu.PNG")
						if blacksmith3 != 0:
							click(blacksmith3)
							if exists("CompMissing.PNG"):
								click("RedX.PNG")
								click("CloseMenu.PNG")
    if shopkeeper1 != 0:
        if exists(shopkeeper):                
            click(shopkeeper)
            click(shopkeeper1)
            if exists("CompMissing.PNG"):
        		click("RedX.PNG")
		        if shopkeeper2 == 0:
		            click("CloseMenu.PNG")
		        if shopkeeper2 != 0:
					click(shopkeeper2)
	                if exists("CompMissing.PNG"):
						click("RedX.PNG")
						if shopkeeper3 == 0:
							click("CloseMenu.PNG")
						if shopkeeper3 != 0:
							click(shopkeeper3)
							if exists("CompMissing.PNG"):
									click("RedX.PNG")
									click("CloseMenu.PNG")
    if carpenter1 != 0:
        if exists(carpenter):
			click(carpenter)
			click(carpenter1)
			if exists("CompMissing.PNG"):
				click("RedX.PNG")
				if carpenter2 == 0:
					click("CloseMenu.PNG")
				if carpenter2 != 0:
					click(carpenter2)
					if exists("CompMissing.PNG"):
						click("RedX.PNG")
						if carpenter3 == 0:
							click("CloseMenu.PNG")
						if carpenter3 != 0:
							click(carpenter3)
							if exists("CompMissing.PNG"):
								click("RedX.PNG")
								click("CloseMenu.PNG")   
    if exists("CloseBTN.PNG"):        
        click("CloseBTN.PNG")
    if exists("SmallX.PNG"):        
        click("SmallX-1.PNG")
    if exists("done.png"):        
        click("done.png")
    if exists("BigNext.PNG"):
		click("BigNext.PNG")
    if exists("OK.PNG"):
        click("OK.PNG")        
    if exists("CloseMenu.PNG"):
        click("CloseMenu.PNG")
    if exists("Spin.PNG"):
		click("Spin.PNG")
		wait("SpinClose.PNG")
		click("SpinClose.PNG")
    if exists("EndProg.PNG"):
        x = 0            
   

