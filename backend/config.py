from pydantic_settings import BaseSettings
from functools import lru_cache
import os,sys
root_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path=os.path.join(root_path, ".env.local")
class Settings(BaseSettings):
    db_host: str = "localhost"
    db_port: int = 5433
    db_name: str = "eduagent"
    db_user: str
    db_password: str
    @property
    def database_url(self) -> str:
        return(f"postgresql+asyncpg://{self.db_user}:{self.db_password}"
               f"@{self.db_host}:{self.db_port}/{self.db_name}"
)
    milvus_host: str = "localhost"
    milvus_port: int =19531

    deepseek_api_key: str ="qsgqhd"
    deepseek_base_url: str ="https://api.deepseek.com/v1"
    deepseek_model_chat: str ="deepseek_flash"
    deepseek_model_coder: str ="deepseek_flash"

    reranker_model_path: str ="models/reranker/bge-reranker-large"
    classifier_model_path: str="./models/classifier/all_miniLM-L6-v2"
    bge_m3_model_path: str="./models/embedding/bge_m3"


    jwt_secret_key:str
    jwt_algorithm:str = "HS256"
    jwt_access_token_expires_minutes :int=10080

    kb_mcp_server_url:str="http://localhost:8080/mcp/kb"
    web_search_mcp_url: str="http://localhost:8080/mcp/web-search"
    tavily_api_key:str=""

    app_env: str="local"
    app_debug: bool=False
    app_host: str="0.0.0.0"
    app_port: str=8080
    log_level: str="INFO"
    default_tenant_id:str="tenant_default"
    class Config:
        env_file=env_path
        env_file_encoding="utf-8"
        case_sensitive=False
        extra="ignore"
@lru_cache()
def get_settings()->Settings:
    return Settings()

