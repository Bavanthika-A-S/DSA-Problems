class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        if divisor == 0:
            return "Cannot divide by zero"

        negative = False
        if dividend < 0:
            dividend = -dividend
            negative = not negative
        if divisor < 0:
            divisor = -divisor
            negative = not negative

        result = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

        
            while dividend >= temp + temp:
                temp = temp + temp
                multiple = multiple + multiple

            dividend = dividend - temp
            result = result + multiple

        if negative:
            return -result
        return result

