from worker import Worker
from consoleIO import *

workers: list(Worker) = getWorkers(5)

for worker in workers:
    print(worker)