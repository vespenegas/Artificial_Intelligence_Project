# This is a sample Python script.
from tkinter import *

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# create window
root = Tk()

# create Starting Frame for budget setting
BudgetFrame = Frame(root)
BudgetFrame.grid(row=0, column=0)

def submit():  # Creates sumbit screen for User Convenience Where you call methods
    saveInputs()
    clear_frame()
    titleName = Label(BudgetFrame, text="Hello and Welcome to our shopping list Application", font=35)
    StartingTextEmptyWin2 = Label(BudgetFrame, text="  ")
    processingLabel = Label(BudgetFrame, text="Form has been submitted.Please wait while we process your order",
                            font=25)
    titleName.grid(row=0, column=0)
    StartingTextEmptyWin2.grid(row=1, column=0)
    processingLabel.grid(row=2, column=0)
    # if list is created delete
    FinalScreen()


def saveInputs():  # used to update variables
    global budgetAmount, MeatOption, veggieOption, fruitOption, diaryOption, grainOption
    budgetAmount = budgetInput.get()
    MeatOption = meat.get()
    veggieOption = vegetable.get()
    fruitOption = fruit.get()
    diaryOption = diary.get()
    grainOption = grain.get()

def clear_frame():
    for widgets in BudgetFrame.winfo_children():
        widgets.destroy()

def FinalScreen():  # needs to be contected to algorithm
    clear_frame()
    FinalTotal = 'Your Total is: $' + budgetAmount
    shoppinglist = ['chicken breast', '80% lean ground beef', 'cucumber', 'avocado', 'red grape', '2% milk',
                    'english muffins',
                    'yellow peaches, cheetos', 'pear', 'whole carrots', 'bella muchroom', 'pumpkin pie']
    TitleName = Label(BudgetFrame, text="Hello and Welcome to our shopping list Application", font=35)
    StartingTextEmptyWin3 = Label(BudgetFrame, text="  ")
    TitleName.grid(row=0, column=0)
    StartingTextEmptyWin3.grid(row=1, column=0)
    for i in range(len(shoppinglist)):
        curListItem = Label(BudgetFrame, text=shoppinglist[i], font=20)
        curListItem.grid(row=i + 2, column=0)
    StartingTextEmptyWin3_1 = Label(BudgetFrame, text="  ")
    StartingTextEmptyWin3_1.grid(row=len(shoppinglist) + 3, column=0)
    FinalBudgetAmount = Label(BudgetFrame, text=FinalTotal, font=25)
    FinalBudgetAmount.grid(row=(len(shoppinglist) + 4), column=0)

# create a label Widget
StartingText = Label(BudgetFrame, text="Hello and Welcome to our shopping list Application", font=(30))
StartingTextEmpty = Label(BudgetFrame, text="  ")
StartingTextEmpty2 = Label(BudgetFrame, text="  ")
StartingTextEmpty3 = Label(BudgetFrame, text="  ")

BudgetText = Label(BudgetFrame, text="Please input a budget amount into the input field below without $")
budgetInput = Entry(BudgetFrame)
budgetInput.insert(0, "00.00")
budgetAmount = budgetInput.get()

ExemptionText = Label(BudgetFrame, text="Please check off any food tree type you don't want in your list")
# 1 is checked and 0 is unchecked
meat = IntVar()  # used later for algorithm
meatCheck = Checkbutton(BudgetFrame, text="Do you not want meat in your shopping list", variable=meat)

vegetable = IntVar()  # used later for algorithm
vegetableCheck = Checkbutton(BudgetFrame, text="Do you not want vegetables in your shopping list", variable=vegetable)

fruit = IntVar()  # used later for algorithm
fruitCheck = Checkbutton(BudgetFrame, text="Do you not want fruits in your shopping list", variable=fruit)

diary = IntVar()  # used later for algorithm
diaryCheck = Checkbutton(BudgetFrame, text="Do you not want diary in your shopping list", variable=diary)

grain = IntVar()  # used later for algorithm
grainCheck = Checkbutton(BudgetFrame, text="Do you not want grain like bread or rice in your shopping list",
                         variable=grain)

SubmitButton = Button(BudgetFrame, text="Submit your budget", padx=100, command=submit, fg="white", bg="black")

# Shoving it onto the screen
StartingText.grid(row=0, column=0)
StartingTextEmpty.grid(row=1, column=0)
BudgetText.grid(row=2, column=0)
budgetInput.grid(row=3, column=0)
ExemptionText.grid(row=4, column=0)
meatCheck.grid(row=5, column=0)
vegetableCheck.grid(row=6, column=0)
fruitCheck.grid(row=7, column=0)
diaryCheck.grid(row=8, column=0)
grainCheck.grid(row=9, column=0)
StartingTextEmpty2.grid(row=10, column=0)

SubmitButton.grid(row=11, column=0)
StartingTextEmpty3.grid(row=12, column=0)
root.mainloop()

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':


# See PyCharm help at https://www.jetbrains.com/help/pycharm/