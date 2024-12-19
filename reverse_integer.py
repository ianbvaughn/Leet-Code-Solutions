def reverse(x:int) -> int:
 unsigned_str = str(abs(x))[::-1]
 return int(unsigned_str)