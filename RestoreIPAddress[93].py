# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

#     For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

# Example 1:

# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]

# Example 2:

# Input: s = "0000"
# Output: ["0.0.0.0"]

# Example 3:

# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

 

# Constraints:

#     1 <= s.length <= 20
#     s consists of digits only.

# Accepted
# 390.5K
# Submissions
# 828.9K
# Acceptance Rate
# 47.1%


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        print(s)
        interval,n,res_ip = '.', 1, []
        # interval_nums = range(1,len(s)+1/3)
        if s.isdigit() and 12 >= len(s) >= 4 :
            print('is_dig -supere', int(s))
            for index, num in enumerate(s): 
                print(index, num)
                if index < (len(s)+1)/3:
                    new_ip = s[0:1] + interval + s[1:2] + interval + s[2:3] + interval + s[3:4]
                    print(new_ip)
                    res_ip.append(new_ip) 
                elif index == (len(s)+1)/3:
                    new_ip = s[0] #[0:1] + interval + s[1+ index:2+index] + interval + s[2 + index:3] + interval + s[3+index:4+index]
                    print(new_ip)
        print(res_ip)
        return res_ip
list_num = "25525s11135", "25525511135","0000","101023"
for i in list_num:
    Solution.restoreIpAddresses('Succees', i)


