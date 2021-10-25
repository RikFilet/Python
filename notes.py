#x = -2
#y = 3
#z = 1.27
#print( abs( x ) )
#print( max( x, y, z ) )
#print( min( x, y, z ) )
#print( pow( x, y ) )
#print( round( z, 1 ) )
#
#print( "Achterwaarts zijn ze {2}, {1} en {0}.".format(
#"een", "twee", "drie" ) )
#
#print( "{:5d} gedeeld door {:5d} is {:5f}".format( 1, 2, 1/2 ) )
#print( "{:<5f} gedeeld door {:^5f} is {:>5f}".format( 1 ,2 ,1/2 ))
#
print( "De eerste drie getallen zijn {:7} , {:7} en {:7}.".format(
"een", "twee", "drie" ) )
import math
print( math.sqrt( 4 ) )


from math import exp, log
print( "De waarde van e is bij benadering", exp( 1 ) )
e_sqr = exp( 2 )
print( "e kwadraat is", e_sqr , "wat betekent" )
print( "dat log(", e_sqr , ") gelijk is aan", log( e_sqr ) )