"""

OOP Return on investment calculator. Can take itemized dictionaries of expenses, income, and investment and do the math for the user.

"""


#Runs all the math. Takes name parameter for light personalization
class Calculating():
    def __init__(self, name):
        self.name = name
        self.income = 0
        self.expense = 0
        
    #Builds dictionaries for income, expenses, and investment in property
    def build_dict(self, category_name):
        d = {}
        self.category_name = category_name
        choice = input(f"If you would like assistance calculating your {category_name} please enter 'c'. If you already have the value, enter 'e'. ").strip().lower()
        while True:
            if choice == "c":
                while True:
                    category = input(f"What {category_name} category would you like to add to calculations? If complete, enter 'd' ").strip().title()
                    if category == 'D':
                        return d
                    else: 
                        try: 
                            amount = float(input(f"And what is the amount for this category, {self.name}? "))
                            d[category] = amount
                        except ValueError:
                            print("Please enter a valid integer.")
            
            elif choice == "e":
                try:
                    final_amount = float(input(f"What is your total {category_name} for this property? "))
                    d["total"] = final_amount
                    return d
                except ValueError:
                    print("Please enter a valid integer.")

    #Income finalization
    def total_income(self):  
        final_dict = self.build_dict("income") 
        final_amount = sum(final_dict.values())
        self.income = final_amount
        while True:
            if len(final_dict) > 1:
                print(f"{self.name.title()}, your income breakdown is {final_dict}")
            check = input(f"Your total monthly income is {final_amount}. Your total yearly income is {final_amount * 12}. Does this seem correct? Please enter 'y' for yes,'n' for no. ")
            while True:
                if check == 'y':
                    print(f"Thank you, {self.name}. Let us proceed.")
                    break
                elif check == 'n':
                    print("Very well, let us start total income calculations again.")
                    final_dict = self.build_dict("income")
                else:
                    print("Please enter a valid answer.")
            break

    #Expense finalization 
    def expenses(self):
        final_dict = self.build_dict("expenses") 
        final_amount = sum(final_dict.values())
        self.expense = final_amount
        while True:
            if len(final_dict) > 1:
                print(f"Your expenses breakdown is {final_dict}")
            check = input(f"Your total monthly expenses: {final_amount}. Your total yearly expenses: {final_amount * 12}. Does this seem correct? Please enter 'y' for yes,'n' for no. ")
            while True:
                if check == 'y':
                    print(f"Thank you, {self.name}. Let us proceed.")
                    break
                elif check == 'n':
                    print(f"Very well, {self.name.title()}, let us start total expense calculations again.")
                    final_dict = self.build_dict("expenses")
                else:
                    print("Please enter a valid answer.")
            break

    #Cash flow calculations
    def cash_flow(self):
        flow = self.income - self.expense
        print(f"Your overall monthly cash flow: {flow}. Your yearly flow: {flow * 12}")

    #Final calculations, routes into investment dictionary setup
    def cash_return(self):
        final_dict = self.build_dict("return on investment") 
        final_amount = sum(final_dict.values())
        while True:
            if len(final_dict) > 1:
                print(f"{self.name.title()}, your investment breakdown is {final_dict}")
            check = input(f"Your total investment is {final_amount}. Does this seem correct? Please enter 'y' for yes,'n' for no. ")
            while True:
                if check == 'y':
                    print(f"Thank you, {self.name}. Let us proceed.")
                    break
                elif check == 'n':
                    print("Very well, let us start return on investment calculations again.")
                    final_dict = self.build_dict("return on investment")
                else:
                    print("Please enter a valid answer.")
            break
        roi_base = ((self.income - self.expense) * 12)/final_amount
        roi = roi_base * 100
        print(f"{self.name.title()}, your cash-on-cash return on investment is {roi}%.")


class Main:
    def instructions():
        print("""
            Welcome your friendly neighborhood rental Return on Investment calculator! In order for us to calculate your final RoI, we will need the total income for the property and total expenses. If you only have an itemized or partially totalled amount that's okay, the calculator will take that information and do the math for you! 
            \n Please only enter digits for all dollar amounts and enter as monthly totals, otherwise the math will be off.
        """)
        
    def run():
        Main.instructions()
        name = input("May I have your name? ")
        calc = Calculating(name)
        calc.total_income()
        calc.expenses()
        calc.cash_flow()
        calc.cash_return()

Main.run()