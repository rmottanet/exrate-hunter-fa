import os
from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.config import Config
from app.services import BCBQuotesService, ExchangeRatesService, OpenExchangeService
from app.data import DataConsolidator, DataFilter
from app.redis_service import RedisWriter, RedisReader

router = APIRouter()

bearer_scheme = HTTPBearer()

# checkout token
async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    # Verificar se o token fornecido é igual ao token esperado
    if credentials.credentials != Config.COINSNARK_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    return True

@router.get("/consolidate-and-save")
async def consolidate_and_save_data(token_valid: bool = Depends(verify_token)):
    try:
        # Consumir dados dos serviços externos
        service_1_data = BCBQuotesService.get_bcb_rates_data(Config.BCBQUOTES_API_URL)
        service_2_data = OpenExchangeService.get_openexchange_rates_data(Config.OPEN_EXCHANGE_API_URL, Config.OPEN_EXCHANGE_API_KEY)
        service_3_data = ExchangeRatesService.get_exchangerates_rates_data(Config.EXCHANGE_RATES_API_URL, Config.EXCHANGE_RATES_API_KEY)

        # Consolidar dados
        consolidator = DataConsolidator(service_1_data, service_2_data, service_3_data)
        consolidated_data = consolidator.consolidate()

        # Escrever dados consolidados no Redis
        redis_writer = RedisWriter(Config.REDIS_HOST, Config.REDIS_PORT, Config.REDIS_KEY)
        redis_writer.write_to_redis(consolidated_data)

        return {"message": "Data saved to Redis successfully!"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to consolidate and save data: {str(e)}")


@router.get("/exrates")
async def retrieve_exrates_data(token_valid: bool = Depends(verify_token)):
    try:
        # Recuperar dados do Redis
        redis_reader = RedisReader(Config.REDIS_HOST, Config.REDIS_PORT, Config.REDIS_KEY)
        redis_data = redis_reader.read_from_redis()

        # Filtrar dados
        data_filter = DataFilter(redis_data)
        filtered_data = data_filter.filter()

        return filtered_data
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to retrieve data: {str(e)}")

    
@router.get("/", response_class=HTMLResponse)
async def read_root():
    try:
        static_dir = os.path.join(os.path.dirname(__file__), "../static")
        
        if not os.path.isdir(static_dir):
            raise HTTPException(status_code=404, detail="Static directory not found")
        
        html_path = os.path.join(static_dir, "index.html")
        
        if not os.path.isfile(html_path):
            raise HTTPException(status_code=404, detail="HTML file not found")
        
        with open(html_path, "r") as file:
            html_content = file.read()

        return HTMLResponse(content=html_content, status_code=200)
    
    except HTTPException as e:
        raise e
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
