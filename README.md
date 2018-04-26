PingPerDay v3.0 by Raymond Spangle (git@leper.org)
--------------------------------------------------

<pre>
- edit extras/ListSubnet to reflect the subnet(s) you'd like to list
- extras/ListSubnet > IPlist.txt
- AND/OR manually edit IPlist.txt to contain only the IP addresses you wish to monitor

# Install into your web space:
mkdir /var/www/html/PingPerDay
cp -av . /var/www/html/PingPerDay
chown -R apache:apache /var/www/html/PingPerDay

# Add ppd.cron to root's crontab:  
(crontab -l ; cat ppd.cron) | crontab -

# Initial run:
/var/www/html/PingPerDay/PingPerDay
# Second run to initialize differences:
/var/www/html/PingPerDay/PingPerDay

# Build the first IPCT log:
/var/www/html/PingPerDay/IPChangeTracker/BuildBigLog

</pre>
