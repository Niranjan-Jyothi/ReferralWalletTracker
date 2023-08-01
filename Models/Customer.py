from datetime import date
import Constants

class Customer:
    """ A class representing a customer. """

    def __init__(self, name, phoneNumber, email, specialOccasion, gender, wallet = 0):
        self.Name: str = name
        self.PhoneNumber: int = phoneNumber
        self.Email: str = email
        self.SpecialOccasion: date = specialOccasion.strftime(Constants.DateTimeFormat)
        self.Gender = gender
        self.Wallet: int = wallet
        self.RegisteredAt: date = date.today().strftime(Constants.DateTimeFormat)