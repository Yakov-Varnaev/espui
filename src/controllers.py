from uuid import UUID

from fastapi import APIRouter, Depends

from src.dependencies import (
    espanso_exporter,
    match_creator,
    match_deleter,
    match_lister,
    match_retriver,
    match_updater,
)
from src.exceptions import BadRequest
from src.models import Match
from src.services import (
    MatchCreator,
    MatchDeleter,
    MatchLister,
    MatchRetriever,
    MatchUpdater,
)
from src.services.espanso import EspansoConfigExporter

router = APIRouter(prefix="/matches")


@router.get("/export/")
def export_matches(
    force: bool = False, service: EspansoConfigExporter = Depends(espanso_exporter)
) -> None:
    try:
        service(force)
    except FileExistsError as e:
        raise BadRequest(detail=str(e))


@router.post("/")
def create_match(
    data: Match,
    service: MatchCreator = Depends(match_creator),
) -> Match:
    return service(data)


@router.get("/")
def list_matches(
    query: str | None = None,
    service: MatchLister = Depends(match_lister),
) -> list[Match]:
    return service(query)


@router.get("/{id}/")
def retrieve_match(
    id: UUID, service: MatchRetriever = Depends(match_retriver)
) -> Match:
    return service(id)


@router.put("/{id}/")
def update_match(
    id: UUID, data: Match, service: MatchUpdater = Depends(match_updater)
) -> Match:
    return service(id, data)


@router.delete("/{id}/")
def delete_match(id: UUID, service: MatchDeleter = Depends(match_deleter)) -> UUID:
    return service(id)
