# 0x1A-application_server

# 2-app_server-nginx_config
Contains a nginx configuration file that, among other routes, configures the server to forward requests to /airbbnb-onepage/ to a gunicorn application server listening on port 5000.

# 3-app_server-nginx_config
In addition to the configuration in 2-app_server-nginx_config, configure the nginx server to forward requests to /airbnb-dynamic/number_odd_or_even/(\d+) and /number_odd_or_even/(\d+) to a gunicorn application server listening on port 5001.

Examples of URLs matched:
- /number_odd_or_even/9
- /airbnb-dynamic/number_odd_or_even/4
