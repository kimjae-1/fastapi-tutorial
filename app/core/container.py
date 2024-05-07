from dependency_injector import providers, containers

from app.core.config import Config

from app import services
from app import repositories
from app.core.redis import RedisCache


class Container(containers.DeclarativeContainer):
    config: Config = providers.Configuration()

    wiring_config = containers.WiringConfiguration(
        packages=[
            "app.core",
            "app.routers",
        ]
    )
    # redis
    redis_cache = providers.Singleton(RedisCache)
    
    # repositories
    class_repository = providers.Factory(repositories.ClassRepository)
    user_repository = providers.Factory(repositories.UserRepository)

    # services
    class_service = providers.Factory(
        services.ClassService, class_repository=class_repository
    )
    user_service = providers.Factory(
        services.UserService, user_repository=user_repository
    )
