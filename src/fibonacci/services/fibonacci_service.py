from src.fibonacci.repositories.cache_repository import CacheRepository


class FibonacciService:
    def __init__(self, cache_repository: CacheRepository):
        self._cache_repository = cache_repository

    def get_fibonacci_seq(self, seq_start: int, seq_end: int):
        pass