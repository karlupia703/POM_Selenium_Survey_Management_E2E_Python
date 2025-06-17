from dotenv import load_dotenv
import os
load_dotenv()
class Config:
    base_url = "https://survey-building-app-develop-iymj66chvq-uc.a.run.app/"
    language = "pt_BR"  # Options: "Español", "en_US" , pt_BR

    Email = os.getenv("user") # Add your username here
    Password = os.getenv("password") # Add your password here

