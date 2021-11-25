class att:

    def __init__(self, itemname, itemcode, price = 0 ):
        self.itemname = itemname
        self.itemcode = itemcode
        self.price = price

class supermart:

    itms = []
    selecteditms = []

    def __init__(self, itemname, itemcode, price ):
        b = att(itemname,itemcode=itemcode, price = price)
        self.itms.append(b)
    
    def show(self):
        print("============== AVAILBALE ITEMS ==========")
        
        pos=0

        for att in self.itms:
            print("============ ", pos, " ==========") 
            pos += 1   
            self.display(att)
            
    
    def select(self):
        print("========== SELECT AN ITEM  =======")
        print("====== HOW MANY ITEMS YOU WANT? ======")
        neededitms = int(input())

        for i in range(0, neededitms ):
            print("====== INPUT THE ITEM NO ======")
            selecteditms = int(input())
            print("========== SELECTED ITEM =======")
            b = self.getattById(selecteditms - 1)
            self.selecteditms.append(b)
            print(self.display(b))

    def getattById(self, position):
        return self.itms[position]

    def display(self, itms):
        print("Item name : ", itms.itemname)
        print("Item code : ", itms.itemcode)
        print("item Price : ", itms.price)

    def selecteditem(self):
        return self.selecteditms


class cart:

    items = []
    def __init__(self, myBooks):
        self.items = myBooks
    
    def display(self):
        pos = 0
        for itms in self.items:
            print("============ CART ITEMS ========")
            pos += 1
            print("============ ITEM NO", pos,"========")
            print("Item name : ", itms.itemname)
            print("item code : ", itms.itemcode)
            print("item Price : ",itms.price)

    def getTotal(self):
        total = sum(map(lambda b : b.price, self.items))
        print("=========== TOTAL PRICE =======")
        print(total)
   
    def delete(self):
        print("=========== DO YOU WANT DELETE? 1 = YES, 0 = NO")
        choice = int(input())
        if (choice == 1):
            print("=========== ENTER ITEM NUMBER =======")
            position = int(input())
            self.items.remove(self.getitmsById(position))
        else:
            print("=========== NO ITEMS DELETED =========")

    def getitmsById(self, position):
        return self.items[position - 1]

    
if "__MAIN__":

    print("========== WELCOME TO SUPER MART ==========")

    sm = supermart("rice", "ABC", 55)
    sm = supermart("wheat", "wht", 70)
    sm = supermart("pulses", "pls", 100)
    sm = supermart("fruits", "fts", 150)
    sm = supermart("vegetables", "veg", 100)
    
    
    sm.show()

    sm.select()

    selecteditems = sm.selecteditem()
    
    print(selecteditems)

    c = cart(selecteditems)

    c.display()

    c.delete()

    c.getTotal()

   