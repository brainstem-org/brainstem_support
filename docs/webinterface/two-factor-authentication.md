---
layout: default
title: Two-Factor Authentication
parent: Web interface
nav_order: 7
---

# Two-Factor Authentication (2FA)

2FA adds an extra layer of security by requiring a second verification step beyond your password. BrainSTEM supports email verification and authenticator apps.

## Setup & Methods

### Quick Setup
1. **Avatar → Two-factor authentication** ([www.brainstem.org/account/two_factor/](https://www.brainstem.org/account/two_factor/))
2. **Choose method:** Email (instant) or Authenticator app (scan QR code)
3. **Generate backup tokens** after completing your first 2FA login

### Email Verification
- **Setup:** Click **Activate Email Authentication**
- **Use:** Enter 6-digit code received from `noreply@mg.brainstem.org` (expires in 5 minutes)

### Authenticator Apps
- **Setup:** Click **Add Authentication App** → Scan QR code → Enter verification code
- **Use:** Enter current 6-digit code from app (refreshes every 30 seconds)
- **Apps:** Google Authenticator, Duo Mobile, Authy, or Microsoft Authenticator

### Backup Tokens
- **Generate:** After first successful 2FA login → **Generate Tokens** → Save securely
- **Use:** Click **Use Backup Token** when locked out
- **Note:** Single-use only, auto-deleted when all primary methods removed

## Usage & Management

### Login Process
1. Enter username/password
2. Enter code from default method (or click alternate method/backup token)

### Managing Methods
- **Add/Remove:** Visit [www.brainstem.org/account/two_factor/](https://www.brainstem.org/account/two_factor/)
- **Multiple apps:** Add new method before removing old
- **Default:** First enabled method (green badge)
- **Organization restrictions:** Some domains require at least one 2FA method and limit email disable

### Troubleshooting
- **Expired codes:** Wait 1 minute before requesting new email code
- **Locked out:** Try backup tokens or alternate methods first
- **Need help:** Use [contact form](https://brainstem.org/#Get-in-touch)

## Security & Best Practices

### Security Features
- **Rate limiting:** Prevents brute-force attacks
- **Time limits:** Email codes expire in 5 minutes, 1-minute cooldown between requests
- **Auto-cleanup:** Backup tokens are deleted when all primary methods are removed

### Organization Policies
Some organizations policy required 2FA and prevent complete disabling. You can still switch between email and authenticator methods.

### Best Practices
- **Recommended:** Use authenticator apps for enhanced security
- **Backup:** Set up multiple methods and save backup tokens offline
- **Safety:** Test new methods before removing old ones, never share backup tokens
