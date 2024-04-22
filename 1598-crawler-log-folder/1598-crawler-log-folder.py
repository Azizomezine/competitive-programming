class Solution:
    def minOperations(self, logs: List[str]) -> int:
        our_stack = []
        for i in range(len(logs)):
            if logs[i] == "../":
                if len(our_stack) == 0:
                    continue
                else:
                    our_stack.pop()
            elif logs[i] == "./":
                continue

            else:
                our_stack.append(logs[i])


        return len(our_stack)

        

