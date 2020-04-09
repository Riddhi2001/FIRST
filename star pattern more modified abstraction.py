#width of screen
WIDTH = 60

SHARP, MINUS, STAR = "#","_","*"

CRLF, BS = "\n", "\b"

SPACE = " "


#starting pattern
SP = SHARP
#repeating patter
RP = STAR
#end pattern
EP = SHARP


#to print the frame of the pattern consisting of loop
def pattern(size: int, screen_width: int):

    return CRLF.join(line(line_no, screen_width) for line_no in range(size))


#each line of pattern
def line(n: int, width: int):
    
    return leading_space(n, width) + start_pattern(n) + repeat_pattern(n) + end_pattern(n)



def leading_space(n: int, width: int) -> str:
    
    return SPACE * (width//2 - n)



def start_pattern(n: int) -> str:
    return SP



def repeat_pattern(n: int):
    return n * RP * 2



def end_pattern(n: int):

    return EP



print(pattern(7,60))
