FROM caddy:2.10.0-builder AS builder

# Add rate_limit plugin
RUN xcaddy build --with github.com/mholt/caddy-ratelimit

FROM caddy:2.10.0

# Copy custom Caddy
COPY --from=builder /usr/bin/caddy /usr/bin/caddy
