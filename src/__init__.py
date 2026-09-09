from fastapi import FastAPI, status
from src.books.routes import book_router
from src.auth.routes import auth_router
from src.reviews.routes import review_router
from contextlib import asynccontextmanager
from src.db.main import init_db
from .errors import (
    create_exception_handler,
    InvalidCredentials,
    BookNotFound,
    UserAlreadyexists,
    UserNotFound,
    InsufficientPermission,
    AccessTokenRequired,
    InvalidToken,
    RefreshTokenRequired,
    RevokedToken
)

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"Server is starting ...")
    await init_db()
    yield
    print(f"Server has been stopped")

version = "v1"

app = FastAPI(
    title= "bookly",
    description= "A rest API for a book review service",
    version = version
)

app.add_exception_handler(
    UserAlreadyexists,
    create_exception_handler(
        status_code=status.HTTP_403_FORBIDDEN,
        initial_detail={
            "message": "User with email already exists",
            "error_code": "User exists"
        }
    )
)

app.add_exception_handler(
    UserNotFound,
    create_exception_handler(
        status_code=status.HTTP_404_NOT_FOUND,
        initial_detail={
            "message": "User not found",
            "error_code": "User_not_found"
        }
    )
)

app.add_exception_handler(
    InvalidCredentials,
    create_exception_handler(
        status_code=status.HTTP_400_BAD_REQUEST,
        initial_detail={
            "message": "Invalid email or password",
            "error_code": "Invalid_email_or_password"
        }
    )
)

app.add_exception_handler(
    InvalidToken,
    create_exception_handler(
        status_code=status.HTTP_403_FORBIDDEN,
        initial_detail={
            "message": "Token is invalid or expired",
            "error_code": "Invalid_token"
        }
    )
)

app.add_exception_handler(
    BookNotFound,
    create_exception_handler(
        status_code=status.HTTP_403_FORBIDDEN,
        initial_detail={
            "message": "Book Not Found",
            "error_code": "Book_not_found"
        }
    )
)

app.add_exception_handler(
    RevokedToken,
    create_exception_handler(
        status_code=status.HTTP_401_UNAUTHORIZED,
        initial_detail={
            "message": "Token is invalid or has been revoked",
            "resolution": "Please get a new token",
            "error_code": "Token_revoked"
        }
    )
)

app.add_exception_handler(
    AccessTokenRequired,
    create_exception_handler(
        status_code=status.HTTP_403_FORBIDDEN,
        initial_detail={
            "message": "Please provide a valid access token",
            "resolution": "Please get an access token",
            "error_code": "access_token_required"
        }
    )
)

app.add_exception_handler(
    RefreshTokenRequired,
    create_exception_handler(
        status_code=status.HTTP_403_FORBIDDEN,
        initial_detail={
            "message": "Please provide a valid refresh token",
            "resolution": "Please get a refresh token",
            "error_code": "refresh_token_required"
        }
    )
)

app.add_exception_handler(
    InsufficientPermission,
    create_exception_handler(
        status_code=status.HTTP_403_FORBIDDEN,
        initial_detail={
            "message": "You don't have the permission",
            "resolution": "You are not allowed to do this task",
            "error_code": "permission_not_granted"
        }
    )
)

app.include_router(book_router, prefix= f"/api/{version}/books", tags=['Book'])
app.include_router(auth_router, prefix= f"/api/{version}/auth", tags=['User'])
app.include_router(review_router, prefix= f"/api/{version}/reviews", tags=['Reviews'])