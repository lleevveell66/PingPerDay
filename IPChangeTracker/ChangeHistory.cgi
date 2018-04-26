#!/usr/bin/perl

use CGI;

my $q=new CGI;

$ip2show=$q->param('IP');

print $q->header;

print $q->start_html(-title=>'IP Change Tracker - $ip2show');

print <<ENDHTML;
<center><img src="images/ipct_logo.png" width="75%"></center>
<hr>

<form action="ChangeHistory.cgi" method="post">

<center><table cellpadding="3" cellspacing="3" border="1" width="50%">
<tr><th>IP to see change history for:</th></tr>
<tr><td>
<center>
<input type="text" name="IP" value="$ip2show"><input type="submit" value="Check!">
</center>

</td></tr>
</table></center>

<hr>

</form>
ENDHTML

print "<b>IP:</b> = $ip2show<br><br>\n";

$output=`/usr/bin/tac biglog.log | /bin/grep ",$ip2show,"`;

print "<b>CHANGES:</b><br><br>\n";
print "<pre>$output</pre>\n";

print "<b>EXPLAINATION:</b><br><br>\n";
(@lines)=split(/\n/,$output);

$red="<font color='#FF0000'>";
$green="<font color='#009900'>";
$blue="<font color='#0000FF'>";
$black="</font>";


foreach $line (@lines)
{
 ($date,$time,$ip1,$hostname1,$pingable1,$ip2,$hostname2,$pingable2)=split(/,/,$line);

 $hostname1=~s/.vzbi.com//;
 $hostname2=~s/.vzbi.com//;

 if($hostname1 ne $hostname2) 
  { print "On $date the hostname changed from <b>$hostname1</b> to $blue<b>$hostname2</b>$black<br>\n"; }
 if($pingable1 ne $pingable2)
  { if($pingable1 eq 'YES') { print "On $date the IP went from up to $red<b>DOWN</b>$black<br>\n" } 
     else { print "On $date the IP went from down to $green<b>UP</b>$black<br>\n"; } }

}

print $q->end_html;

exit(0);
