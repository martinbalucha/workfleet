from fastapi import FastAPI
from mangum import Mangum

from workfleet.web_api.routers.toolsets import router as toolsets_router

app = FastAPI(title="Workfleet", redirect_slashes=False)
app.include_router(toolsets_router, prefix="/v1")

# Register lambda adapter
handler = Mangum(app, lifespan="off")
