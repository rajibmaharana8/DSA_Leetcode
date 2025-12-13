import re

class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        category_order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        
        valid = []
        
        for c, b, a in zip(code, businessLine, isActive):
            if a and c and re.match(r'^[A-Za-z0-9_]+$', c) and b in category_order:
                valid.append((c, b))
        
        valid.sort(key=lambda x: (category_order[x[1]], x[0]))
        
        return [c for c, _ in valid]