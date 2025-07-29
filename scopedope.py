#!/usr/bin/env python3

import argparse
import socket

def print_banner():
    banner = r"""
 ____                       ____                   
/ ___|  ___ ___  _ __   ___|  _ \  ___  _ __   ___ 
\___ \ / __/ _ \| '_ \ / _ \ | | |/ _ \| '_ \ / _ \
 ___) | (_| (_) | |_) |  __/ |_| | (_) | |_) |  __/
|____/ \___\___/| .__/ \___|____/ \___/| .__/ \___|
                |_|                    |_|         

                                                       
             ScopeDope - Subdomain Scope Checker
                       by Abir Limon
    """
    print(banner)

def load_ips(ip_file):
    with open(ip_file, "r") as f:
        ips = set(line.strip() for line in f if line.strip())
    print(f"[+] Loaded {len(ips)} valid IPs from {ip_file}")
    return ips

def resolve_to_ips(domain):
    try:
        return socket.gethostbyname_ex(domain)[2]
    except socket.gaierror:
        print(f"[!] Failed to resolve {domain}")
        return []

def main():
    print_banner()

    parser = argparse.ArgumentParser(description="ScopeDope: Match subdomains to in-scope IPs.")
    parser.add_argument("-u", "--input", required=True, help="Input subdomain file")
    parser.add_argument("-i", "--ips", required=True, help="File containing in-scope IPs")
    parser.add_argument("-o", "--output", required=True, help="Output file for matching subdomains")
    args = parser.parse_args()

    in_scope_ips = load_ips(args.ips)
    matched_subdomains = []
    total_checked = 0

    print(f"\n[+] Checking subdomains from {args.input}...\n")

    with open(args.input, "r") as sub_file:
        for line in sub_file:
            subdomain = line.strip()
            if not subdomain:
                continue
            total_checked += 1
            resolved_ips = resolve_to_ips(subdomain)
            if any(ip in in_scope_ips for ip in resolved_ips):
                print(f"[+] {subdomain} is in scope (resolves to: {', '.join(resolved_ips)})")
                matched_subdomains.append(subdomain)
            else:
                print(f"[-] {subdomain} is not in scope")

    with open(args.output, "w") as out_file:
        for sub in matched_subdomains:
            out_file.write(sub + "\n")

    print("\n================ Summary ================ ")
    print(f"[+] Total valid IPs loaded     : {len(in_scope_ips)}")
    print(f"[+] Total subdomains checked  : {total_checked}")
    print(f"[+] Subdomains in scope       : {len(matched_subdomains)}")
    print(f"[+] Output written to         : {args.output}")
    print("=========================================\n")

if __name__ == "__main__":
    main()
