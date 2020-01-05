from src.ops2 import *

class IntcodeComputer:
    def __init__(self, instructions):
        self.memory = instructions

    def run(self):
        num_instructions = len(self.memory) // 4
        for i in range(num_instructions):
            instruction = self.memory[i*4:(i+1)*4]
            try:
                self.exec(instruction)
            except HaltException:
                break
        return self.memory

    def exec(self, instruction):
        op = instruction[0]
        if op in ops.keys():
            if op == HALT_CODE:
                raise HaltException
            arg1_loc, arg2_loc, out_loc = instruction[1:]
            arg1, arg2 = map(self.mem_load, (arg1_loc, arg2_loc))
            out = ops[op](arg1, arg2)
        else:
            raise InvalidOpException
        self.mem_store(out_loc, out)

    def mem_load(self, mem_loc):
        return self.memory[mem_loc]

    def mem_store(self, mem_loc, value):
        self.memory[mem_loc] = value

