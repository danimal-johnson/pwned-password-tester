# pwned-password-tester
A Python script to securely compare a password with breached password lists online.

This program is an attempt to solve the problem of determining whether or not
your password has been found on any known list of compromised passwords
without actually revealing it to anyone.

## Usage
You must have Python 3 installed on your machine to run the script. It is
available on all major platforms.

If Python is installed in its default location in Linux, you can run the
script by typing `./ppt.py`. Otherwise, you may have to run it by typing
`python3 ppt.py`.

If you're thinking of modifying the script to allow the password to be
passed as a command-line argument (i.e. `./ppt.py password1`), **don't!**
It is tempting to do so for creating an automated script, but that introduces
a serious security flaw: the plain-text password will be visible
in the command line history for all to see!

## Overview: The problem

Tl;dr: Sending your password to someone else to check is a bad idea. Checking
it yourself is too tedious.

You could go to a web site that asks you to enter your password and then
searches breached password lists for you. But that requires trusting the
web site that you are visiting. In fact, creating a site like that would
be a good way to harvest passwords and create password lists to hack into
people's accounts (please don't do this). This is what we are trying to avoid.

Complicating the problem is that compromised password lists that are
available for sale on the dark web are in plain text. There are currently
over 500 million passwords that have been breached and appear in those
lists. The lists are large and searches may take a long time. If you try
to do this from home, you will need a significant amount of disk
space and processing power and be constantly checking for new lists.

## Overview: The solution

Tl;dr: Hash your password. Send a tiny bit of it to be compared. Receive
a list of all the hashes that could match yours. Check this much shorter 
list yourself for matches.

### Advantages

* Your password is never shared with anyone.
* The list of breached passwords are never shared with you, either.
* Your password is always compared with the most up-to-date set of
breached passwords.
* You can see how many times your password has been compromised.

**Note:** Finding your password on the list does not *necessarily* mean
*your* accounts were breached, but it *does* mean that *someone* that uses
the same password as you had an account compromised.

**Another Note:** Conversely, *not* finding your password in the breached
lists doesn't necessarily mean it's a *good* password, either. It only means it
hasn't been stolen from a company in a security breach and then posted
online *in plain text*! 

## The Details

1. Your password is hashed in SHA1 format. This isn't the most secure hash,
but it doesn't need to be for this purpose.
2. The first 5 bytes of the hash are sent to api.pwnedpasswords.com.
3. You receive the subset of the 500 million compromised passwords that
could include yours, along with the number of times each appeared. Currently,
returned lists contain an average of 478 unique passwords (min 381, max 584).
4. You compare your password hash with the remaining 35 characters of
each hash you received to determine whether or not your password has been
compromised.

This is implemented with a python script. Being a script, you
can easily verify the source and know it hasn't been compiled into a
malicious program or one that is infected with a virus. It is inherently
open source.

## Other Links

* [More information on the API](https://haveibeenpwned.com/API/v2)
* [How the k-Anonymity implementation works](https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/)

Special thanks to [Troy Hunt](https://www.troyhunt.com/) for creating the API
and [Cloudflare](http://wwww.cloudflare.com) for hosting the massive amount
of data for free. 
