#-------------------------------------------------------------------------------
# Name:        turtle_user_input.py
# Purpose: This module handles all the keystroke listening for listening for user
#    input on the Turtle screen. It handles only the basic letters (Upper and
#    lower) as well as numbers. It also enables backspace deletions.
#
# Author:   Bridget O'Daniel, odanielb
#
# Acknowledgements: This module is heavily based upon and edited from the
#    fraction_window_listener.py module by Dr. Mario Nakazawa from here:
#    http://cs.berea.edu/courses/csc226/tasks/fraction_window_listener.py
# ------------------------------------------------------------------------------

import turtle

class Input_String:

    def __init__( self, x_pos=-120, y_pos=0 ):
        self.string = ""                                                        #This string will house the built up string of user input
        self.writing = True                                                     #This tells if a string can currently be added

        self.scribe = turtle.Turtle()                                           #This Turtle will write it on the screen
        turtle.colormode(255)
        self.scribe.color(71, 230, 163)
        self.scribe.hideturtle()
        self.scribe.penup()
        self.scribe.setpos( x_pos, y_pos )
        self.scribe.write(self.string, False, "center",font=("Century Gothic",30,("bold","normal")))

    def update_turtle(self):
        """When characters are being added to the string, it appears on the screen
        when this turtle object is updated."""
        self.scribe.clear()
        self.scribe.write(self.string, False, "center", font=("Century Gothic",30,("bold","normal")))

    def get_string(self):
        """Returns the string that the user has built up at this point.
        post: Returns a string object."""
        return self.string

    #---------------------------------------------------------------------
    #   These next functions "BUILD" the input from the keyboard
    #   into a attribute called "string".
    #   The object allows users to type a period (".") to get clear the
    #   number string, and it records all the digits the user inputs.
    #---------------------------------------------------------------------
    def clear_string( self ):
        """Clears the string."""
        self.string = ""
        self.scribe.clear()

    def finish_string( self ):
        """Submits the string as it is currently built."""
        self.writing = False

    def delete_char( self ):
        """This method catches the backspace key and removes the last character
        in the string it is building."""
        new_string = ""
        index=0
        while(index < len(self.string)-1):
            new_string += self.string[index]
            index = index + 1
        self.string = new_string
        self.update_turtle()

    def add_zero( self ):
        self.string += "0"
        self.update_turtle()
    def add_one( self ):
        self.string += "1"
        self.update_turtle()
    def add_two( self ):
        self.string += "2"
        self.update_turtle()
    def add_three( self ):
        self.string += "3"
        self.update_turtle()
    def add_four( self ):
        self.string += "4"
        self.update_turtle()
    def add_five( self ):
        self.string += "5"
        self.update_turtle()
    def add_six( self ):
        self.string += "6"
        self.update_turtle()
    def add_seven( self ):
        self.string += "7"
        self.update_turtle()
    def add_eight( self ):
        self.string += "8"
        self.update_turtle()
    def add_nine( self ):
        self.string += "9"
        self.update_turtle()
    def add_A( self ):
        self.string += "A"
        self.update_turtle()
    def add_a( self ):
        self.string += "a"
        self.update_turtle()
    def add_B( self ):
        self.string += "B"
        self.update_turtle()
    def add_b( self ):
        self.string += "b"
        self.update_turtle()
    def add_C( self ):
        self.string += "C"
        self.update_turtle()
    def add_c( self ):
        self.string += "c"
        self.update_turtle()
    def add_D( self ):
        self.string += "D"
        self.update_turtle()
    def add_d( self ):
        self.string += "d"
        self.update_turtle()
    def add_E( self ):
        self.string += "E"
        self.update_turtle()
    def add_e( self ):
        self.string += "e"
        self.update_turtle()
    def add_F( self ):
        self.string += "F"
        self.update_turtle()
    def add_f( self ):
        self.string += "f"
        self.update_turtle()
    def add_G( self ):
        self.string += "G"
        self.update_turtle()
    def add_g( self ):
        self.string += "g"
        self.update_turtle()
    def add_H( self ):
        self.string += "H"
        self.update_turtle()
    def add_h( self ):
        self.string += "h"
        self.update_turtle()
    def add_I( self ):
        self.string += "I"
        self.update_turtle()
    def add_i( self ):
        self.string += "i"
        self.update_turtle()
    def add_J( self ):
        self.string += "J"
        self.update_turtle()
    def add_j( self ):
        self.string += "j"
        self.update_turtle()
    def add_K( self ):
        self.string += "K"
        self.update_turtle()
    def add_k( self ):
        self.string += "k"
        self.update_turtle()
    def add_L( self ):
        self.string += "L"
        self.update_turtle()
    def add_l( self ):
        self.string += "l"
        self.update_turtle()
    def add_M( self ):
        self.string += "M"
        self.update_turtle()
    def add_m( self ):
        self.string += "m"
        self.update_turtle()
    def add_N( self ):
        self.string += "N"
        self.update_turtle()
    def add_n( self ):
        self.string += "n"
        self.update_turtle()
    def add_O( self ):
        self.string += "O"
        self.update_turtle()
    def add_o( self ):
        self.string += "o"
        self.update_turtle()
    def add_P( self ):
        self.string += "P"
        self.update_turtle()
    def add_p( self ):
        self.string += "p"
        self.update_turtle()
    def add_Q( self ):
        self.string += "Q"
        self.update_turtle()
    def add_q( self ):
        self.string += "q"
        self.update_turtle()
    def add_R( self ):
        self.string += "R"
        self.update_turtle()
    def add_r( self ):
        self.string += "r"
        self.update_turtle()
    def add_S( self ):
        self.string += "S"
        self.update_turtle()
    def add_s( self ):
        self.string += "s"
        self.update_turtle()
    def add_T( self ):
        self.string += "T"
        self.update_turtle()
    def add_t( self ):
        self.string += "t"
        self.update_turtle()
    def add_U( self ):
        self.string += "U"
        self.update_turtle()
    def add_u( self ):
        self.string += "u"
        self.update_turtle()
    def add_V( self ):
        self.string += "V"
        self.update_turtle()
    def add_v( self ):
        self.string += "v"
        self.update_turtle()
    def add_W( self ):
        self.string += "W"
        self.update_turtle()
    def add_w( self ):
        self.string += "w"
        self.update_turtle()
    def add_X( self ):
        self.string += "X"
        self.update_turtle()
    def add_x( self ):
        self.string += "x"
        self.update_turtle()
    def add_Y( self ):
        self.string += "Y"
        self.update_turtle()
    def add_y( self ):
        self.string += "y"
        self.update_turtle()
    def add_Z( self ):
        self.string += "Z"
        self.update_turtle()
    def add_z( self ):
        self.string += "z"
        self.update_turtle()

#Where the number is placed
input_string = Input_String(0,0)

def clear_string():
    input_string.clear_string()
def finish_string():
    input_string.finish_string()
def delete_a_char():
    input_string.delete_char()
def get_zer():
    input_string.add_zero()
def get_one():
    input_string.add_one()
def get_two():
    input_string.add_two()
def get_thr():
    input_string.add_three()
def get_fou():
    input_string.add_four()
def get_fiv():
    input_string.add_five()
def get_six():
    input_string.add_six()
def get_sev():
    input_string.add_seven()
def get_eig():
    input_string.add_eight()
def get_nin():
    input_string.add_nine()
def get_A():
    input_string.add_A()
def get_B():
    input_string.add_B()
def get_C():
    input_string.add_C()
def get_D():
    input_string.add_D()
def get_E():
    input_string.add_E()
def get_F():
    input_string.add_F()
def get_G():
    input_string.add_G()
def get_H():
    input_string.add_H()
def get_I():
    input_string.add_I()
def get_J():
    input_string.add_J()
def get_K():
    input_string.add_K()
def get_L():
    input_string.add_L()
def get_M():
    input_string.add_M()
def get_N():
    input_string.add_N()
def get_O():
    input_string.add_O()
def get_P():
    input_string.add_P()
def get_Q():
    input_string.add_Q()
def get_R():
    input_string.add_R()
def get_S():
    input_string.add_S()
def get_T():
    input_string.add_T()
def get_U():
    input_string.add_U()
def get_V():
    input_string.add_V()
def get_W():
    input_string.add_W()
def get_X():
    input_string.add_X()
def get_Y():
    input_string.add_Y()
def get_Z():
    input_string.add_Z()
def get_a():
    input_string.add_a()
def get_b():
    input_string.add_b()
def get_c():
    input_string.add_c()
def get_d():
    input_string.add_d()
def get_e():
    input_string.add_e()
def get_f():
    input_string.add_f()
def get_g():
    input_string.add_g()
def get_h():
    input_string.add_h()
def get_i():
    input_string.add_i()
def get_j():
    input_string.add_j()
def get_k():
    input_string.add_k()
def get_l():
    input_string.add_l()
def get_m():
    input_string.add_m()
def get_n():
    input_string.add_n()
def get_o():
    input_string.add_o()
def get_p():
    input_string.add_p()
def get_q():
    input_string.add_q()
def get_r():
    input_string.add_r()
def get_s():
    input_string.add_s()
def get_t():
    input_string.add_t()
def get_u():
    input_string.add_u()
def get_v():
    input_string.add_v()
def get_w():
    input_string.add_w()
def get_x():
    input_string.add_x()
def get_y():
    input_string.add_y()
def get_z():
    input_string.add_z()


def set_up_window( win ):
    """This function sets up the window to listen for characters and builds the
    string as the user types the characters. The Enter button resets the string
    to blank."""
    win.onkey(clear_string, '.')
    win.onkey(finish_string, 'Return')
    win.onkey(delete_a_char, "BackSpace")
    win.onkey(get_zer, '0')
    win.onkey(get_one, '1')
    win.onkey(get_two, '2')
    win.onkey(get_thr, '3')
    win.onkey(get_fou, '4')
    win.onkey(get_fiv, '5')
    win.onkey(get_six, '6')
    win.onkey(get_sev, '7')
    win.onkey(get_eig, '8')
    win.onkey(get_nin, '9')
    win.onkey(get_A, 'A')
    win.onkey(get_B, 'B')
    win.onkey(get_C, 'C')
    win.onkey(get_D, 'D')
    win.onkey(get_E, 'E')
    win.onkey(get_F, 'F')
    win.onkey(get_G, 'G')
    win.onkey(get_H, 'H')
    win.onkey(get_I, 'I')
    win.onkey(get_J, 'J')
    win.onkey(get_K, 'K')
    win.onkey(get_L, 'L')
    win.onkey(get_M, 'M')
    win.onkey(get_N, 'N')
    win.onkey(get_O, 'O')
    win.onkey(get_P, 'P')
    win.onkey(get_Q, 'Q')
    win.onkey(get_R, 'R')
    win.onkey(get_S, 'S')
    win.onkey(get_T, 'T')
    win.onkey(get_U, 'U')
    win.onkey(get_V, 'V')
    win.onkey(get_W, 'W')
    win.onkey(get_X, 'X')
    win.onkey(get_Y, 'Y')
    win.onkey(get_Z, 'Z')
    win.onkey(get_a, 'a')
    win.onkey(get_b, 'b')
    win.onkey(get_c, 'c')
    win.onkey(get_d, 'd')
    win.onkey(get_e, 'e')
    win.onkey(get_f, 'f')
    win.onkey(get_g, 'g')
    win.onkey(get_h, 'h')
    win.onkey(get_i, 'i')
    win.onkey(get_j, 'j')
    win.onkey(get_k, 'k')
    win.onkey(get_l, 'l')
    win.onkey(get_m, 'm')
    win.onkey(get_n, 'n')
    win.onkey(get_o, 'o')
    win.onkey(get_p, 'p')
    win.onkey(get_q, 'q')
    win.onkey(get_r, 'r')
    win.onkey(get_s, 's')
    win.onkey(get_t, 't')
    win.onkey(get_u, 'u')
    win.onkey(get_v, 'v')
    win.onkey(get_w, 'w')
    win.onkey(get_x, 'x')
    win.onkey(get_y, 'y')
    win.onkey(get_z, 'z')


def unbind_keys(win):
    """This function unbinds the 0-9 and A-z keys from whatever function they
    were set to call on click previously in the provided Turtle window."""
    win.onkey(None, 'Return')
    win.onkey(None, '.')
    win.onkey(None, "BackSpace")
    win.onkey(None, '0')
    win.onkey(None, '1')
    win.onkey(None, '2')
    win.onkey(None, '3')
    win.onkey(None, '4')
    win.onkey(None, '5')
    win.onkey(None, '6')
    win.onkey(None, '7')
    win.onkey(None, '8')
    win.onkey(None, '9')
    win.onkey(None, 'A')
    win.onkey(None, 'B')
    win.onkey(None, 'C')
    win.onkey(None, 'D')
    win.onkey(None, 'E')
    win.onkey(None, 'F')
    win.onkey(None, 'G')
    win.onkey(None, 'H')
    win.onkey(None, 'I')
    win.onkey(None, 'J')
    win.onkey(None, 'K')
    win.onkey(None, 'L')
    win.onkey(None, 'M')
    win.onkey(None, 'N')
    win.onkey(None, 'O')
    win.onkey(None, 'P')
    win.onkey(None, 'Q')
    win.onkey(None, 'R')
    win.onkey(None, 'S')
    win.onkey(None, 'T')
    win.onkey(None, 'U')
    win.onkey(None, 'V')
    win.onkey(None, 'W')
    win.onkey(None, 'X')
    win.onkey(None, 'Y')
    win.onkey(None, 'Z')
    win.onkey(None, 'a')
    win.onkey(None, 'b')
    win.onkey(None, 'c')
    win.onkey(None, 'd')
    win.onkey(None, 'e')
    win.onkey(None, 'f')
    win.onkey(None, 'g')
    win.onkey(None, 'h')
    win.onkey(None, 'i')
    win.onkey(None, 'j')
    win.onkey(None, 'k')
    win.onkey(None, 'l')
    win.onkey(None, 'm')
    win.onkey(None, 'n')
    win.onkey(None, 'o')
    win.onkey(None, 'p')
    win.onkey(None, 'q')
    win.onkey(None, 'r')
    win.onkey(None, 's')
    win.onkey(None, 't')
    win.onkey(None, 'u')
    win.onkey(None, 'v')
    win.onkey(None, 'w')
    win.onkey(None, 'x')
    win.onkey(None, 'y')
    win.onkey(None, 'z')
