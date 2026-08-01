class Solution:
    def ops(self,x,y,op):
        if op == '+':
            return x+y
        elif op == '-':
            return x-y
        elif op == '*':
            return x*y
        elif op == '/':
            return int(x/y)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in '+*-/':
                a=stack.pop()
                b=stack.pop()

                r=self.ops(b,a,i)
                stack.append(r)
            else:
                stack.append(int(i))

        return stack[0]
