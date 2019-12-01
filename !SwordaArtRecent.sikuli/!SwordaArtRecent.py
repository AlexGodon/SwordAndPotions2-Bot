x=1
setAutoWaitTimeout(3)

shopkeeper="ShopKeeper-1.PNG"
shopkeeper1="DustTriad.PNG"
shopkeeper2=0
shopkeeper3=0

blacksmith="LeatherWorker.PNG"
blacksmith1="SoftGloves.PNG"
blacksmith2="RidingBoots.PNG"
blacksmith3="LeatherCuirass.PNG"

druid="DruidTry-1.PNG"
druid1="CombatStaff.PNG"
druid2="OakenStaff.PNG"
druid3="Supple Dust.png"

while x==1:
    if exists(Pattern("Summary.PNG").targetOffset(381,220)):
        click(Pattern("Summary.PNG").targetOffset(381,220))
    if exists("OpenShop.PNG"):
        click("OpenShop.PNG")
    if exists("CloseBTN.PNG"):        
        click("CloseBTN.PNG")
    if exists("done.png"):        
        click("done.png")
    if exists("OK.PNG"):
        click("OK.PNG")        
    if exists("CloseMenu.PNG"):
        click("CloseMenu.PNG")  
    if exists("RandomError.PNG"):
		click(Pattern("RefreshBT.PNG").targetOffset(76,1))
		wait(Pattern("RefreshBT.PNG").targetOffset(76,1))
		dragDrop(Pattern("TopDragBar.PNG").targetOffset(-1,-2),Pattern("BottomDragBar.PNG").targetOffset(-2,95))
		if exists("Spin.PNG"):
			click("Spin.PNG")
			wait("SpinClose.PNG")
			click("SpinClose.PNG")
    if druid1 != 0:
        if exists(druid):                
            click(druid)
            if exists(druid1):
                click(druid1)
                if exists("CompMissing.PNG"):
                    click("RedX.PNG")
                    if druid2 == 0:
                        click("CloseMenu.PNG")
                    if druid2 != 0:
                        if exists(druid2):
                            click(druid2)
                            if exists("CompMissing.PNG"):
                                click("RedX.PNG")
                                if druid3 == 0:
                                    click("CloseMenu.PNG")
                                if druid3 != 0:
                                    if exists(druid3):
                                        click(druid3)
                                        if exists("CompMissing.PNG"):
                                            click("RedX.PNG")
                                            click("CloseMenu.PNG")
        
    if blacksmith1 != 0:
        if exists(blacksmith):                
            click(blacksmith)
            if exists(blacksmith1):
                click(blacksmith1)
                if exists("CompMissing.PNG"):
                    click("RedX.PNG")
                    if blacksmith2 == 0:
                        click("CloseMenu.PNG")
                    if blacksmith2 != 0:
                        if exists(blacksmith2):
                            click(blacksmith2)
                            if exists("CompMissing.PNG"):
                                click("RedX.PNG")
                                if blacksmith3 == 0:
                                    click("CloseMenu.PNG")
                                if blacksmith3 != 0:
                                    if exists(blacksmith3):
                                        click(blacksmith3)
                                        if exists("CompMissing.PNG"):
                                            click("RedX.PNG")
                                            click("CloseMenu.PNG")
                                


    if shopkeeper1 != 0:
        if exists(shopkeeper):                
            click(shopkeeper)
            if exists(shopkeeper1):
                click(shopkeeper1)
                if exists("CompMissing.PNG"):
                    click("RedX.PNG")
                    if shopkeeper2 == 0:
                        click("CloseMenu.PNG")
                    if shopkeeper2 != 0:
                        if exists(shopkeeper2):
                            click(shopkeeper2)
                            if exists("CompMissing.PNG"):
                                click("RedX.PNG")
                                if shopkeeper3 == 0:
                                    click("CloseMenu.PNG")
                                if shopkeeper3 != 0:
                                    if exists(shopkeeper3):
                                        click(shopkeeper3)
                                        if exists("CompMissing.PNG"):
                                            click("RedX.PNG")
                                            click("CloseMenu.PNG")

    
    if exists("EndProg.PNG"):
        x = 0            
   


