######################################################################
# Author: Dostonbek Toirov
# Username: toirovd
#
# Assignment: A7: UPC Bar Codes
#
# Purpose: Determine how to do some basic operations on lists
#
######################################################################
# Acknowledgements: TAs: Rusty Dotson, Tahmid Efaz
#
####################################################################################

import turtle

def valid_input(bar_code):
    '''
    Given the bar_code argument, checks and returns True if the input consists of 12 characters
    and only numbers.
    :param bar_code:
    :return:
    '''
    if len(bar_code) == 12:
        for i in bar_code:
            try:
                int(i)
            except ValueError:
                return False
            if int(i) >= 0 and int(i) <= 9:
                continue
            else:
                return False
        return True
    return False

def valid_code(b_code):
    '''
    Given b_code argument, checks and returns True if the b_code
    is a valid sequence of numbers by using the formula.
    :param b_code:
    :return:
    '''
    odd_num = 0
    even_num = 0
    last_dig = b_code[len(b_code) - 1]
    b_code = b_code[:-1]
    for i in range(len(b_code)):
        if i % 2 == 0:
            odd_num = odd_num + int(b_code[i])
        else:
            even_num = even_num + int(b_code[i])
    odd_num = odd_num * 3
    sum = even_num + odd_num
    remainder = sum % 10
    if remainder == 0:
        res = remainder
    else:
        res = 10 - remainder

    if res == int(last_dig):
        return True
    else:
        return False


def binary_num(b_code, true_or_false):
    '''
    If the bar code is valid, converts all the digits of the bar code with
    their corresponding binary numbers.
    :param b_code:
    :param true_or_false:
    :return:
    '''
    if true_or_false == True:
        dict = {
            0: "0001101",
            1: "0011001",
            2: "0010011",
            3: "0111101",
            4: "0100011",
            5: "0110001",
            6: "0101111",
            7: "0111011",
            8: "0110111",
            9: "0001011"
        }

        li = []
        for i in str(b_code):
            li.append(dict[int(i)])
        return li
    else:
        turt = turtle.Turtle()
        wn = turtle.Screen()
        turt.write("Error Message: Wrong Barcode!")
        wn.exitonclick()


def draw_bar(bin_num):
    '''
    Given the binary numbers, draws the bar.
    :param bin_num:
    :return:
    '''
    turt = turtle.Turtle()
    wn = turtle.Screen()
    turt.pensize(3)
    turt.speed(10)
    turt.penup()
    turt.setpos(-100, 100)

    # draw the beginning part of the bar code
    turt.pendown()
    turt.right(90)
    turt.forward(170)
    turt.forward(-170)
    turt.right(-90)
    turt.penup()
    turt.forward(3)

    turt.penup()
    turt.forward(3)

    turt.pendown()
    turt.right(90)
    turt.forward(170)
    turt.forward(-170)
    turt.right(-90)
    turt.penup()
    turt.forward(3)

    # draw the bar of the first digit
    for i in bin_num[0]:
        if int(i) == 0:
            turt.penup()
            turt.forward(3)
        else:
            turt.pendown()
            turt.right(90)
            turt.forward(170)
            turt.forward(-170)
            turt.right(-90)
            turt.penup()
            turt.forward(3)

    # draw the left side of the bar code
    for i in bin_num[1:6]:
        for j in i:
            if int(j) == 0:
                turt.penup()
                turt.forward(3)
            else:
                turt.pendown()
                turt.right(90)
                turt.forward(150)
                turt.forward(-150)
                turt.right(-90)
                turt.penup()
                turt.forward(3)

    # draw the middle part of the bar code
    for i in range(2):
        turt.penup()
        turt.forward(3)
        turt.pendown()
        turt.right(90)
        turt.forward(170)
        turt.forward(-170)
        turt.right(-90)
        turt.penup()
        turt.forward(3)
    turt.penup()
    turt.forward(3)

    # draw the right side of the bar code
    for i in bin_num[6:11]:
        for j in i:
            if int(j) == 1:
                turt.penup()
                turt.forward(3)
            else:
                turt.pendown()
                turt.right(90)
                turt.forward(150)
                turt.forward(-150)
                turt.right(-90)
                turt.penup()
                turt.forward(3)

    # draw the bar of the last digit
    for i in bin_num[11]:
        if int(i) == 1:
            turt.penup()
            turt.forward(3)
        else:
            turt.pendown()
            turt.right(90)
            turt.forward(170)
            turt.forward(-170)
            turt.right(-90)
            turt.penup()
            turt.forward(3)

    # draw the ending part of the bar code
    turt.pendown()
    turt.right(90)
    turt.forward(170)
    turt.forward(-170)
    turt.right(-90)
    turt.penup()
    turt.forward(3)

    turt.penup()
    turt.forward(3)

    turt.pendown()
    turt.right(90)
    turt.forward(170)
    turt.forward(-170)
    turt.right(-90)
    turt.penup()
    turt.forward(3)


    wn.exitonclick()


def main():
    # input from user
    b_code = input("Give me a barcode number: ")

    # check all are numbers; ask again if not
    while not valid_input(b_code):
        b_code = input("Give me a VALID barcode number [0-9]:")

    # check for valid UPC code
    true_or_false = valid_code(b_code)

    # convert to binary numbers
    bin_num = binary_num(b_code, true_or_false)

    # draw the bar code
    draw_bar(bin_num)


if __name__ == '__main__':
    main()
