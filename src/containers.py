from dependency_injector import containers, providers
from dependency_injector.ext import flask
from flask import Flask

from src.fibonacci.repositories.memcached_repository import MemcachedRepository


class ApplicationContainer(containers.DeclarativeContainer):
    app = flask.Application(Flask, __name__)

    cache_repository = providers.Factory(MemcachedRepository)
    fibonacci_service = providers.Factory(
        FibonacciService,
        cache_repository=cache_repository,
    )