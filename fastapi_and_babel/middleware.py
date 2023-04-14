from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from fastapi.responses import StreamingResponse


class Middleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next) -> StreamingResponse:
        locale = request.headers.get("locale")

        if locale:
            request.app.state.babel.default_locale = locale
            
        response = await call_next(request)
        return response