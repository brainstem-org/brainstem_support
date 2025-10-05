---
layout: default
title: Two-Factor Authentication
parent: Web interface
nav_order: 7
---

# Two-Factor Authentication (2FA)

2FA adds an extra layer of security to your BrainSTEM account by requiring a second verification step beyond your password.

## Quick Setup (3 steps)

1. **Avatar → Two-factor authentication** (or visit `/account/two_factor/`)
2. **Choose your method:**
   - **Email** – Instant setup, receive 6-digit codes via email
   - **Authenticator app** – Scan QR code with Google Authenticator, etc.
3. **Important:** Log out and log back in using 2FA before generating backup tokens

## Method Details

### Email Verification
- **Setup:** Click **Activate Email Authentication** → Done
- **Login:** Check email from `noreply@mg.brainstem.org` for 6-digit code (5-minute expiry)
- **Good for:** Quick setup, no app required

### Authenticator Apps (TOTP)
- **Setup:** Click **Add Authentication App** → Scan QR code OR click secret key to copy → Enter 6-digit code
- **Login:** Open app, enter current 6-digit code (changes every 30 seconds)
- **Supported apps:** Google Authenticator, Microsoft Authenticator, Authy, 1Password
- **Good for:** Most secure, works offline

### Backup Tokens
- **Setup:** Requires completing at least one 2FA login first → Click **Generate Tokens** → Save securely
- **Use:** Click **Use Backup Token** at login when locked out
- **Important:** Each token works once, automatically deleted if you remove all primary methods

## Using 2FA

**Normal login:** Username/password → Enter code from your default method → Done

**Switch methods:** Click alternate method button or **Use Backup Token** at login

**Troubleshooting:**
- **Email codes expired?** Wait 1 minute before requesting new code
- **Too many attempts?** Switch to backup token or alternate method
- **Locked out?** Contact administrator after trying all recovery options

## Managing Methods

**Add/Remove:** Visit `/account/two_factor/`
- **Email:** Activate/Disable (may be restricted by organization)
- **Apps:** Add multiple, Delete individually (add new before removing old)
- **Tokens:** Generate new set anytime (requires verified 2FA session)

**Default method:** First method you enable becomes default, shown with green badge

## Security Features

| Feature | Details |
|---------|----------|
| **Email code expiry** | 5 minutes |
| **Cooldown period** | 1 minute between email requests |
| **Rate limiting** | Prevents brute-force attacks |
| **Automatic cleanup** | Backup tokens deleted when last primary method removed |

## Organization Policies

**Restricted domains** (e.g., @company.org):
- 2FA automatically enabled when you verify email
- Cannot disable 2FA completely
- Can still switch between email and authenticator apps

**Check if affected:** Try disabling all 2FA methods – if blocked by policy, your domain requires 2FA

## Best Practices

✅ **DO:**
- Use authenticator apps (more secure than email)
- Set up multiple methods for backup
- Save backup tokens securely offline
- Test new methods before removing old ones

❌ **DON'T:**
- Share backup tokens
- Rely on only one authentication method
- Ignore emails from `noreply@mg.brainstem.org`

## Need Help?

**Locked out of all methods?** Use the [contact form on the landing page](https://brainstem.org/#Get-in-touch) for assistance. Our IT team will help verify your identity and reset your access.
