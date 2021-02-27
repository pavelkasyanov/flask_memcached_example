import abc
from typing import List


class CacheRepository:
    @abc.abstractmethod
    def get_cache_seq(self) -> List[int]:
        raise NotImplemented


class MemcachedRepository(CacheRepository):
    def get_cache_seq(self) -> List[int]:
        pass
