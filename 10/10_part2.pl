
use strict;
use warnings;
use Data::Dumper;


my $count = 0;

my $tot = 0;

my $x= 1;

my @frame = [];

my @a = (0...5);

for my $i (@a) {
    my @f1 = ['.', '.', '.', '.' , '.' , '.' , '.' , '.' , '.' , '.', '.', '.', '.', '.' , '.' , '.' , '.' , '.' , '.' , '.', '.', '.', '.', '.' , '.' , '.' , '.' , '.' , '.' , '.', '.', '.', '.', '.' , '.' , '.' , '.' , '.' , '.' , '.'];
    push(@frame, @f1);
}
shift @frame;

sub dumpArr {
    for my $i (@frame) {
        for my $j (@$i) {
            print $j;
        }
        print "\n"
    }
}

sub cycle {
    $count += 1;
    if (($count - 20) % 40 == 0) {
        $tot += $count * $x;
    }
    my $pos = $count-1 % 241;
    my $r = int($pos/40);
    my $c = $pos % 40;

    print $pos;
    print " ";
    print $r;
    print " ";
    print $c;
    print " ";
    print $x;
    print "\n";

    if ( $x - 1 <= $c && $x + 1 >= $c ) {
        $frame[$r][$c] = '#'
    }

}


foreach my $line ( <STDIN> ) {
    chomp( $line );
    
    if ($line eq "noop") {
        cycle();
    } 
    my @spl = split(" ", $line);
    if ($spl[0] eq "addx") {
        cycle();
        cycle();
        $x += $spl[1] + 0;
        
    }
}

print $tot;

print "\n";

dumpArr();