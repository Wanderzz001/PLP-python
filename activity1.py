class Town:
    def __init__(self, name, population, region):
        self.name = name
        self.population = population
        self.region = region

    def info(self):
        print(f"🏘️ Town: {self.name}, Population: {self.population}, Region: {self.region}")

    def grow(self, amount):
        self.population += amount
        print(f"{self.name} grew by {amount} people. New population: {self.population}")

    def shrink(self, amount):
        self.population = max(0, self.population - amount)
        print(f"{self.name} lost {amount} people. New population: {self.population}")



class City(Town):
    def __init__(self, name, population, region, mayor, gdp):
        super().__init__(name, population, region)  
        self.mayor = mayor
        self.gdp = gdp  
    def info(self):
        print(f"🌆 City: {self.name}, Population: {self.population}, Region: {self.region}, Mayor: {self.mayor}, GDP: ${self.gdp}M")

    def develop(self, amount):
        self.gdp += amount
        print(f"{self.name}'s economy grew by ${amount}M. New GDP: ${self.gdp}M")
