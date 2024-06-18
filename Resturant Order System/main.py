import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image, ImageTk
import random
from datetime import date
from datetime import datetime

# shows menu items and prices
prices = {
    'Shrimp Dumpling' : 10,
    'Beef Ribs' : 12,
    'Lotus Wrapped Sticky Rice' : 16,
    'Steamed Dumplings' : 12,
    'Chicken Feet' : 12,
    'Egg Tarts' : 5,
}

root  = Tk()

# name of my resturant
root.title("Derrick's Dim Sum")

# ------------------------------------FUNCTIONS--------------------------------------------- #

#region Generating a random Order ID when starting a new order
def ORDER_ID():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    order_id = 'NUM_'
    random_letters = ''
    random_digits = ''
    for i in range(0,3):
        random_letters += random.choice(letters)
        random_digits += str(random.choice(numbers))

    order_id += random_letters + random_digits
    return order_id
#endregion

#region Add to Order Button
def add():
    # updating the transaction label
    current_order = orderTransaction.cget("text")
    added_dish = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")]) + "$ "
    updated_order = current_order + added_dish
    orderTransaction.configure(text=updated_order)

    # updating the order total label
    order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
    order_total = order_total.replace("$", "")
    updated_total = int(order_total) + prices[displayLabel.cget("text")]
    orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")
#endregion

#region Remove Button Function
def remove():
    dish_to_remove = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")])
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    if dish_to_remove in transaction_list:
        # update transaction label
        transaction_list.remove(dish_to_remove)
        updated_order = ""
        for item in transaction_list:
            updated_order += item + "$ "

        orderTransaction.configure(text = updated_order)

        # update transaction total
        order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
        order_total = order_total.replace("$", "")
        updated_total = int(order_total) - prices[displayLabel.cget("text")]
        orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")

#endregion

#region Display Button Functions
def displayShrimpDumpling():
    ShrimpDumplingFrame.configure(
        relief = "sunken",
        style = "SelectedDish.TFrame"
    )
    lotusWrappedStickyRiceFrame.configure(style = "DishFrame.TFrame")
    EggTartsFrame.configure(style= "DishFrame.TFrame")
    ChickenFeetFrame.configure(style = "DishFrame.TFrame")
    steamedDumplingFrame.configure(style = "DishFrame.TFrame")
    BeefRibsFrame.configure(style = "DishFrame.TFrame")

    displayLabel.configure(
        image = ShrimpDumplingImage,
        text = "Shrimp Dumpling",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        compound = "bottom",
        padding = (5, 5, 5, 5),
    )

def displayBurger():
    BeefRibsFrame.configure(
        relief = "sunken",
        style = "SelectedDish.TFrame"
    )
    lotusWrappedStickyRiceFrame.configure(style="DishFrame.TFrame")
    EggTartsFrame.configure(style="DishFrame.TFrame")
    ChickenFeetFrame.configure(style="DishFrame.TFrame")
    steamedDumplingFrame.configure(style="DishFrame.TFrame")
    ShrimpDumplingFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        text = "Beef Ribs",
        font = ('Helvetica', 14,"bold"),
        foreground = "white",
        image = ribsImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displayBeefRibs():
    lotusWrappedStickyRiceFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame"
    )
    ShrimpDumplingFrame.configure(style="DishFrame.TFrame")
    EggTartsFrame.configure(style="DishFrame.TFrame")
    ChickenFeetFrame.configure(style="DishFrame.TFrame")
    steamedDumplingFrame.configure(style="DishFrame.TFrame")
    BeefRibsFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        text = "Lotus Wrapped Sticky Rice",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        image = LotusRiceImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displaySteamedDumplings():
    steamedDumplingFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame"
    )
    lotusWrappedStickyRiceFrame.configure(style="DishFrame.TFrame")
    EggTartsFrame.configure(style="DishFrame.TFrame")
    ChickenFeetFrame.configure(style="DishFrame.TFrame")
    ShrimpDumplingFrame.configure(style="DishFrame.TFrame")
    BeefRibsFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        text = "Steamed Dumplings",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        image = steamedDumplingsImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displayEggTarts():
    EggTartsFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame"
    )
    lotusWrappedStickyRiceFrame.configure(style="DishFrame.TFrame")
    ShrimpDumplingFrame.configure(style="DishFrame.TFrame")
    ChickenFeetFrame.configure(style="DishFrame.TFrame")
    steamedDumplingFrame.configure(style="DishFrame.TFrame")
    BeefRibsFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        text = "Egg Tarts",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        image = EggTartsImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displayChickenFeet():
    ChickenFeetFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame"
    )
    lotusWrappedStickyRiceFrame.configure(style="DishFrame.TFrame")
    EggTartsFrame.configure(style="DishFrame.TFrame")
    ShrimpDumplingFrame.configure(style="DishFrame.TFrame")
    steamedDumplingFrame.configure(style="DishFrame.TFrame")
    BeefRibsFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        image = ChickenFeetImage,
        text = "Chicken Feet",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )
#endregion

#region Generating Receipt from Order Button
def order():
    new_receipt = orderIDLabel.cget('text')
    new_receipt = new_receipt.replace("ORDER ID : ","")
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    order_day = date.today()
    order_time = datetime.now()

    for item in transaction_list:
        item += "$ "

    with open(new_receipt, 'w') as file:
        file.write("Derrick's Dim Sum")
        file.write("\n")
        file.write(order_day.strftime("%x"))
        file.write("\n")
        file.write(order_time.strftime("%X"))
        file.write("\n\n")
        for item in transaction_list:
            file.write(item + "\n")
        file.write("\n\n")
        file.write(orderTotalLabel.cget("text"))

    orderTotalLabel.configure(text = "TOTAL : 0$")
    orderIDLabel.configure(text = "ODER ID: " + ORDER_ID())
    orderTransaction.configure(text = "")

#endregion

# ---------------------------------- STYLING AND IMAGES ------------------------------------ #

#region Style configurations
s = ttk.Style()
s.configure('MainFrame.TFrame', background = "#2B2B28")
s.configure('MenuFrame.TFrame', background = "#4A4A48")
s.configure('DisplayFrame.TFrame', background = "#0F1110")
s.configure('OrderFrame.TFrame', background = "#B7C4CF")
s.configure('DishFrame.TFrame', background = "#4A4A48", relief = "raised")
s.configure('SelectedDish.TFrame', background = "#C4DFAA")
s.configure('MenuLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 13, "italic"),
            foreground = "white",
            padding = (5, 5, 5, 5),
            width = 21
            )
s.configure('orderTotalLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 10, "bold"),
            foreground = "white",
            padding = (2, 2, 2, 2),
            anchor = "w"
            )
s.configure('orderTransaction.TLabel',
            background = "#4A4A48",
            font = ('Helvetica', 12),
            foreground = "white",
            wraplength = 170,
            anchor = "nw",
            padding = (3, 3, 3, 3)
            )

# endregion

# region Images
# Top Banner images
LogoImageObject = Image.open("Images/Screen Images/logo.tiff").resize((130, 130))
LogoImage = ImageTk.PhotoImage(LogoImageObject)

TopBannerImageObject = Image.open("Images/Screen images/banner.png").resize((800, 130))
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)

# Menu images
displayDefaultImageObject = Image.open("Images/Screen Images/display.png").resize((350,360))
displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)

ShrimpDumplingImageObject = Image.open("Images/Food Images/shrimp dumpling.jpeg").resize((350,334))
ShrimpDumplingImage = ImageTk.PhotoImage(ShrimpDumplingImageObject)

ribsImageObject = Image.open("Images/Food Images/ribs.jpeg").resize((350,334))
ribsImage = ImageTk.PhotoImage(ribsImageObject)

LotusRiceImageObject = Image.open("Images/Food Images/Lotus Wrapped Sticky Rice.jpeg").resize((350,334))
LotusRiceImage = ImageTk.PhotoImage(LotusRiceImageObject)

steamedDumplingsImageObject = Image.open("Images/Food Images/steamed Dumplings.jpeg").resize((350,334))
steamedDumplingsImage = ImageTk.PhotoImage(steamedDumplingsImageObject)

ChickenFeetImageObject = Image.open("Images/Food Images/chicken feet.jpeg").resize((350,334))
ChickenFeetImage = ImageTk.PhotoImage(ChickenFeetImageObject)

EggTartsImageObject = Image.open("Images/Food Images/Egg Tarts.jpeg").resize((350,334))
EggTartsImage = ImageTk.PhotoImage(EggTartsImageObject)


#endregion

#----------------------------------- WIDGETS ----------------------------------------------- #

# region Frames

# Section Frames
mainFrame = ttk.Frame(root, width = 800, height = 580, style = 'MainFrame.TFrame')
mainFrame.grid(row = 0, column = 0, sticky = "NSEW")

topBannerFrame = ttk.Frame(mainFrame)
topBannerFrame.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 3)

menuFrame = ttk.Frame(mainFrame, style = 'MenuFrame.TFrame')
menuFrame.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "NSEW")

displayFrame = ttk.Frame(mainFrame, style = "DisplayFrame.TFrame")
displayFrame.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "NSEW")

orderFrame = ttk.Frame(mainFrame, style = "OrderFrame.TFrame")
orderFrame.grid(row = 1, column = 2, padx = 3, pady = 3, sticky = "NSEW")

# Dish Frames
ShrimpDumplingFrame = ttk.Frame(menuFrame, style = "DishFrame.TFrame")
ShrimpDumplingFrame.grid(row = 1, column = 0, sticky = "NSEW")

BeefRibsFrame = ttk.Frame(menuFrame,style ="DishFrame.TFrame")
BeefRibsFrame.grid(row = 2, column = 0, sticky ="NSEW")

lotusWrappedStickyRiceFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
lotusWrappedStickyRiceFrame.grid(row = 3, column = 0, sticky ="NSEW")

steamedDumplingFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
steamedDumplingFrame.grid(row = 4, column = 0, sticky ="NSEW")

ChickenFeetFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
ChickenFeetFrame.grid(row = 5, column = 0, sticky ="NSEW")

EggTartsFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
EggTartsFrame.grid(row = 6, column = 0, sticky ="NSEW")

#endregion

# region Top Banner Section

LogoLabel = ttk.Label(topBannerFrame, image = LogoImage, background = "#0F1110")
LogoLabel.grid(row = 0, column = 0, sticky = "W")

RestaurantBannerLabel = ttk.Label(topBannerFrame, image = TopBannerImage, background = "#0F1110")
RestaurantBannerLabel.grid(row = 0, column = 1, sticky = "NSEW")

# endregion

#region Menu Section
MainMenuLabel = ttk.Label(menuFrame, text = "MENU", style = "MenuLabel.TLabel")
MainMenuLabel.grid(row = 0, column = 0, sticky = "WE")
MainMenuLabel.configure(
    anchor = "center",
    font = ("Helvetica", 14, "bold")
)

ShrimpDumplingDishLabel = ttk.Label(ShrimpDumplingFrame, text ="Shrimp Dumpling - $10", style ="MenuLabel.TLabel")
ShrimpDumplingDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

BeefRibsDishLabel = ttk.Label(BeefRibsFrame, text ="Beef Ribs - $12", style ="MenuLabel.TLabel")
BeefRibsDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

lotusWrappedStickyRiceDishLabel = ttk.Label(lotusWrappedStickyRiceFrame, text ="Lotus Sticky Rice - $16", style ="MenuLabel.TLabel")
lotusWrappedStickyRiceDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

steamedDumplingDishLabel = ttk.Label(steamedDumplingFrame, text ="Steamed Dumplings - $12", style ="MenuLabel.TLabel")
steamedDumplingDishLabel.grid(row = 0, column = 0, padx =10, pady = 10, sticky = "W")

ChickenFeetDishLabel = ttk.Label(ChickenFeetFrame, text ="Chicken Feet - $12", style ="MenuLabel.TLabel")
ChickenFeetDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

EggTartsDishLabel = ttk.Label(EggTartsFrame, text ="Egg Tarts - $5", style ="MenuLabel.TLabel")
EggTartsDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

#Buttons
ShrimpDumplingDisplayButton = ttk.Button(ShrimpDumplingFrame, text ="Display", command = displayShrimpDumpling)
ShrimpDumplingDisplayButton.grid(row = 0, column = 1, padx = 10)

BeefRibsDisplayButton = ttk.Button(BeefRibsFrame, text ="Display", command = displayBurger)
BeefRibsDisplayButton.grid(row = 0, column = 1, padx = 10)

LotusWrappedDisplayButton = ttk.Button(lotusWrappedStickyRiceFrame, text ="Display", command = displayBeefRibs)
LotusWrappedDisplayButton.grid(row = 0, column = 1, padx = 10)

SteamedDumplingsDisplayButton = ttk.Button(steamedDumplingFrame, text ="Display", command = displaySteamedDumplings)
SteamedDumplingsDisplayButton.grid(row = 0, column = 1, padx = 10)

ChickenFeetDisplayButton = ttk.Button(ChickenFeetFrame, text ="Display", command = displayChickenFeet)
ChickenFeetDisplayButton.grid(row = 0, column = 1, padx = 10)

EggTartDisplayButton = ttk.Button(EggTartsFrame, text ="Display", command = displayEggTarts)
EggTartDisplayButton.grid(row = 0, column = 1, padx = 10)

# endregion

#region Order Section
orderTitleLabel = ttk.Label(orderFrame, text = "ORDER")
orderTitleLabel.configure(
    foreground="white", background="black",
    font=("Helvetica", 14, "bold"), anchor = "center",
    padding = (5, 5, 5, 5),
)
orderTitleLabel.grid(row = 0, column = 0, sticky = "EW")

orderIDLabel = ttk.Label(orderFrame, text = "ORDER ID : " + ORDER_ID())
orderIDLabel.configure(
    background = "black",
    foreground = "white",
    font = ("Helvetica", 11, "italic"),
    anchor = "center",
)
orderIDLabel.grid(row = 1, column = 0, sticky = "EW", pady = 1)

orderTransaction = ttk.Label(orderFrame, style = 'orderTransaction.TLabel')
orderTransaction.grid(row = 2, column = 0, sticky = "NSEW")

orderTotalLabel = ttk.Label(orderFrame, text = "TOTAL : 0$", style = "orderTotalLabel.TLabel")
orderTotalLabel.grid(row = 3, column = 0, sticky = "EW")

orderButton = ttk.Button(orderFrame, text = "ORDER", command = order)
orderButton.grid(row = 4, column = 0, sticky = "EW")


# endregion

# region Display Section
displayLabel = ttk.Label(displayFrame, image = displayDefaultImage)
displayLabel.grid(row = 0, column = 0 , sticky = "NSEW", columnspan = 2)
displayLabel.configure(background = "#0F1110")

addOrderButton = ttk.Button(displayFrame, text = "ADD TO ORDER", command = add)
addOrderButton.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton = ttk.Button(displayFrame, text = "REMOVE", command = remove)
removeOrderButton.grid(row = 1, column = 1, padx = 2, sticky = "NSEW")

#endregion



#----------------------------- GRID CONFIGURATIONS -------------------------------------------#
mainFrame.columnconfigure(2, weight = 1)
mainFrame.rowconfigure(1, weight = 1)
menuFrame.columnconfigure(0, weight = 1)
menuFrame.rowconfigure(1, weight = 1)
menuFrame.rowconfigure(2, weight = 1)
menuFrame.rowconfigure(3, weight = 1)
menuFrame.rowconfigure(4, weight = 1)
menuFrame.rowconfigure(5, weight = 1)
menuFrame.rowconfigure(6, weight = 1)
orderFrame.columnconfigure(0, weight = 1)
orderFrame.rowconfigure(2, weight = 1)



root.mainloop()