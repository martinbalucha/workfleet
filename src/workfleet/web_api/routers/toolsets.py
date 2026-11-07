from fastapi.routing import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from workfleet.web_api.dtos.toolsets.create_toolset_request import CreateToolsetRequest
from workfleet.web_api.dtos.toolsets.create_toolset_response import (
    CreateToolsetResponse,
)
from workfleet.web_api.dtos.toolsets.get_toolset_response import GetToolsetResponse

router = APIRouter(prefix="/toolsets", tags=["toolsets"])


@router.post("", status_code=HTTP_201_CREATED, response_model=CreateToolsetResponse)
def create(body: CreateToolsetRequest) -> CreateToolsetResponse:
    raise NotImplementedError()


@router.get("/{toolset_id}", status_code=HTTP_200_OK, response_model=GetToolsetResponse)
def get(toolset_id: str) -> GetToolsetResponse:
    raise NotImplementedError()
