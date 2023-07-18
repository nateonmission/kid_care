from functools import lru_cache
from pathlib import Path

from markdown import markdown
from fastapi import APIRouter
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from starlette.responses import HTMLResponse, RedirectResponse

import config

router = APIRouter()

@router.get("/", include_in_schema=False)
async def redirect_to_docs():
    """
    Redirect root path to Swagger UI.

    Returns:
        A `RedirectResponse` to Swagger UI page.
    """
    return RedirectResponse(url=f"/docs")


@router.get("/docs", include_in_schema=False)
def overridden_swagger():
    # return get_swagger_ui_html(
    #     title=config.PROJECT_TITLE + " - Swagger UI",
    #     openapi_url=f"{config.ROOT_PATH}/openapi.json",
    #     swagger_favicon_url=config.FAVICON_PATH,
    # )
    return get_swagger_ui_html(openapi_url="/openapi.json", title= config.PROJECT_TITLE)

@router.get("/redoc", include_in_schema=False)
def overridden_redoc():
    """
    Overrides default ReDoc HTML with a custom favicon.

    Returns:
        ReDoc HTML with a custom favicon.
    """
    return get_redoc_html(
        title=config.PROJECT_TITLE + " - Swagger UI",
        openapi_url=f"/openapi.json",
        redoc_favicon_url=config.FAVICON_PATH,
    )


@lru_cache
def _get_changelog_html() -> bytes:
    """
    Retrieve changelog markdown file and convert to HTML.

    Returns:
        HTML representation of the changelog markdown file.
    """
    changelog_path: Path = Path(__file__).parent / "CHANGELOG.md"
    _changelog_html = markdown(changelog_path.read_text())
    return _changelog_html


@router.get("/changelog", response_class=HTMLResponse)
async def changelog() -> HTMLResponse:
    """
    Display the changelog for this API.

    Returns:
        HTMLResponse containing the changelog for this API.
    """
    return HTMLResponse(content=_get_changelog_html())