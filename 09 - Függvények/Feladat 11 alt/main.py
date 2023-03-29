from worker import Worker
from consoleIO import *
from functions import calculateWage

workers: list(Worker) = getWorkers(5)

for worker in workers:
    print(worker)