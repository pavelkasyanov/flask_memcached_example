
from dependency_injector import containers, providers

from src.repositories import MemcachedRepository
from src.services import FibonacciService


class Container(containers.DeclarativeContainer):

    cache_repository = providers.Factory(MemcachedRepository)

    fibonacci_service = providers.Factory(
        FibonacciService,
        cache_repository=cache_repository,
    )