#This file defines all comnfiguration values the app needs
#(DB connection )
from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    #MongoDG settings: tells where as to make connect and what nees to do
    MONGO_URI: str = "mongodb://localhost:27017"
    MONGO_DB_NAME: str = "it_servivedesk"

    #GIVES THE APP NAME
    APP_NAME: str ="IT Service Desk App API"

    #Inform pydantic settings to load vlaues from .env file
    model_config=SettingsConfigDict(env_file=".env",env_file_encoding="utf-8")

#Shared settings object that all other files can import
settings=Settings()    