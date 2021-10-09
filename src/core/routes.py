from fastapi import APIRouter

import views.media
import views.story

router = APIRouter()
router.include_router(views.story.router)
router.include_router(views.media.router)
