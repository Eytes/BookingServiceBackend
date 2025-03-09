from fastapi import APIRouter


class API[Service]:
    def __init__(self, service: Service) -> None:
        self.__service = service

    @staticmethod
    def create_api_router(prefix: str, tags: list[str]) -> APIRouter:
        return APIRouter(prefix=prefix, tags=tags)
