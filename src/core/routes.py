from fastapi import APIRouter

import views.story

router = APIRouter()
router.include_router(views.story.router)
