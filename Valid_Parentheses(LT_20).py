class Solution:
    def isValid(self, s: str) -> bool:
            st = []
            n = len(s)
            for i in range(n):
                if s[i] == '[' or s[i] == '{' or s[i] == '(':
                    st.append(s[i])
                else:
                    if len(st) == 0:
                        return False
                    ch = st.pop()
                    if (s[i] == ')' and ch != '(') or (s[i] == ']' and ch != '[') or (s[i] == '}' and ch != '{'):
                        return False
            return len(st) == 0