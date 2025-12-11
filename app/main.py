from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_auth, routes_prediction
from app.middleware import logging_middleware
from app.core.exceptions import register_exception_handlers


app = FastAPI(title='Car Price Prediction API')

# link middleware 
app.add_middleware(logging_middleware)

# link endpoints
app.include_router(routes_auth.router, tags=['Auth'])
app.include_router(routes_prediction.router, tags=['Prediction'])

# monitoring using Prometheus
Instrumentator().instrument(app).expose(app)

# add exception handler
register_exception_handlers(app)