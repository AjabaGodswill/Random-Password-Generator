import string
import random
import numbers


def pw_gen(size=32, chars=string.ascii_letters + string.punctuation + string.digits):
    return ''.join( random.choice( chars ) for _ in range( size ) )
 

print( pw_gen( int( input( 'password length:' ) ) ) )
