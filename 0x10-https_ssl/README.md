# 0x10-https_ssl
Configure SSL Termination on a cluster of servers

## 0x10-https_ssl
The server is configured as follows:
- Add the subdomain `www` to the domain, point it to your `lb-01` IP
- Add the subdomain `lb-01` to the domain, point it to the `lb-01` IP
- Add the subdomain `web-01` to the domain, point it to the `web-01` IP
- Add the subdomain `web-02` to the domain, point it to the `web-02` IP

Write a bash script `0x10-https_ssl` that accepts two arguments:
- `domain`:
    type: string
    what: domain name to audit
    mandatory: yes
- `subdomain`:
    type: string
    what: specific subdomain to audit
    mandatory: no

- Output: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]`
- When only the parameter `domain` is provided, display information for its subdomains `www`, `lb-01`, `web-01` and `web-02` - in this order
- When passing domain and subdomain parameters, display information for the specified subdomain
- `awk` is used to format the outputs
