from oops.abstraction_examples.abstraction import AbstractOperation


class AddOperation(AbstractOperation):
    def execute(self):
        return self.operand_a + self.operand_b
 
 
class SubtractOperation(AbstractOperation):
    def execute(self):
        return self.operand_a - self.operand_b
 
 
class MultiplyOperation(AbstractOperation):
    def execute(self):
        return self.operand_a * self.operand_b
 
 
class DivideOperation(AbstractOperation):
    def execute(self):
        return self.operand_a / self.operand_b


operation = AddOperation(1, 2)
print operation.execute()

operation = SubtractOperation(8, 2)
print operation.execute()

operation = MultiplyOperation(8, 2)
print operation.execute()

operation = DivideOperation(8, 2)
print operation.execute()
