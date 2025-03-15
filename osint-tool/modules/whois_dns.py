# WHOIS and DNS lookup module
import dns
import whois
from modules.utils import print_table

def start_lookup():
    domain = input("Enter domain name: ")

    print("🔍 Fetching WHOIS Data...")
    whois_info = whois.whois(domain)

    print("🔍 Resolving DNS Records...")
    dns_records = []
    for record_type in ["A", "MX", "NS", "TXT"]:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            dns_records.append([record_type, ", ".join([str(r) for r in answers])])
        except:
            dns_records.append([record_type, "No Record"])

    print_table([
        ["Domain", whois_info.domain_name],
        ["Registrar", whois_info.registrar],
        ["Creation Date", whois_info.creation_date],
        ["Expiration Date", whois_info.expiration_date]
    ], headers=["Field", "Value"])

    print_table(dns_records, headers=["DNS Record", "Value"])
    return dns_records
