from computer import Computer
from motherboard import Motherboard
from cpu import Processor
from gpu  import GraphicsCard
from ram import RandomAccessMemory

processor: Processor = Processor("Intel", "i5 9400F", 4.5, 6, 32)
ram: RandomAccessMemory = RandomAccessMemory("Kingston", 16, "DDR4", 30000)
motherboard: Motherboard = Motherboard("Gigabyte", "B450M-A", 4, 5)
gpu: GraphicsCard = GraphicsCard("Nvidia", "GTX 1660", 150000)

computer: Computer = Computer(processor, ram, motherboard, gpu)

print(computer)


