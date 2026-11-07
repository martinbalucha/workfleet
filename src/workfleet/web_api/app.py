from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(title="Workfleet", redirect_slashes=False)
handler = Mangum(app, lifespan="off")
