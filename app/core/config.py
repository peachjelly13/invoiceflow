from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    #App
    APP_NAME: str
    APP_ENV: str = "development"
    DEBUG: bool = True  #Set This False for production
    SECRET_KEY: str

    # PostgreSQL
    DATABASE_URL:str
    
    # Redis
    REDIS_URL:str
    
    # Anthropic
    ANTHROPIC_API_KEY:str
   
    # JWT
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ALGORITHM: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )

settings = Settings()

