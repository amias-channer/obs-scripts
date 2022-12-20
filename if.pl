#!/usr/bin/perl
#

use CGI qw/ param header /;
use POSIX qw(strftime);

my $q=CGI->new;

# the parameters to compare
my $first   = $q->param('a');
my $second  = $q->param('b');

# the operation to perform
my $op      = $q->param('o');

# the results to return
my $true    = $q->param('t');
my $false   = $q->param('f');

# default returns to 1 or 0 
if (!$true)  { $true = 1 };
if (!$false) { $false = 0 };

my @allowed_channel_ids = qw / YOUR-CHANNEL-ID-GOES-HERE-OR-YOU-GET-NO-RESPONSE /;


if (exists $ENV{'HTTP_USER_AGENT'} && $ENV{'HTTP_USER_AGENT'} eq 'StreamElements Bot') {
        my $channel_id = $ENV{'HTTP_X_STREAMELEMENTS_CHANNEL'};
        my $auth = false;
        if  (grep($channel_id,@allowed_channel_ids)) { $auth = true };
        unless ($auth) { exit };
} else {
        exit
}

# print headers using every trick in the book to disable caching of output
print header(
    -type => 'text/plain',
   # date in the past
    -expires       => 'Sat, 26 Jul 1997 05:00:00 GMT',
    # always modified
    -Last_Modified => strftime('%a, %d %b %Y %H:%M:%S GMT', gmtime),
    # HTTP/1.0
    -Pragma        => 'no-cache',
    # HTTP/1.1 + IE-specific (pre|post)-check
    -Cache_Control => join(', ', qw(
        private
        no-cache
        no-store
        must-revalidate
        max-age=0
        pre-check=0
        post-check=0
    )),);

# choose an operation and do it
if ($op eq "or")  {
        if ($first or  $second) {
                print $true
        } else {
                print $false
        }
} elsif ($op eq "and") {
        if ($first and $second) {
                print $true
        } else {
                print $false
        }
} elsif ($op eq "ne")  {
        if ($first ne  $second) {
                print $true
        } else {
                print $false
        }
} else {
        if ($first eq  $second) {
                print $true
        } else {
                print $false
        }
}
~               
