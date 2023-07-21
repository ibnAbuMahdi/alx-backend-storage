import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = method.__qualname__ + ':inputs'
        outputs_key = method.__qualname__ + ':outputs'

        self._redis.rpush(inputs_key, str(args))

        output = method(self, *args, **kwargs)

        self._redis.rpush(outputs_key, str(output))

        return output
    return wrapper


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float, None]:
        if not self._redis.exists(key):
            return None

        data = self._redis.get(key)
        if fn is None:
            return data

        return fn(data)

    def get_str(self, key: str) -> Union[str, None]:
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        return self.get(key, int)


def replay(method: Callable):
    """ replay history of method calls """
    red = redis.Redis.from_url('redis://localhost:6379/0')
    inputs_key = method.__qualname__ + ':inputs'
    outputs_key = method.__qualname__ + ':outputs'

    call_count = red.llen(inputs_key)

    print(f"{method.__qualname__} was called {call_count} times:")
    input_values = red.lrange(inputs_key, 0, call_count - 1)
    output_values = red.lrange(outputs_key, 0, call_count - 1)

    for inputs, output in zip(input_values, output_values):
        inputs_str = inputs.decode()
        output_str = output.decode()
        print(f"{method.__qualname__}(*{eval(inputs_str)}) -> {output_str}")
