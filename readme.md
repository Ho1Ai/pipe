# What pipe is

Pipe is a package manager for WaxusBS. It is simple and open-source. Everyone can take it's client side or server side code. Main purpose of WaxusBS (I named Waxus because pipe is just a package manager for Waxus, as I said) is to give people something lightweight, something that can be used by millions of people. But firstly I wanna give people a chance to move to Unix-like systems (for example, Linux (Arch Linux, Fedora Linux (even if it is still so easy also for people, who didn't use anything, that looks like Unix-like system (even macOS)), Ubuntu Linux (same story as with Fedora: it is just easy to use), Mint (same story as with Fedora and Ubuntu: it is just easy for everyone), Gentoo Linux, Debian Linux, etc.), FreeBSD, etc.). My main purpose is to create a lightweight OS, which one can be used as users want. And also I am just "escaping from reality" using this project :')

# Manual

at the moment you have to start a local server (check pipe-server repository), then you can add some packages using, for example, Postman or smth like that... well, I'm gonna write this stuff in readme.md for backend. Then you have to start venv (you can create it using "python -m venv venv"), then you have to install package "requests" (write "pip install requests"), then start `main.py`. At the moment works only -I key, so you can't use -U or -R keys. Well, let's look at example (user input goes after '>' symbol):

[main@main ~] $ python ./main.py
write a key (-I, -R, -U): > -I
write package name: > one
resolving dependencies for: one
resolving dependencies for: rustc
resolving dependencies for: GNU
resolving dependencies for: qt6
package: one
full list of installation (package and dependencies for this package): ['one', 'rustc', 'GNU', 'qt6']



it was just an example with list of dependencies for:
one: qt6, rustc
qt6: rustc, GNU
rustc: GNU

P.S.: at the moment I am just testing this stuff, so it doesn't download anything or something. It can only resolve dependencies list, no more


# What is 'install_cfg.totmb'

'install_cfg.totmb' keeps package info for installation. It has some rules: first line is ALWAYS package type line ('pkg_type' line), second line is ALWAYS package version line ('pkg_ver'/'pkg_version' line). Everything reads these things from these lines so if you want to change it you had better change next files if you need package manager, which can work: I.py (in ./keys), install.py (in ./installer) and also U.py will use these lines (since p0012 it will update everything that can be updated)
