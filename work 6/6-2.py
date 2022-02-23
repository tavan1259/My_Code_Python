class ShoppingCart:
    def __init__(self, id):
        self.id = id
        self.books = []

    def add_book(self, book, n,total):
        ad_b = [book,n,total]
        if len(self.books) == 0 :
            self.books.append(ad_b)
        else :
            if ad_b not in self.books:
                for All_book in self.books:
                    if book not in All_book:
                        self.books.append(ad_b)
                        break
                    else:
                        if book in All_book:
                            All_book[1] += n
                            break
                    print("\n")

            

    def delete_book(self , book):
        if len(self.books) > 0:
            for D_book in self.books:
                if D_book[0] == book:
                    self.books.remove(D_book)
                    break


    def get_total(self):
        cal_total = 0
        if len(self.books) > 0:
            for num in range(len(self.books)):
                cal_total += (self.books[num][2] * self.books[num][1])
        
        return cal_total
            
    def __lt__(self, rhs):

        return self.get_total() < rhs.get_total()


cart = ShoppingCart(64015048)
cartMan = ShoppingCart(2020)

cart.add_book("b1", 2,200)
cart.add_book("b2", 7,1000)
cart.add_book("b1", 3,200)
cart.add_book("b2", 7,1000)
cart.add_book("b3", 10,10000)


print(cart.books)
cart.delete_book("b3")
cartMan.delete_book("b3")
print(cart.books)

print(f"ราคารวมของหนังสือทั้งหมดในตะกร้า 1 = {cart.get_total()}")
print(f"ราคารวมของหนังสือทั้งหมดในตะกร้า 2 = {cartMan.get_total()}")
print(cartMan.__lt__(cart))
print(cart < cartMan)