class Solution:
    def isHappy(self, n: int) -> bool:
        # Solved using recursion - most easiest way

        # the intuition is simple
        # - will use recursion and do the mathematics 
        # - will aintroduce a set to keep storing the outcome
        # - if that outcome is 1 then return True
        # - but if that outcome is something that already present in the set means it has a cycle, so will return False

        # set is to keep track the total we already found
        st = set()

        # recursive fn
        def getAns(num):
            total = 0
            # calculating digit's square and adding to the total
            while num:
                digit = num % 10
                total += digit * digit
                num //= 10
            # if total is 1 then return true
            if total == 1:
                return True
            # but if total encounters anything from the set that means it has a cycle
            # and will never reached to answer
            # so return false
            if total in st:
                return False
            # then adding total to the set
            # it must be after checking 1 and total present in the set or not cause otherwise total will always be inside set
            st.add(total)
            # recursive call
            return getAns(total)

        return getAns(n)