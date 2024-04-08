class Triple:
    def init(self, op, arg1, arg2, result):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

    def str(self):
        return f"({self.op}, {self.arg1}, {self.arg2}, {self.result})"


class Quadruple:
    def init(self, op, arg1, arg2, result):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

    def str(self):
        return f"({self.op}, {self.arg1}, {self.arg2}, {self.result})"


class CodeGenerator:
    def init(self):
        self.triples = []
        self.quadruples = []

    def gen_triple(self, op, arg1, arg2, result):
        triple = Triple(op, arg1, arg2, result)
        self.triples.append(triple)

    def gen_quadruple(self, op, arg1, arg2, result):
        quadruple = Quadruple(op, arg1, arg2, result)
        self.quadruples.append(quadruple)

    def display_triples(self):
        print("Generated Triples:")
        for index, triple in enumerate(self.triples):
            print(f"T{index + 1}: {triple}")

    def display_quadruples(self):
        print("Generated Quadruples:")
        for index, quadruple in enumerate(self.quadruples):
            print(f"Q{index + 1}: {quadruple}")


def main():
    generator = CodeGenerator()

    num_statements = int(input("Enter the number of statements: "))

    for i in range(num_statements):
        op = input(f"Enter operation for statement {i+1}: ")
        arg1 = input("Enter arg1: ")
        arg2 = input("Enter arg2: ")
        result = input("Enter result: ")

        generator.gen_triple(op, arg1, arg2, result)
        generator.gen_quadruple(op, arg1, arg2, result)

    generator.display_triples()
    print()
    generator.display_quadruples()


if name == "main":
    main()
