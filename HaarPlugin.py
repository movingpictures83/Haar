def haarFWT ( signal, level ):

    s = .5;                  # scaling -- try 1 or ( .5 ** .5 )

    h = [ 1,  1 ];           # lowpass filter
    g = [ 1, -1 ];           # highpass filter        
    f = len ( h );           # length of the filter

    t = signal;              # 'workspace' array
    l = len ( t );           # length of the current signal
    y = [0] * l;             # initialise output

    t = t + [ 0, 0 ];        # padding for the workspace

    for i in range ( level ):

        y [ 0:l ] = [0] * l; # initialise the next level 
        l2 = l // 2;         # half approximation, half detail

        for j in range ( l2 ):            
            for k in range ( f ):                
                y [j]    += t [ 2*j + k ] * h [ k ] * s;
                y [j+l2] += t [ 2*j + k ] * g [ k ] * s;

        l = l2;              # continue with the approximation
        t [ 0:l ] = y [ 0:l ] ;

    return y


import PyPluMA
import PyIO

class HaarPlugin:
    def input(self, inputfile):
        self.parameters = PyIO.readParameters(inputfile)
        svaluefile = open(PyPluMA.prefix()+"/"+self.parameters["svalues"])
        self.s0 = []
        for line in svaluefile:
            self.s0.append(float(line.strip()))
        self.levels = int(self.parameters["levels"])

    def run(self):
        pass

    def output(self, outputfile):
        print("Level 0")
        print(self.s0)
        for i in range(1, self.levels):
           print("Level "+str(i))
           print(haarFWT(self.s0, i))
        
#def main():
#    s0 = [ 56, 40, 8, 24, 48, 48, 40, 16 ];
#    print( "level 0" );
#    print( s0 );
#
#    print( "level 1" );
#    print( haarFWT (s0, 1 ) );
#
#    print( "level 2" );
#    print( haarFWT (s0, 2 ) );
#
#    print( "level 3" );
#    print( haarFWT (s0, 3 ) );
#
#if __name__ == "__main__":
#    main()
# run with: >>> execfile ( "haarwavelet.py" )
