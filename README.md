PingPerDay v3.0 by Raymond Spangle (git@leper.org)
--------------------------------------------------

![PingPerDay Main Screen Screenshot](images/capture_MainScreen.jpg?raw=true "Screen Shot")

A simple set of scripts which monitors DNS and connectivity changes daily, tracking and reporting changes via email,log files, and web.

![PingPerDay Change Tracker Screen Screenshot](images/capture_ChangeTracker.jpg?raw=true "Screen Shot")

<pre>
# Edit extras/ListSubnet to reflect the subnet(s) you'd like to list
extras/ListSubnet > IPlist.txt
# AND/OR manually edit IPlist.txt to contain only the IP addresses you wish to monitor

# Install into your web space:
mkdir /var/www/html/PingPerDay
cp -av . /var/www/html/PingPerDay
chown -R apache:apache /var/www/html/PingPerDay

# Customize your email address:
vi /var/www/html/PingPerDay/FindChanges

# Add ppd.cron to root's crontab:  
(crontab -l ; cat ppd.cron) | crontab -

# Initial run:
/var/www/html/PingPerDay/PingPerDay
# Second run to initialize differences:
/var/www/html/PingPerDay/PingPerDay

# Build the first IPCT log:
/var/www/html/PingPerDay/IPChangeTracker/BuildBigLog

</pre>
