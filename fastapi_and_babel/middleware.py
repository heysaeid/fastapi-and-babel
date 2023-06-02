from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from fastapi.responses import Response


class Middleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next) -> Response:
        locale = request.headers.get("locale")

        if locale:
            request.app.state.babel.default_locale = locale
            
        response: Response = await call_next(request)
        return response