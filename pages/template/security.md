# Security

Security is our first priority.
We try to make projects as secure as possible.
We use a lot of 3rd party tools to achieve that.

## Django

Django has a lot of [security-specific settings](https://docs.djangoproject.com/en/6.1/topics/security/)
that are all turned on by default in this template.

We also [enforce](production-checklist.md) all the best practices
by running `django` checks inside CI for each commit.

We also use a set of custom `django` apps
to enforce even more security rules:

- [django-axes](https://github.com/jazzband/django-axes) to track and ban repeating access requests
- [django-csp](https://github.com/mozilla/django-csp) to enforce [Content-Security Policy](https://www.w3.org/TR/CSP/) for our webpages

And there are also some awesome extensions that are not included:

- [django-honeypot](https://github.com/jamesturk/django-honeypot) - django application that provides utilities for preventing automated form spam

### Passwords

We use strong algorithms for password hashing:
`bcrypt`, `PBKDF2` and `Argon2` which are known to be secure enough.

## Dependencies

We use [poetry](https://python-poetry.org/) which ensures
that all the dependencies hashes match during the installation process.
Otherwise, the build will fail.
So, it is almost impossible to replace an already existing package
with a malicious one.

We also use [pip-audit](https://github.com/pypa/pip-audit)
to analyze dependencies for known vulnerabilities.
This check is advisory: it reports findings without blocking the build
because it can produce false positives.
Review its output before deploying to production.

```bash
pip-audit --desc
```

We also use [Github security alerts](https://help.github.com/articles/about-security-alerts-for-vulnerable-dependencies/)
for our main template repository.

## Static analysis

We use `wemake-python-styleguide` which has multiple security-based rules.
And `ruff` which includes [bandit](https://pypi.org/project/bandit/)
with security checks inside.

## Dynamic analysis

You can monitor your running application to detect anomalous activities.
Tools to consider:

- [clair](https://github.com/quay/clair) - a tool to perform static analysis of known vulnerabilities, trojans, viruses, malware & other malicious threats in docker images/containers and to monitor the docker daemon and running docker containers for detecting anomalous activities

All the tools above are not included into this template.
You have to install them by yourself.

## Secrets

We store secrets separately from code. So, it is harder for them to leak.
However, we encourage to use tools like
[truffleHog](https://github.com/dxa4481/truffleHog) or [detect-secrets](https://github.com/Yelp/detect-secrets) inside your workflow.

You can also turn on [Gitlab secrets checker](https://docs.gitlab.com/ee/user/project/repository/push_rules.html#prevent-pushing-secrets-to-the-repository) which we highly recommend.

## Audits

The only way to be sure that your app is secure
is to constantly audit it in production.

There are different tools to help you:

- [twa](https://github.com/trailofbits/twa) - tiny web auditor that has a lot of security checks for the webpages
- [XSStrike](https://github.com/s0md3v/XSStrike) - automated tool to check that your application is not vulnerable to `xss` errors
- [docker-bench](https://github.com/docker/docker-bench-security) - a script that checks for dozens of common best-practices around deploying Docker containers in production
- [lynis](https://cisofy.com/lynis/) - a battle-tested security tool for systems running Linux, macOS, or Unix-based operating system
- [trivy](https://github.com/knqyf263/trivy) - a simple and comprehensive vulnerability scanner for containers

But, even after all your attempts to secure your application,
it **won’t be 100% safe**. Do not fall into this false feeling of security.

## Further reading

- [Open Web Application Security Project](https://github.com/OWASP/ASVS)
- [Docker security](https://docs.docker.com/engine/security/security/)
- [AppArmor](https://docs.docker.com/engine/security/apparmor/) and [bane](https://github.com/genuinetools/bane)
