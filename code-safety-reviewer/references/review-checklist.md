# Code Safety Review Checklist

## Change Set

- Check `git status`.
- Check `git diff --stat`.
- Inspect changed files only unless dependencies require broader context.
- Identify generated files, lockfiles, config files, migration files, CI scripts, and deployment scripts.

## Secrets And Privacy

- No API keys, tokens, passwords, cookies, private keys, credentials, or signed URLs.
- No personal data in logs, fixtures, screenshots, or example docs.
- No local machine paths that reveal private user details unless intended.
- Logs redact identifiers and tokens.

## Auth And Authorization

- Authentication is required where expected.
- Authorization checks happen before side effects.
- Client-side checks are not treated as sufficient.
- Role/tenant/user scoping cannot be bypassed by changing IDs.
- Admin/debug endpoints are gated.

## Injection And Unsafe Inputs

- SQL uses parameters, not string interpolation.
- Shell commands avoid string-built command lines.
- HTML/Markdown/user content is escaped or sanitized.
- File paths are normalized and constrained to intended roots.
- URLs for fetch/proxy/webhooks are validated to avoid SSRF.
- Deserialization avoids unsafe formats or untrusted code execution.

## File And Data Safety

- Recursive delete/move operations verify resolved absolute paths.
- Writes are atomic or recoverable where needed.
- Migrations are reversible or have backup guidance.
- Bulk updates are scoped by tenant/user/project.
- Retries are idempotent.
- Partial failure behavior is defined.

## Operational Safety

- Feature flags protect risky rollout when appropriate.
- Config defaults fail safe.
- CI/deploy scripts do not expose secrets in logs.
- Error handling reports enough to debug without leaking sensitive data.
- Observability exists for critical paths.
- Rollback path is documented for risky changes.

## Tests

- Changed behavior has unit or integration tests.
- Security-sensitive paths include negative tests.
- Data migrations include representative before/after checks.
- UI changes have smoke or E2E tests when user workflows are affected.
- Bug fixes include regression tests when feasible.

## Severity Guide

- Critical: immediate exploit, data loss, credential exposure, auth bypass in production path.
- High: likely security issue or production outage risk with realistic trigger.
- Medium: plausible bug, missing guardrail, missing test around important behavior.
- Low: minor hardening, maintainability risk, unclear edge case.
