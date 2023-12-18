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

## 1-haproxy_ssl_termination
Create a certificate using `certbot` and configure HAproxy to accept encrypted traffic (using SSL offloading) for the `www` subdomain. The file `1-haproxy_ssl_termination` represents the HAproxy config file found on the laod balancer server.

**NOTE**: during the certbot configuration, the `fullchain.pem` and `privkey.pem` files were merged into one file called `/etc/haproxy/certs/www.peterndungu.tech.pem`, which is referenced in the HAproxy config file. Since the SSL certificate is renewed regularly, the combined file needs to be recreated each time the SSL certificate is renewed.

Requirements:
- HAproxy must be listening on port TCP 443
- HAproxy must be accepting SSL traffic

## 100-redirect_http_to_https
Configure HAproxy to automatically redirect HTTP traffic to HTTPS:
- HAproxy should return a `301`
- HAproxy should redirect HTTP traffic to HTTPS
