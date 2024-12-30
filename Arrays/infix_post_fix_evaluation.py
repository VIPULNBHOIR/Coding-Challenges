class Solution:
    def calculate(self, s: str):
        
        def postfix(s):
            stack = []
            string = ""
            s = s.replace( " ","")
            for char in s:
                if char == ")":
                    while stack:
                        if stack[-1] == "(":
                            stack.pop()
                            break
                        else:
                            string += stack.pop()

                elif char >= '0' and char <= "9":
                    string += char

                elif char in ("+", "-", "("):
                    if char == "(":
                        stack.append(char)

                    else:
                        while stack:
                            if stack[-1] == '(':
                                break
                            else:
                                string += stack.pop()
                                
                        stack.append(char)
            while stack:
                string += stack.pop()

            print(string)

            return evalt(string)

        def evalt(post_exp):
            stack = []
            for char in post_exp:
                if char >= '0' and char <= "9":
                    num = ord(char) - ord('0')
                    stack.append(num)

                elif char == '-':
                    if len(stack) == 1:
                        return -(stack[-1])
                    else:       
                        num1 = stack.pop()
                        num2 = stack.pop()
                        cal = (num2 - num1)
                        stack.append(cal)

                elif char == '+':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    cal = (num2 + num1)
                    stack.append(cal)
                    
            print(stack)
            return stack[0]


        return postfix(s)
                
print(Solution().calculate("(0)+(9)-(8)"))


