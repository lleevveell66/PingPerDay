#!/usr/bin/perl

use CGI;

$q=CGI->new;

$IP=$q->param('IPAddr');

print $q->header;
print $q->start_html(-title=>"IP History for $IP (since 04/15/15)",-BGCOLOR=>'white');

print <<EOT;
<font face="verdana" size="3">
IP History for $IP (since 04/15/15):
</font>
<pre>
EOT

$output=`grep '$IP,' logs/ChangeTracker.log`;

print $output;

print "</pre>\n";

print $q->end_html;

exit(0);
