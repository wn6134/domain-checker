# domain-checker
Collects nameservers and IP addresses for provided list of domains.

Requirements: 
   * python3
   * python packages: 
     * nslookup 
     * python-whois
       
To install python packages execute:
```
pip3 install nslookup python-whois
```

Prepare a file with a list of domains.

Run script:
```
domain-checker.py -o out.csv < domains.txt
```

STDOUT example:
```
-----
Domain: google.com
Nameservers: NS1.GOOGLE.COM, NS2.GOOGLE.COM, NS3.GOOGLE.COM, NS4.GOOGLE.COM, ns4.google.com, ns3.google.com, ns1.google.com, ns2.google.com
IP addresses: 64.233.162.138, 64.233.162.101, 64.233.162.102, 64.233.162.100, 64.233.162.113, 64.233.162.139
-----
Domain: youtube.com
Nameservers: NS1.GOOGLE.COM, NS2.GOOGLE.COM, NS3.GOOGLE.COM, NS4.GOOGLE.COM, ns2.google.com, ns4.google.com, ns1.google.com, ns3.google.com
IP addresses: 173.194.222.91, 173.194.222.93, 173.194.222.190, 173.194.222.136
-----
Domain: instagram.com
Nameservers: NS-1349.AWSDNS-40.ORG, NS-2016.AWSDNS-60.CO.UK, NS-384.AWSDNS-48.COM, NS-868.AWSDNS-44.NET
IP addresses: 54.208.215.118, 3.210.178.0, 3.215.47.155, 3.218.251.107, 54.210.252.14, 52.21.48.38, 54.208.155.193, 3.208.4.201
-----
Domain: facebook.com
Nameservers: A.NS.FACEBOOK.COM, B.NS.FACEBOOK.COM, C.NS.FACEBOOK.COM, D.NS.FACEBOOK.COM
IP addresses: 157.240.205.35
```
out.csv:
```
google.com;NS1.GOOGLE.COM,NS2.GOOGLE.COM,NS3.GOOGLE.COM,NS4.GOOGLE.COM,ns4.google.com,ns3.google.com,ns1.google.com,ns2.google.com;64.233.162.138,64.233.162.101,64.233.162.102,64.233.162.100,64.233.162.113,64.233.162.139
youtube.com;NS1.GOOGLE.COM,NS2.GOOGLE.COM,NS3.GOOGLE.COM,NS4.GOOGLE.COM,ns2.google.com,ns4.google.com,ns1.google.com,ns3.google.com;173.194.222.91,173.194.222.93,173.194.222.190,173.194.222.136
instagram.com;NS-1349.AWSDNS-40.ORG,NS-2016.AWSDNS-60.CO.UK,NS-384.AWSDNS-48.COM,NS-868.AWSDNS-44.NET;54.208.215.118,3.210.178.0,3.215.47.155,3.218.251.107,54.210.252.14,52.21.48.38,54.208.155.193,3.208.4.201
facebook.com;A.NS.FACEBOOK.COM,B.NS.FACEBOOK.COM,C.NS.FACEBOOK.COM,D.NS.FACEBOOK.COM;157.240.205.35
```