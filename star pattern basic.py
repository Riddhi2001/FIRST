WIDTH = 60
UNIT = '*'
CRLF = "\n"
SPACE = ' '

def pattern(size: int):
    return CRLF.join([leading_space(line_no) + line(line_no) for line_no in range(size)])

def line(width: int) -> str:
    return (UNIT *(2*width + 1))

def leading_space(n: int):
    return (WIDTH - n) * SPACE

print(pattern(7))
