from abc import ABCMeta, abstractmethod


class AbstractOperation:
    __metaclass__ = ABCMeta

    def __init__(self, operand_a, operand_b):
        self.operand_a = operand_a
        self.operand_b = operand_b
        super(AbstractOperation, self).__init__()
    
    @abstractmethod
    def execute(self):
        pass
