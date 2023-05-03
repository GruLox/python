from motherboard import Motherboard
from cpu import Processor
from gpu  import GraphicsCard
from ram import RandomAccessMemory

class Computer: 
    def __init__(self, cpu: Processor, ram: RandomAccessMemory, gpu: GraphicsCard, motherboard: Motherboard):
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu
        self.motherboard = motherboard

    def __str__(self):
        return f"CPU: {self.cpu}\nRAM: {self.ram}\nGPU: {self.gpu}\nMotherboard: {self.motherboard}"