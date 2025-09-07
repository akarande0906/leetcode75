'''
LC 93: Restore IP Addresses
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        IP_list = []
        def getIPAddress(ip_address, start):
            if len(ip_address) == 4 and start == len(s):
                IP_list.append('.'.join(ip_address))
                return
            for ip_len in range(1, 4):
                if start + ip_len <= len(s):
                    part = s[start: start + ip_len]
                    if (part[0] == '0' and len(part) > 1) or int(part) > 255:
                        continue
                    getIPAddress(ip_address + [part], start + ip_len)
        
        getIPAddress([], 0)
        return IP_list

# Time: O(3^4) = O(1)
# Space: O(1)

restoreIpAddresses = Solution().restoreIpAddresses
print (restoreIpAddresses("25525511135"))
print (restoreIpAddresses("0000"))
print (restoreIpAddresses("101023"))


    
        