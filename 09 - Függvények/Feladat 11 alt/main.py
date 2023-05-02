from worker import Worker
from consoleIO import getWorkers


workers: list() = getWorkers(2)

for worker in workers:
    print(worker)