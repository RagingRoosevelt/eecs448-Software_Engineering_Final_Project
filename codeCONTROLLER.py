from codeVIEW import GUI



recipes=[]
i=0

gui = GUI()
gui.buildGUI()

while True:
    gui.root.update()
    
    action = gui.getRecentAction()
    if action!=None:
        print(action)
    
    if action=="quit":
        gui.root.destroy()
        break
    
