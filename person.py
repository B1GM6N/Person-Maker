people = []

class person:
   
    def __init__(self, gender, name, hairstyle, haircolor, shirt, hoodie, jacket, pants, shoes):
        self.haircolor = haircolor
        self.hairstyle = hairstyle
        self.shirt = shirt
        self.hoodie = hoodie
        self.jacket = jacket
        self.pants = pants
        self.shoes = shoes
        self.name = name
        self.gender = gender
   
    def change_clothes(self, shirt, hoodie, jacket, pants, shoes):
        self.shirt = shirt
        self.hoodie = hoodie
        self.jacket = jacket
        self.pants = pants
        self.shoes = shoes

    def change_hair(self, hairstyle, haircolor):
        self.haircolor = haircolor
        self.hairstyle = hairstyle
    
    def print_everything(self):
        print(self.gender)
        print(self.name)
        print(self.hairstyle)
        print(self.haircolor)
        print(self.shirt)
        print(self.hoodie)
        print(self.jacket)
        print(self.pants)
        print(self.shoes)
    
def main():
    while True:
        print("Would you like to 1 - make a person or 2 - change a persons clothes or hair? or 3 - Leave.")
        option = input(">")
        if option == "1":
            print("Lets make a person!")
            print("If your person is not wearing this type of clothing type none.")
            name = input("What is their name?")
            people.append(name)
            gender = input("What is their gender?")
            hair = input("What is their hairstyle?")
            color = input("What is their hair color?")
            shirt = input("What shirt are they wearing?")
            hoodie = input("What hoodie are they wearing?")
            jacket = input("What jacket are they wearing?")
            pants = input("What pants are they wearing?")
            shoes = input("What shoes are they wearing?")
            name = person(gender, name, hair, color, shirt, hoodie, jacket, pants, shoes)
            name.print_everything()
            
            
        elif option == "2":
            print("Who are you changing?")
            name = input(">")
            if name in people:
                print("Would you like to 1 - change their clothes 2 - change their hair.")
                change = input(">")
                if change == "1":
                    shirt = input("What new shirt are they wearing?")
                    hoodie = input("What new hoodie are they wearing?")
                    jacket = input("What new jacket are they wearing?")
                    pants = input("What new pants are they wearing?")
                    shoes = input("What new shoes are they wearing?")
                    name.change_clothes(shirt, hoodie, jacket, pants, shoes)
                    name.print_everything()
                elif change == "2":
                    hair = input("What is their hairstyle?")
                    color = input("What is their hair color?")
                    name.change_hair(hair, color)
                    name.print_everything
                else:
                    print("not valid input.")
            else:
                print("That person has not been made yet.")
        elif option == "3":
            break
        else:
            print("not valid input")
                

main()