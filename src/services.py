from typing import List

from src.repositories import CacheRepository
from src.utilits import fibonacci_seq


class FibonacciService:
    def __init__(self, cache_repository: CacheRepository):
        self._cache_repository = cache_repository
        self._key_value = "fib_seq"

    def get_fibonacci_seq(self, seq_start: int, seq_end: int):
        cur_fib_seq = self._cache_repository.get_cache_seq(self._key_value)

        if not cur_fib_seq or len(cur_fib_seq) < 2:
            all_seq, result_seq = self._gen_fib_seq(seq_start, seq_end)
            self._cache_repository.set_cache_seq(self._key_value, all_seq)
            return result_seq
        else:
            if seq_start not in cur_fib_seq or seq_end > cur_fib_seq[-1]:
                all_seq, _ = self._gen_fib_seq(seq_start, seq_end, cur_fib_seq[-2], cur_fib_seq[-1])
                cur_fib_seq = sorted([1] + list(set(cur_fib_seq).union(all_seq))) # need add 1 firs fibonacci number but set remove all dublicate
                self._cache_repository.set_cache_seq(self._key_value, cur_fib_seq)

            return [x for x in cur_fib_seq if seq_start <= x <= seq_end]

    @staticmethod
    def _gen_fib_seq(seq_start: int, seq_end: int, fib1: int = 0, fib2: int = 1) -> (List[int], List[int]):
        """
        :param seq_start:
        :param seq_end:
        :return: all seq and filtered seq
        """
        all_seq = []
        result_seq = []
        for value in fibonacci_seq(fib1, fib2):
            all_seq.append(value)
            if value > seq_end:
                return all_seq, result_seq

            if value >= seq_start:
                result_seq.append(value)
