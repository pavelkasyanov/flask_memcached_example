from typing import List

from .cache_repository import CacheRepository


class MemcachedRepository(CacheRepository):
    def get_cache_seq(self) -> List[int]:
        pass
