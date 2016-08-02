/usr/local/bin/nova-api & echo $! >/opt/stack/status/stack/n-api.pid; fg || echo "n-api failed to start" | tee "/opt/stack/status/stack/n-api.failure"

