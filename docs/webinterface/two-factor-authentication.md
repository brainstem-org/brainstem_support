---
layout: default
title: Two-Factor Authentication
parent: Account and security
grand_parent: Web interface
nav_order: 2
---

# Two-Factor Authentication (2FA)
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Overview

Two-factor authentication adds a second step to signing in: a code from an authenticator app or from an email. BrainSTEM supports both, plus single-use backup tokens.

2FA is optional for most accounts. It becomes mandatory in two cases:

- Your organisation requires it. When two-factor sign-in is required for your email domain, email authentication is turned on automatically the next time you sign in, and it cannot be disabled: "Two-factor authentication is required by your organization's policy and cannot be disabled." You can still add an authenticator app and switch methods.
- You want to create an API token. Tokens can only be created once a two-factor method is set up.

## Setup

1. Open the avatar menu and choose **Security & access** → **Two-factor authentication** ([www.brainstem.org/account/two_factor/](https://www.brainstem.org/account/two_factor/)).
2. Under **Active Authentication Methods**, click **Add Authentication App** (**Add another Authentication App** once you have one) or **Activate Email Authentication**.
3. For an authenticator app, follow the **Configure Two-Factor Authentication** wizard: scan the QR code (or enter the secret key) in your app and type the 6-digit code it shows.
4. Under **Backup Tokens**, click **Generate Tokens** and store the tokens offline.

![Two-factor authentication page: an authenticator app and the Backup Tokens row under Active Authentication Methods, and the Add another Authentication App and Activate Email Authentication buttons]({{site.baseurl}}/assets/images/screenshots/two-factor-active-methods.png)
{: .screenshot }
*Two-factor authentication page with one authenticator app. Backup tokens become available after you have signed in with a second factor.*

### Authenticator apps
{: .no_toc}

Any TOTP app works, for example Google Authenticator, Microsoft Authenticator, Duo Mobile or Authy. The app shows a 6-digit code that changes every 30 seconds.

### Email codes
{: .no_toc}

With **Email Authentication** a 6-digit code is sent to your account email at sign-in. The method listed first is marked **(Default)** and is used first at sign-in; you can switch to another method on the sign-in page.

### Backup tokens
{: .no_toc}

Backup tokens are single-use codes for when you cannot reach your app or email. **View Tokens** shows the remaining tokens; **Generate Tokens** replaces them. They are removed when you remove all primary methods.

## Signing in with 2FA

1. Enter your email and password.
2. Enter the code from your default method, or choose another method or a backup token.
3. Tick **Keep me signed in** to stay signed in for 30 days from your last activity; otherwise the session ends after 12 hours.

After five failed attempts, sign-in for that account and address is blocked for one hour.

## Managing methods

- Add a new method before removing the one you rely on.
- Methods and backup tokens are managed on the same two-factor page.
- When your organisation requires 2FA, the email method stays on; you can add an app but not remove every method.

## Recovery

If you lose access to your app and email:

1. Use a backup token to sign in.
2. Add a new authenticator app or re-activate email authentication, then generate new backup tokens.

Without a backup token, contact support through the [contact form](https://brainstem.org/#Get-in-touch).

## Organisation policies and session lifetimes

Your institution can set a security policy for every account with its email domain. You see its effect at sign-in and on the two-factor page; the policy can tighten the system defaults, never loosen them:

| Setting | Meaning |
|---------|---------|
| **Two-factor sign-in** | **Required** or **Optional** |
| **Stays signed in for** | How long a **Keep me signed in** session lasts since the last activity (system default 30 days, up to 365 days) |
| **Sign-in renewed every** | How often an active session is extended |
| **Must sign in again after** | A hard limit after which you sign in again regardless of activity |

When your institution turns on email 2FA for every account of its domain, it is enabled for you at the next sign-in if you have no two-factor method yet.

## Best practices

- Prefer an authenticator app over email codes.
- Keep backup tokens offline and never share them.
- Set up a second method before you change phones.
- Review **Active sessions** in the avatar menu now and then and sign out devices you no longer use, see [User profile]({{"webinterface/user-profile/#active-sessions"|absolute_url}}).

## Related

- [User profile]({{"webinterface/user-profile/#active-sessions"|absolute_url}}): **Active sessions**, **Change password** and the **Keep me signed in** lifetimes
- [User profile: API tokens]({{"webinterface/user-profile/#api-tokens"|absolute_url}}): why a token needs a two-factor method first
- [API]({{"api/"|absolute_url}}): signing in from scripts with a personal access token or the device flow
- [Get started]({{"tutorials/get_started/"|absolute_url}}): creating your account
