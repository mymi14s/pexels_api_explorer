import os
from pexels_apis import PexelsAPI
from utils import authenticate_user, header_scheme


from fastapi import (
    Depends, FastAPI
)
from fastapi.responses import RedirectResponse

from model import (
    SearchMediaModel, PageLengthModel, MediaID, PopularVideoModel,
    CollectionModel,
)

current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
with open(parent_dir+'/README.md', 'r') as file:
    
    content = file.read()

app = FastAPI(
    title="Pexels API Explorer",
    description=content,
    summary="Photo and Video API for Pexels.com",
    version="0.0.3",
    terms_of_service="https://github.com/mymi14s/pexels_api_explorer",
    contact={
        "name": "Anthony Emmanuel",
        "url": "https://github.com/mymi14s/pexels_api_explorer",
        "email": "hackacehuawei@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)




@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

@app.post("/search-photos")
async def search_photos(item: SearchMediaModel = Depends(), auth_data: dict = Depends(authenticate_user),):
    return auth_data['pexels'].search_photos(item.dict())


@app.post("/get-curated-photos")
async def get_curated_photos(item: PageLengthModel = Depends(), auth_data: dict = Depends(authenticate_user),):
    return auth_data['pexels'].get_curated_photos(item.dict())


@app.post("/get-photo")
async def get_photo(item: MediaID = Depends(), auth_data: dict = Depends(authenticate_user),):
    return auth_data['pexels'].get_photo(item.id)


@app.post("/search-videos")
async def search_videos(item: SearchMediaModel = Depends(), auth_data: dict = Depends(authenticate_user),):
    return auth_data['pexels'].search_videos(item.dict())


@app.post("/get-popular-videos")
async def get_popular_videos(item: PopularVideoModel = Depends(), auth_data: dict = Depends(authenticate_user),):
    return auth_data['pexels'].get_popular_videos(item.dict())

@app.post("/get-video")
async def get_video(item: MediaID = Depends(), auth_data: dict = Depends(authenticate_user),):
    return auth_data['pexels'].get_video(item.id)

@app.post("/get-featured-collections")
async def get_featured_collections(item: PageLengthModel = Depends(), auth_data: dict = Depends(authenticate_user),):
    return auth_data['pexels'].get_featured_collections(item.dict())

@app.post("/get-my-collections")
async def get_my_collections(item: PageLengthModel = Depends(), auth_data: dict = Depends(authenticate_user),):
    return auth_data['pexels'].get_my_collections(item.dict())

@app.post("/get-collection-media")
async def get_collection_media(item: CollectionModel = Depends(), auth_data: dict = Depends(authenticate_user),):
    return auth_data['pexels'].get_collection_media(item.dict())
