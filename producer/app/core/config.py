from pydantic import BaseSettings, validator

# Load environment variables into a pydantic BaseSetting object
class AppConfig(BaseSettings):

    PROJECT_NAME : str 
    KAFKA_HOST : str 
    KAFKA_PORT : str
    TOPIC_NAME : str 
    KAFKA_URL : str = ""

    class Config:

        case_sensitive = True

    @validator("KAFKA_URL", pre=True, always=True)
    def set_kafka_url(cls, v, values, **kwargs):
        return values['KAFKA_HOST'] + ":" + values['KAFKA_PORT'] 
# Configuration for the producer is handled through 
# environment variables (in .env file) that are read in by a Pydantic BaseSettings object:
app_config = AppConfig()