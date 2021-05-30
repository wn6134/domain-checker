import argparse
import ipaddress
import os
import sys
from contextlib import contextmanager

import nslookup
import whois


@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout


def get_nameservers(domain_name):
    try:
        with suppress_stdout():
            return whois.whois(domain_name).name_servers
    except whois.parser.PywhoisError:
        return None


def get_ips(domain_name, name_servers=None):
    default_name_servers = ['8.8.8.8', '8.8.4.4', '1.1.1.1']
    if name_servers:
        dns_servers = []
        for name_server in name_servers:
            try:
                ipaddress.ip_address(name_server)
                dns_servers.append(name_server)
            except ValueError:
                dns_servers.extend(nslookup.Nslookup(dns_servers=default_name_servers).dns_lookup(name_server).answer)
    else:
        dns_servers = default_name_servers
    return nslookup.Nslookup(dns_servers=dns_servers).dns_lookup(domain_name).answer


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output_filename', help='output file name')
    args = parser.parse_args()
    f = None
    if args.output_filename:
        f = open(args.output_filename, 'w')
    for line in sys.stdin:
        domain = line.strip()
        domain_idna = line.strip().encode('idna').decode()
        print('-----')
        print('Domain:', domain)
        if domain_idna != domain:
            print('Encoded:', domain_idna)
        nameservers = get_nameservers(domain_idna)
        print('Nameservers:', ', '.join(nameservers if nameservers else ('None',)))
        ips = get_ips(domain_idna, nameservers)
        print('IP addresses:',  ', '.join(ips if ips else ('None',)))
        if f:
            f.write(
                ';'.join((
                    domain,
                    ','.join(nameservers if nameservers else ('None',)),
                    ','.join(ips if ips else ('None',))
                )) + '\n'
            )
    if f:
        f.close()
