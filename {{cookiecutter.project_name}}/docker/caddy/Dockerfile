FROM caddy:2.11.3-builder AS builder

# Add rate_limit plugin
RUN xcaddy build --with github.com/mholt/caddy-ratelimit

FROM caddy:2.11.3

# Copy custom Caddy
COPY --from=builder /usr/bin/caddy /usr/bin/caddy
