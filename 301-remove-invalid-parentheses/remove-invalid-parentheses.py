class Solution(object):
    def removeInvalidParentheses(self, s):

        res = []

        def remove(s, last_i, last_j, pair):
            balance = 0

            for i in range(last_i, len(s)):
                if s[i] == pair[0]:
                    balance += 1
                elif s[i] == pair[1]:
                    balance -= 1

                if balance >= 0:
                    continue

                # Extra closing parenthesis
                for j in range(last_j, i + 1):
                    if s[j] == pair[1] and (j == last_j or s[j - 1] != pair[1]):
                        remove(
                            s[:j] + s[j + 1:],
                            i,
                            j,
                            pair
                        )

                return

            # No extra ')' remaining
            reversed_s = s[::-1]

            if pair[0] == '(':
                remove(reversed_s, 0, 0, (')', '('))
            else:
                res.append(reversed_s)

        remove(s, 0, 0, ('(', ')'))

        return res