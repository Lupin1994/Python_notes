import view,functions

def start():
    while True:
        action_number = view.action_number()
        match action_number:
            case 1:
                functions.show('all')
            case 2:
                functions.add()
            case 3:
                functions.show('all')
                functions.del_show('del')
            case 4:
                functions.show('all')
                functions.del_show('edit')
            case _:
                view.goodbuy()
                break
                
            
        