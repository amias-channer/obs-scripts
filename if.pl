#!/usr/bin/perl

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

# default returns to parameters values 
if (!$true)  { $true = $first };
if (!$false) { $false = $second };

# ids for react_dj kolanutwaffles
my @allowed_channel_ids = qw / YOUR_CHANNEL_ID_GOES_HERE /;


# Security - we require the user agent of the StreamElements Bot
if (exists $ENV{'HTTP_USER_AGENT'} && $ENV{'HTTP_USER_AGENT'} eq 'StreamElements Bot') {
        # now we are checking the header containing the channel id has one of our allowed ids
        my $channel_id = $ENV{'HTTP_X_STREAMELEMENTS_CHANNEL'};

        # no entry unless your ID is on the list
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
} elsif ($op eq ">")  {
        if ($first > $second) {
                print $true
        } else {
                # if they dont match and we dont have a supplied output for false then print nothing
                if ($false eq $second) {
                        print ""
                } else {
                        print $false
                }
        }
} elsif ($op eq "<")  {
        if ($first <  $second) {
                print $true
        } else {
                # if they dont match and we dont have a supplied output for false then print nothing
                if ($false eq $second) {
                        print ""
                } else {
                        print $false
                }
        }
} else {
        if ($first eq  $second) {
                print $true
        } else {
                # if they dont match and we dont have a supplied output for false then print nothing
                if ($false eq $second) {
                        print ""
                } else {
                        print $false
                }
        }
}
~                 
