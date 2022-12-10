
use strict;
use warnings;


my $count = 0;

my $tot = 0;

my $x= 1;


sub cycle {
    $count += 1;
    if (($count - 20) % 40 == 0) {
        $tot += $count * $x;
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