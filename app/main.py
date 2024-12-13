from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.bookings.router import router as booking_router
from app.users.router import router as users_router
from app.pages.router import router as router_pages
from app.hotels.router import router as hotels_router
from app.images.router import router as images_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(users_router)
app.include_router(booking_router)
app.include_router(hotels_router)
app.include_router(images_router)
app.include_router(router_pages)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie","Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin","Authorization"],
)

