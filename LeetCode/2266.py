'''
2266. Count Number of Texts

Alice is texting Bob using her phone. The mapping of digits to letters is shown
in the figure below. In order to add a letter, Alice has to press the key of
the corresponding digit i times, where i is the position of the letter in the
key.

For example, to add the letter 's', Alice has to press '7' four times.
Similarly, to add the letter 'k', Alice has to press '5' twice. Note that the
digits '0' and '1' do not map to any letters, so Alice does not use them.
However, due to an error in transmission, Bob did not receive Alice's text
message but received a string of pressed keys instead.

For example, when Alice sent the message "bob", Bob received the
string "2266622". Given a string pressedKeys representing the string received
by Bob, return the total number of possible text messages Alice could have
sent.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: pressedKeys = "22233"
Output: 8
Explanation:
The possible text messages Alice could have sent are:
"aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae", and "ce".
Since there are 8 possible messages, we return 8.
Example 2:

Input: pressedKeys = "222222222222222222222222222222222222"
Output: 82876089
Explanation:
There are 2082876103 possible text messages Alice could have sent.
Since we need to return the answer modulo 109 + 7, we return 2082876103 % (109 + 7) = 82876089.
'''
# It can be a combination of the numbers we pic. If the substring

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        OPT = [0 for i in range(1+len(pressedKeys))]
        OPT[1] = 1
        OPT[0] = 1
        for i in range(2,len(pressedKeys)+1):
            OPT[i] += OPT[i-1]
            if i-1 >0 and pressedKeys[i-1] == pressedKeys[i-2]:
                OPT[i] += OPT[i-2]
            if i-2>0 and pressedKeys[i-1]== pressedKeys[i-2] and pressedKeys[i-1] == pressedKeys[i-3]:
                OPT[i] += OPT[i-3]
            if pressedKeys[i-1] == "7" or pressedKeys[i-1] == "9":
                if i-3 >0 and pressedKeys[i-1] == pressedKeys[i-2] and pressedKeys[i-1] == pressedKeys[i-3] and pressedKeys[i-1] == pressedKeys[i-4]:
                    OPT[i] += OPT[i-4]
            OPT[i] %= (10**9 + 7)
        return OPT[-1] % (10**9 + 7)

print( "22233: ", int(Solution().countTexts("22233")) )
print( "222222222222222222222222222222222222: ", int(Solution().countTexts("222222222222222222222222222222222222")) )