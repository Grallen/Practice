#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Challenge: Meta-Class Magic
# Create a metaclass SingletonMeta that enforces the Singleton pattern. Any class using this metaclass can only have one instance.
#
# class Database(metaclass=SingletonMeta):
#     pass
#
# db1 = Database()
# db2 = Database()
# assert db1 is db2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Clear the console
print("\033[H\033[J", end="")


class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        print(f"Database INIT ({type(self)})")

    def __new__(cls):
        print(f"Database NEW ({type(cls)})")
        return super().__new__(cls)

print("Start")
db1 = Database()
db2 = Database()
assert db1 is db2



