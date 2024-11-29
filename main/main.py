from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.activityLog.route import router as ActivityLogRouter
from routes.badge.route import router as BadgeRouter
from routes.certificate_.route import router as CertificateRouter
from routes.course.route import router as CourseRouter
from routes.lesson.route import router as LessonRouter
from routes.personalGoal.route import router as PersonalGoalRouter
from routes.portfolio.route import router as PortfolioRouter
from routes.schedule.route import router as ScheduleRouter
from routes.user.route import router as UserRouter
from database import engine, Base

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create database tables
Base.metadata.create_all(bind=engine)

logger.info("Starting application...")

# Initialize FastAPI app
app = FastAPI(
    title="Portfolio API",
    description="API for managing user portfolios",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all routers
app.include_router(ActivityLogRouter)
app.include_router(BadgeRouter)
app.include_router(CertificateRouter)
app.include_router(CourseRouter)
app.include_router(LessonRouter)
app.include_router(PersonalGoalRouter)
app.include_router(PortfolioRouter)
app.include_router(ScheduleRouter)
app.include_router(UserRouter)

logger.info("All routers registered successfully")

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to the experaAPI",
        "docs": "/docs",
        "redoc": "/redoc"
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)