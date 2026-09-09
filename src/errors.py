from typing import Any, Callable
from fastapi.requests import Request
from fastapi.responses import JSONResponse

class BooklyException(Exception):
    """This is the base class for all bookly errors"""
    pass

class InvalidToken(BooklyException):
    """User has provided an Invalid or expired token"""
    pass

class RevokedToken(BooklyException):
    """User has provided an Invalid or expired token"""
    pass

class AccessTokenRequired(BooklyException):
    """User has provided an Refresh token when Access token was required"""
    pass

class RefreshTokenRequired(BooklyException):
    """User has provided an Access token when Refresh token was required"""
    pass

class UserAlreadyexists(BooklyException):
    """User has provided an email for a user who already exists during sign up"""
    pass

class InvalidCredentials(BooklyException):
    """User has provided wrong email or passowrd during login"""
    pass


class InsufficientPermission(BooklyException):
    """User does not have necessary permissiopn to perform an action"""
    pass

class BookNotFound(BooklyException):
    """Book Not Found"""
    pass

class UserNotFound(BooklyException):
    """User Not Found"""
    pass

def create_exception_handler(status_code: int, initial_detail: Any) -> Callable[[Request,Exception], JSONResponse]:
    
    async def exception_handler(request: Request, exc: BooklyException):
        
        return JSONResponse(
            content= initial_detail,
            status_code= status_code
        )
        
    return exception_handler