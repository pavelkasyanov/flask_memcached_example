import abc
import json
from typing import List, Any

from pymemcache.client import base


class CacheRepository:
    @abc.abstractmethod
    def get_cache_seq(self, key: str) -> List[int]:
        raise NotImplemented

    @abc.abstractmethod
    def set_cache_seq(self, key: str, value: Any):
        raise NotImplemented


class MemcachedRepository(CacheRepository):
    def __init__(self, host: str, port: int):
        self._cache = base.Client((host, port))

    def get_cache_seq(self, key: str) -> List[int]:
        val = self._cache.get(key)
        return json.loads(val) if val else []

    def set_cache_seq(self, key: str, value: Any):
        result_str = json.dumps(value)
        self._cache.set(key, result_str)
