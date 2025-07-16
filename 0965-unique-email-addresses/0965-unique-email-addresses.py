class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dic={}
        for mail in emails:
            parts=mail.split("@")
            if '.' in parts[0]:
                parts[0]=parts[0].replace('.','')
            if '+' in parts[0]:
                parts[0]=parts[0].split('+')[0]
            dic[parts[0]+"@"+parts[1]]=dic.get(parts[0]+"@"+parts[1],0)+1

        return len(dic)

