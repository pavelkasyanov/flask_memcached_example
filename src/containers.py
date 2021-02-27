from dependency_injector import containers, providers

from src.repositories import MemcachedRepository
from src.services import FibonacciService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    cache_repository = providers.Singleton(MemcachedRepository,
                                           host=config.cache.host,
                                           port=config.cache.port)

    fibonacci_service = providers.Factory(
        FibonacciService,
        cache_repository=cache_repository,
    )