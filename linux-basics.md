# Linux Basics for Hackers - Reference Guide

**Hacking is the most important skill set of the 21st century!**

- **Ethical hacking** is the practice of attempting to infiltrate and exploit a system in order to find out its weaknesses and better secure it.
- A **penetration test** is essentially a legal, commissioned hack to demonstrate the vulnerability of a firm's network and systems.

## Why Linux?
- ✅ Open source: The source code is available to change and manipulate as needed.
- 🔍 Transparent: All working parts are visible and can be manipulated.
- 🎛️ Granular control: Everything can be controlled by the terminal at the most macro level. Scripting is simple and effective.
- 🛠️ Most hacking tools are written for Linux.
- 🚀 The future belongs to Linux/Unix.

---

## Chapter 1: Getting started with the basics

### Introductory terms and concepts
- **Binaries**: Executable files, reside in the `/usr/bin` or `/usr/sbin` directories, include utilities such as *ps, cat, ls* and *cd*, and applications.
- **Case Sensitivity**: `Desktop` ≠ `desktop` ≠ `DeskTop`.
- **Directory**: Provides files organization in a hierarchical manner.
- **Home Directory**: `/home/username` (default save location for user files).
- **Kali Linux**: Purpose-built for penetration testing (pre-loaded with hacking tools).
- **root**: Superuser/admin account.
- **Script**: A file containing commands (bash, Python, etc.).
- **Shell**: Command interpreter. Bash (*Bourne-again shell*), C shell and Z shell.
- **Terminal**: Command-line interface (CLI).

### The Linux filesystem
At the very top of the filesystem structure is `/`, which is often referred to as the root of the filesystem.
![image 7TZC82](https://github.com/user-attachments/assets/a255003f-5e0b-476f-b35e-ce236f5a3ae6)
- **/root**: The home directory of the all-powerful root user  
- **/etc**: Generally contains the Linux configuration files  
- **/home**: The user's home directory  
- **/mnt**: Where other filesystems are attached or mounted  
- **/media**: For CDs and USB devices  
- **/bin**: Application binaries  
- **/lib**: System libraries  

### Basic Commands

| Command       | Description                                  |
|---------------|----------------------------------------------|
| `pwd`         | Print working directory                     |
| `whoami`      | Show current user                           |
| `cd /path`    | Change directory                            |
| `cd ..`       | Move up one level                           |
| `cd /`        | Jump to root directory                      |
| `ls`          | List contents                               |
| `ls -la`      | Long listing including hidden files         |
| `--help, -h, -?` | Help                                      |
| `man`         | Manual pages                                |

### Finding stuff

| Command       | Description                                  |
|---------------|----------------------------------------------|
| `locate`      | Search entire filesystem (uses daily-updated database) |
| `whereis`     | Find binary files, source and man pages     |
| `which`       | Returns location of binaries in `PATH` variable |
| `find`        | Search with multiple parameters: `find directory options expression` |

#### Wildcards 
- `*` Match any characters
- `.` , 
- `?` Match a single character
- `[]` Match specific characters

`grep` - Filtering via piping

### File/Directory Operations

| Command          | Description                                  |
|------------------|----------------------------------------------|
| `cat`           | Display file content                        |
| `cat > file`    | Create file + add text (CTRL+D to save)      |
| `cat >> file`   | Append to a file                            |
| `touch`         | Change file details/create empty file        |
| `mkdir dir`     | Make directory                              |
| `cp file1 file2`| Copy file                                   |
| `mv file1 file2`| Move/rename file                            |
| `rm file`       | Delete file                                 |
| `rmdir`         | Delete directory                            |
| `rm -r dir`     | Delete directory recursively                |
| `passwd`        | Change password                             |

### Pro Tips
- Never run as root unnecessarily (security risk!)
- `rm -r` is dangerous—double-check before deleting!
- Kali's strength: Pre-installed tools (e.g., nmap, aircrack-ng)

---

## Chapter 2: Text manipulation
## Core Concepts
- **Everything is a file**: Configuration, logs, and system files are all text-based
- **Text manipulation is essential** for system administration and hacking
- **Common use cases**: Config editing, log analysis, data filtering

## File Viewing Commands

### Basic Display
| Command            | Description                                  | Example                     |
|--------------------|----------------------------------------------|-----------------------------|
| `cat`              | Display entire file                          | `cat /etc/snort/snort.conf` |
| `head -n`          | Show first N lines                           | `head -20 file`             |
| `tail -n`          | Show last N lines                            | `tail -15 file`             |
| `nl`               | Display with line numbers                    | `nl config.txt`             |

### Advanced Viewers
| Command | Description | Navigation |
|---------|-------------|------------|
| `more`  | Page-by-page viewer | ENTER=next, q=quit |
| `less`  | Enhanced viewer with search | `/`=search, n=next match |

## Text Filtering & Processing

### grep (Global Regular Expression Print)
```bash
grep "pattern" file              # Basic search
grep -i "pattern" file           # Case-insensitive
grep -v "pattern" file           # Inverse match
cat file | grep "pattern"        # Piped filtering
```
sed (Stream Editor)
```bash
sed 's/old/new/g' file           # Replace all occurrences
sed 's/old/new/2' file           # Replace 2nd occurrence
sed 's/old/new/g' file > newfile # Save changes
```
Practical Examples
Working with Snort Config
```bash
cat /etc/snort/snort.conf | grep "output"  # Find output configs
nl /etc/snort/snort.conf | tail -20        # Numbered last 20 lines
less /etc/snort/snort.conf                 # Interactive exploration
```
Password List Analysis
```bash
cd /usr/share/wordlists/metasploit
cat passwords.lst | grep "123"    # Find simple passwords
nl passwords.lst | tail -5        # Numbered last 5 entries
```
Pro Techniques
- Combining commands with pipes (|) for powerful filtering
- Line numbers with nl for precise reference
- Search/replace workflows with sed
- Interactive exploration with less (search with /)

Exercises
1. Navigate to /usr/share/wordlists/metasploit
2. View passwords.lst with cat, more, and less
3. Add line numbers: nl passwords.lst
4. Find last 20 passwords: tail -20 passwords.lst
5. Search for patterns: cat passwords.lst | grep "123"

### Pro Tip
- Use man command (e.g., man grep) to explore advanced options for each tool.

## Chapter 3: Analyzing and managing networks
## Chapter 4: Adding and removing software
## Chapter 5: Controlling file and directory permissions
## Chapter 6: Process management
## Chapter 7: Managing user environment variables
## Chapter 8: Bash scripting
## Chapter 9: Compressing and archiving
## Chapter 10: Filesystem and storage device management
## Chapter 11: The logging system
## Chapter 12: Using and abusing services
## Chapter 13: Becoming secure and anonymous
## Chapter 14: Understanding and inspecting wireless networks
## Chapter 15: Managing the Linux kernel and loadable kernel modules
## Chapter 16: Automating tasks with job scheduling
## Chapter 17: Python scripting basics for hackers


Linux Network Management - Quick Reference Guide
(Based on Chapter 3: Analyzing and Managing Networks)

1. Network Analysis
Viewing Network Interfaces
Command	Description
ifconfig	Show all active network interfaces (IP, MAC, netmask)
iwconfig	Check wireless interfaces (mode, ESSID, signal strength)
Key Output Fields:

eth0: Wired interface

wlan0: Wireless interface

lo: Loopback (localhost, 127.0.0.1)

inet addr: IP address

HWaddr: MAC address

2. Modifying Network Settings
Changing IP Address
bash
ifconfig eth0 192.168.1.1      # Set static IP  
ifconfig eth0 192.168.1.1 netmask 255.255.255.0 broadcast 192.168.1.255  
Spoofing MAC Address
bash
ifconfig eth0 down             # Disable interface  
ifconfig eth0 hw ether 00:11:22:33:44:55  # Change MAC  
ifconfig eth0 up               # Re-enable interface  
DHCP Assignment
bash
dhclient eth0                  # Request new IP from DHCP  
3. DNS Manipulation
DNS Lookup with dig
bash
dig example.com ns             # Find nameservers  
dig example.com mx             # Find mail servers  
Changing DNS Server
Edit /etc/resolv.conf:

bash
echo "nameserver 8.8.8.8" > /etc/resolv.conf  # Use Google DNS  
Hijacking Domains with /etc/hosts
bash
leafpad /etc/hosts             # Add malicious mappings  
# Example:  
192.168.1.100 www.bank.com    # Redirect traffic to local IP  
4. Key Takeaways
ifconfig/iwconfig: Essential for network recon.

MAC Spoofing: Evade MAC-based security controls.

DNS Tricks: Use dig for recon, /etc/hosts for redirection.

DHCP: Reset IPs with dhclient.

Exercises (Try These!)
Check your network interfaces with ifconfig.

Change eth0 IP to 192.168.1.1.

Spoof your MAC address on eth0.

Find your wireless adapter details with iwconfig.

Reset eth0 to DHCP with dhclient eth0.

Use dig to find nameservers for a website.

Add Google DNS (8.8.8.8) to /etc/resolv.conf.

Pro Tip: Use macchanger -r eth0 for random MAC spoofing (install with apt install macchanger).

Linux Software Management - Quick Reference Guide
(Based on Chapter 4: Adding and Removing Software)

1. APT Package Management
Searching for Packages
bash
apt-cache search snort          # Search for "snort" in repositories  
Installing/Removing Packages
bash
apt-get install snort           # Install Snort  
apt-get remove snort            # Remove Snort (keeps config files)  
apt-get purge snort             # Remove Snort + config files  
Updating & Upgrading
bash
apt-get update                 # Refresh package lists  
apt-get upgrade                # Upgrade all installed packages  
2. Managing Repositories
Editing sources.list
bash
leafpad /etc/apt/sources.list   # Add/remove repositories  
Example: Add Ubuntu repositories for additional software:

text
deb http://archive.ubuntu.com/ubuntu bionic main  
Key Repository Categories
main: Officially supported open-source software

universe: Community-maintained software

multiverse: Copyrighted/restricted software

3. GUI-Based Installers
Synaptic Package Manager
bash
apt-get install synaptic       # Install Synaptic  
Usage:

Launch via Settings → Synaptic Package Manager

Search for packages (e.g., "snort")

Mark for installation → Apply

4. Installing from GitHub
Cloning Repositories
bash
git clone https://github.com/user/repo.git  
Example: Install bluediving (Bluetooth hacking tool):

bash
git clone https://github.com/balle/bluediving.git  
cd bluediving                  # Navigate to cloned directory  
ls -l                          # Verify files  
5. Key Takeaways
apt-get: Primary tool for Debian/Kali package management.

Repositories: Edit /etc/apt/sources.list to add trusted sources.

GitHub: Use git clone for cutting-edge tools not in repositories.

GUI Tools: Synaptic provides a visual alternative to CLI.

Exercises (Try These!)
Install metasploit-framework via apt-get.

Remove it, then reinstall with purge to delete config files.

Update your package lists with apt-get update.

Upgrade all packages with apt-get upgrade.

Clone a hacking tool from GitHub (e.g., theHarvester).

Pro Tip: Always check dependencies with apt-cache show <package> before installation.

Linux File Permissions & Privilege Escalation - Quick Reference Guide
(Based on Chapter 5: Controlling File and Directory Permissions)

1. Permission Basics
User Types
Owner (u): Creator of the file/directory

Group (g): Users in the file's group

Others (o): All other users

Permission Types
Symbol	Permission	Octal Value
r	Read	4
w	Write	2
x	Execute	1
Example: -rwxr-xr--

Owner: rwx (4+2+1 = 7)

Group: r-x (4+0+1 = 5)

Others: r-- (4+0+0 = 4)
→ Permission code: 754

2. Changing Permissions
Numeric Method
bash
chmod 754 file.txt  # Owner: rwx, Group: r-x, Others: r--  
Symbolic (UGO) Method
bash
chmod u+x file.txt      # Add execute for owner  
chmod g-w file.txt      # Remove write for group  
chmod o=rx file.txt     # Set others to read+execute  
Changing Ownership
bash
chown bob file.txt      # Change owner to "bob"  
chgrp hackers file.txt  # Change group to "hackers"  
3. Special Permissions
Permission	Octal	Effect
SUID (Set User ID)	4	Runs as file owner (e.g., chmod 4755 file)
SGID (Set Group ID)	2	Runs as file group (e.g., chmod 2755 file)
Sticky Bit	1	Restricts file deletion in directories (rarely used)
SUID Example:

bash
find / -user root -perm -4000  # Find all SUID files owned by root  
Note: SUID binaries (e.g., sudo, passwd) are common privilege escalation targets.

4. Privilege Escalation via SUID/SGID
Finding Vulnerable Binaries
bash
# Find SUID files:  
find / -perm -4000 -type f 2>/dev/null  

# Find SGID files:  
find / -perm -2000 -type f 2>/dev/null  
Exploiting SUID Binaries
If a binary with SUID (e.g., /usr/bin/customscript) has poor input validation:

bash
./customscript "$(cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash)"  
/tmp/rootbash -p  # Spawns a root shell!  
5. Key Takeaways
Default Permissions: Files (644), Directories (755)

umask: Subtracts from defaults (e.g., umask 022 → files=644, dirs=755)

SUID/SGID: Critical for privilege escalation attacks.

Always check permissions on sensitive files (/etc/shadow, /etc/passwd).

Exercises (Try These!)
List permissions in /etc/passwd with ls -l /etc/passwd.

Create a file and give it rwx for owner, r-x for group, --- for others.

Find all SUID binaries:

bash
find / -perm -4000 -type f 2>/dev/null  
Change ownership of a file to another user with chown.

Pro Tip: Use sudo -l to check for sudo privileges that can be exploited for root access.

Linux Process Management - Quick Reference Guide
(Based on Chapter 6: Process Management)

1. Viewing Processes
Basic Process Listing
bash
ps                     # Shows current terminal's processes  
ps aux                 # Shows ALL processes (detailed)  
Key Columns:

USER: Process owner

PID: Process ID (essential for management)

%CPU/%MEM: Resource usage

COMMAND: Process name

Filtering Processes
bash
ps aux | grep "metasploit"   # Find Metasploit processes  
Real-Time Monitoring with top
bash
top                    # Dynamic view of resource-hungry processes  
Interactive Commands:

k: Kill a process (enter PID)

r: Renice (change priority)

q: Quit

2. Managing Processes
Priority Control (nice/renice)
Command	Description
nice -n -10 /bin/process	Start process with high priority (-20 to 19)
renice 15 -p 1234	Change priority of running process (PID 1234)
Killing Processes
Signal	Number	Effect
SIGHUP	1	Restarts process
SIGTERM	15	Graceful termination (default)
SIGKILL	9	Forceful termination (use sparingly)
Commands:

bash
kill -9 1234           # Force-kill PID 1234  
killall -9 "process"   # Kill all instances of "process"  
Background/Foreground Jobs
bash
leafpad file.txt &     # Run in background  
jobs                  # List background jobs  
fg %1                 # Bring job 1 to foreground  
3. Scheduling Processes
One-Time Tasks (at)
bash
at 1:00 AM Wed        # Schedule a command  
at> /root/scan.sh     # Script to run  
at> [CTRL+D]          # Save job  
Time Formats:

at noon

at now + 2 hours

Recurring Tasks (cron)
(See Chapter 16 for full details)

4. Key Takeaways
ps aux | grep: Find specific processes.

top: Monitor resource usage in real-time.

kill -9: Last resort for stubborn processes.

&: Run processes in background to free terminal.

at: Schedule one-time tasks (e.g., scans).

Exercises (Try These!)
List all processes with ps aux and identify the first/last PID.

Use top to find the most resource-intensive process.

Kill it with kill -9 [PID].

Reduce priority of a process:

bash
renice 19 -p [PID]  
Schedule a script to run next Wednesday at 1 AM:

bash
at 1:00 AM Wed  
at> /root/myscanning  
at> [CTRL+D]  
Pro Tip: Use htop (install via apt install htop) for a more user-friendly process viewer.

Linux Environment Variables - Quick Reference Guide
(Based on Chapter 7: Managing User Environment Variables)

1. Viewing & Modifying Variables
Listing Variables
Command	Description
env	Shows environment variables
set	Shows all variables (including shell/local)
`set	more`	Paginated view
echo $VARIABLE	View a specific variable (e.g., echo $PATH)
Changing Variables
bash
HISTSIZE=0                  # Disable command history (temporary)  
export HISTSIZE=0           # Make change permanent  
2. Customizing Your Shell
Changing the Prompt (PS1)
bash
PS1="\u@\h:\w\$ "           # Default format (user@host:dir$)  
PS1="HackerMode: "          # Custom text prompt  
export PS1="C:\Windows> "   # Fake Windows prompt  
Placeholders:

\u: Username

\h: Hostname

\w: Current directory

Example: Stealthy Prompt
bash
export PS1="C:\Windows\System32> "  # Mimics Windows cmd  
3. Managing PATH
Viewing & Adding Directories
bash
echo $PATH                   # Show current PATH  
PATH=$PATH:/new/directory    # Add a directory to PATH  
Warning: Never overwrite PATH! Always append ($PATH:new_dir).

Example: Adding a Hacking Tools Directory
bash
PATH=$PATH:/root/tools       # Makes tools accessible globally  
4. User-Defined Variables
Creating & Removing
bash
MYVAR="Hello, hacker!"       # Create a variable  
echo $MYVAR                  # View its value  
unset MYVAR                  # Delete the variable  
Making Variables Permanent
bash
export MYVAR="value"         # Available in all sessions  
5. Key Takeaways
PATH: Controls where Linux looks for commands.

PS1: Customize your terminal prompt for convenience/stealth.

HISTSIZE=0: Disables command history (opsec).

Always export to make changes persistent.

Exercises (Try These!)
View all variables:

bash
env | more  
Check hostname:

bash
echo $HOSTNAME  
Create a fake Windows prompt:

bash
export PS1="C:\Windows\> "  
Create a custom variable:

bash
MYNAME="YourName"  
echo $MYNAME  
Add a directory to PATH:

bash
PATH=$PATH:/home/yourname/bin  
Pro Tip: Use alias to create shortcuts for frequently used commands (e.g., alias ll='ls -la').

Bash Scripting for Hackers - Quick Reference Guide
(Based on Chapter 8: Bash Scripting)

1. Script Basics
Structure of a Bash Script
bash
#!/bin/bash                  # Shebang (required)  
# This is a comment          # Comments start with #  
echo "Hello, Hackers!"       # Commands to execute  
Key Commands
Command	Description
echo	Print text/variables
read	Capture user input
chmod +x script.sh	Make script executable
./script.sh	Run the script
2. Essential Scripting Techniques
Variables & User Input
bash
#!/bin/bash  
echo "Enter target IP:"  
read target_ip  
echo "Scanning $target_ip..."  
nmap -sT $target_ip  
Conditional Statements
bash
if [ $port -eq 3306 ]; then  
  echo "MySQL port found!"  
else  
  echo "Not MySQL."  
fi  
Loops
bash
for ip in {1..254}; do  
  nmap -sn 192.168.1.$ip  
done  
3. Practical Hacker Scripts
Port Scanner (Basic)
bash
#!/bin/bash  
nmap -sT 192.168.1.0/24 -p 3306 >/dev/null -oG mysql_scan  
grep open mysql_scan > results.txt  
cat results.txt  
Advanced Port Scanner (User Input)
bash
#!/bin/bash  
echo "Enter first IP octets (e.g., 192.168.1):"  
read base_ip  
echo "Enter port to scan:"  
read port  
nmap -sT $base_ip.0/24 -p $port | grep open  
Service Detection
bash
#!/bin/bash  
echo "Enter IP range (e.g., 192.168.1.1-100):"  
read ip_range  
nmap -sV $ip_range  
4. Key Takeaways
Shebang #!/bin/bash is mandatory for bash scripts.

Variables store data (var="value"; access with $var).

User input is captured with read.

Nmap integration enables powerful scanning tools.

Always chmod +x scripts before running.

Exercises (Try These!)
Greeting Script:

bash
#!/bin/bash  
echo "Welcome, $(whoami)! Today is $(date)."  
MSSQL Scanner:

bash
#!/bin/bash  
nmap -sT 192.168.1.0/24 -p 1433 | grep open  
Advanced MSSQL Scanner:

bash
#!/bin/bash  
echo "Enter starting IP:"; read start_ip  
echo "Enter ending IP:"; read end_ip  
nmap -sT $start_ip-$end_ip -p 1433 | grep open  
Pro Tip: Use #!/bin/bash -x to debug scripts (prints each command before execution).

Linux File Compression & Archiving - Quick Reference Guide
(Based on Chapter 9: Compressing and Archiving)

1. Archiving Files with tar
Creating a Tarball
bash
tar -cvf archive.tar file1 file2 file3  # Combine files into a .tar  
Options:

-c: Create archive

-v: Verbose (show progress)

-f: Specify filename

Viewing/Extracting Archives
bash
tar -tvf archive.tar       # List contents  
tar -xvf archive.tar       # Extract files  
tar -xzf archive.tar.gz    # Extract .gz compressed tarball  
2. Compression Tools
Command	Compress	Decompress	Extension	Notes
gzip	gzip file	gunzip file.gz	.gz	Fast, moderate compression
bzip2	bzip2 file	bunzip2 file.bz2	.bz2	Slower, better compression
compress	compress file	uncompress file.Z	.Z	Least common
Example:

bash
gzip archive.tar          # Compress to archive.tar.gz  
bunzip2 archive.tar.bz2   # Decompress .bz2 file  
3. Forensic Copying with dd
Bit-by-Bit Disk Copy
bash
dd if=/dev/sdb of=/root/disk_copy.img bs=4M conv=noerror  
Key Parameters:

if: Input file (e.g., /dev/sdb for a USB drive)

of: Output file (saved as an image)

bs: Block size (e.g., 4M for 4MB chunks)

conv=noerror: Continue copying after errors

Warning:

Double-check if= target—dd can overwrite disks irreversibly!

4. Key Takeaways
tar: Best for combining files before compression.

gzip/bzip2: Use for compression (trade speed vs. size).

dd: Essential for forensic copies (recovers deleted files).

Exercises (Try These!)
Create three scripts and archive them:

bash
tar -cvf L4H.tar Linux4Hackers{1,2,3}  
Compress with different tools:

bash
gzip L4H.tar       # → L4H.tar.gz  
bzip2 L4H.tar      # → L4H.tar.bz2  
Clone a USB drive:

bash
dd if=/dev/sdc of=/root/usb_copy.img bs=4M  
Pro Tip: Use pv (pipe viewer) with dd to monitor progress:

bash
apt install pv  
dd if=/dev/sdb | pv | dd of=/root/disk_copy.img  

Linux Filesystem and Storage Device Management - Reference Guide
1. Linux Device Representation
Linux uses a file tree structure with / (root) at the top.

Unlike Windows (C:, D:), storage devices are mounted into the filesystem.

All devices are represented as files in the /dev directory.

Device Naming Convention
Device	Description
sda	First SATA/SCSI drive
sdb	Second SATA/SCSI drive
sdc	Third SATA/SCSI drive
sda1	First partition on sda
sda2	Second partition on sda
Types of Devices
Character Devices (c) – Transfer data character by character (e.g., keyboards, mice).

Block Devices (b) – Transfer data in blocks (e.g., hard drives, SSDs, USB drives).

2. Listing and Managing Devices
Commands for Device Information
Command	Description
ls /dev	List all devices
fdisk -l	List all disks and partitions (requires sudo)
lsblk	List block devices in a tree format
df	Show disk space usage
fsck	Check and repair filesystem errors
Example: Listing Partitions
bash
sudo fdisk -l   # List all disks and partitions
lsblk           # Show block devices in a tree
df -h           # Show disk usage in human-readable format
3. Mounting and Unmounting Devices
Mounting = Attaching a storage device to the filesystem.

Unmounting = Safely detaching before removal.

Mount Points
/mnt – Typically for internal drives.

/media – Typically for removable media (USB drives).

Mounting a USB Drive
bash
sudo mount /dev/sdb1 /media   # Mount USB to /media
Unmounting a USB Drive
bash
sudo umount /dev/sdb1   # Unmount before removal
⚠️ Cannot unmount if the device is in use!

4. Checking and Repairing Filesystems
Using fsck (Filesystem Check)
Unmount the device first:

bash
sudo umount /dev/sdb1
Run fsck (specify filesystem type if needed):

bash
sudo fsck /dev/sdb1   # Check for errors
sudo fsck -p /dev/sdb1 # Auto-repair errors
5. Key Takeaways for Hackers
External Media: Hackers often use USB drives to load tools/data.

Finding Critical Files: Understanding /dev, /mnt, and /media helps locate sensitive data.

Disk Cloning: The dd command can copy entire drives (including deleted files).

Error Handling: Use fsck to check for disk corruption.

Quick Command Reference
Task	Command
List disks & partitions	sudo fdisk -l
View block devices	lsblk
Check disk space	df -h
Mount a drive	sudo mount /dev/sdX1 /mnt
Unmount a drive	sudo umount /dev/sdX1
Check for errors	sudo fsck /dev/sdX1
Clone a disk	sudo dd if=/dev/sdX of=/dev/sdY

Linux Logging System - Reference Guide
1. Understanding Linux Logging
Log files track system events, errors, and security alerts.

Hackers need to know how to read logs (for reconnaissance) and manipulate them (to cover tracks).

System admins use logs to detect intrusions and troubleshoot issues.

Key Logging Daemons
Daemon	Description
rsyslog	Default in Debian/Kali (modern replacement for syslogd)
syslog-ng	Alternative logging system (used in some distros)
2. The rsyslog Configuration
Main Configuration File
Located at /etc/rsyslog.conf

Defines what to log, where to log, and how to log.

Logging Rule Format
plaintext
facility.priority    action
Facility = Source of the log (e.g., auth, kern, mail).

Priority = Severity level (e.g., info, crit, emerg).

Action = Where logs are stored (e.g., /var/log/auth.log).

Common Facilities
Facility	Description
auth	Authentication/security logs
cron	Scheduled tasks (cron jobs)
kern	Kernel messages
mail	Email system logs
user	User-level logs
Priority Levels (Low → High)
Priority	Description
debug	Debugging info
info	General messages
notice	Normal but significant events
warning	Potential issues
err	Errors
crit	Critical conditions
alert	Immediate action needed
emerg	System unusable
3. Log Rotation (logrotate)
Prevents log files from consuming too much disk space.

Default config file: /etc/logrotate.conf

Key Settings
Setting	Description
weekly	Rotate logs every week
rotate 4	Keep 4 weeks of logs
compress	Gzip old logs (disabled by default)
Example: Rotate Auth Logs
plaintext
/var/log/auth.log {
    weekly
    rotate 4
    compress
    missingok
}
4. Covering Tracks (For Hackers)
Option 1: Delete Logs
bash
rm /var/log/auth.log  # Basic deletion (recoverable)
❌ Problem: Leaves traces in filesystem metadata.

Option 2: Shred Logs (Secure Deletion)
bash
shred -f -n 10 /var/log/auth.log  # Overwrite 10 times
✅ Better: Makes recovery extremely difficult.

Option 3: Disable Logging
bash
service rsyslog stop  # Temporarily stop logging
⚠️ Warning: Stopping logging may alert admins.

5. Key Log Files
Log File	Purpose
/var/log/auth.log	Authentication logs (logins, sudo, SSH)
/var/log/syslog	General system activity
/var/log/kern.log	Kernel messages
/var/log/cron.log	Scheduled tasks (cron jobs)
/var/log/mail.log	Email server logs
Quick Command Reference
Task	Command
View rsyslog config	cat /etc/rsyslog.conf
Check active logs	tail -f /var/log/syslog
Rotate logs manually	logrotate -f /etc/logrotate.conf
Shred log files	shred -f -n 5 /var/log/auth.log
Stop logging	service rsyslog stop

Linux Services - Reference Guide
1. Understanding Linux Services
Services = Background applications that run continuously (e.g., web servers, databases).

Key Services for Hackers:

Apache (Web Server)

OpenSSH (Remote Access)

MySQL (Database)

PostgreSQL (Metasploit Database)

2. Managing Services
Basic Commands
Command	Description
service <name> start	Start a service
service <name> stop	Stop a service
service <name> restart	Restart a service
systemctl status <name>	Check service status
Examples
bash
service apache2 start   # Start Apache web server
service ssh stop        # Stop SSH service
service mysql restart   # Restart MySQL
3. Key Services & Their Uses
1. Apache Web Server (apache2)
Purpose: Host websites.

Default Web Root: /var/www/html/

Edit Default Page:

bash
nano /var/www/html/index.html
Start Apache:

bash
service apache2 start
Access Website: Open browser to http://localhost

2. OpenSSH (ssh)
Purpose: Securely access remote systems.

Start SSH:

bash
service ssh start
Connect to Remote Host:

bash
ssh user@192.168.1.101
Raspberry Pi Spy Example:

bash
ssh pi@<Pi_IP>  # Log into Raspberry Pi
raspistill -o spyphoto.jpg  # Take a picture remotely
3. MySQL (mysql)
Purpose: Store & manage database-driven data (e.g., websites, credentials).

Start MySQL:

bash
service mysql start
Log in as Root:

bash
mysql -u root -p
Change Password:

sql
UPDATE mysql.user SET password=PASSWORD("hackers-arise") WHERE user='root';
FLUSH PRIVILEGES;
Extract Data:

sql
SHOW DATABASES;
USE <database>;
SHOW TABLES;
SELECT * FROM <table>;
4. PostgreSQL (postgresql)
Purpose: Used by Metasploit for storing scan/exploit data.

Start PostgreSQL:

bash
service postgresql start
Set Up for Metasploit:

bash
msfdb init  # Initialize Metasploit DB
su postgres # Switch to Postgres user
createuser msf_user -P  # Create user
createdb --owner=msf_user hackers_arise_db  # Create DB
Connect in Metasploit:

bash
msfconsole
db_connect msf_user:password@127.0.0.1/hackers_arise_db
db_status  # Verify connection
4. Security Considerations
For Hackers (Covering Tracks)
Stop Logging:

bash
service rsyslog stop  # Disable logging
Shred Logs:

bash
shred -f -n 10 /var/log/auth.log  # Overwrite & delete logs
For Admins (Hardening Services)
Always set strong passwords for MySQL/PostgreSQL.

Disable unused services (service <name> stop + systemctl disable <name>).

Use firewalls (ufw) to restrict access.

Quick Command Cheat Sheet
Task	Command
Start Apache	service apache2 start
Take remote photo (RPi)	raspistill -o photo.jpg
MySQL login	mysql -u root -p
List databases (MySQL)	SHOW DATABASES;
Postgres + Metasploit setup	msfdb init
Check service status	systemctl status <service>

Linux Security & Anonymity - Reference Guide
1. Understanding Online Tracking
IP Addresses reveal your identity and location

Google/Email Services track keywords for ads

Packet Headers contain source/destination IPs (visible in transit)

Traceroute shows the path your traffic takes:

bash
traceroute google.com
2. Tor (The Onion Router)
How Tor Works
Routes traffic through multiple encrypted relays

Each relay only knows previous/next hop (not origin/destination)

Access via Tor Browser (https://www.torproject.org/)

Security Concerns
Exit nodes can see unencrypted traffic

NSA/FSB run Tor relays (traffic correlation attacks)

Slow speeds due to encryption/relays

Usage
bash
sudo apt install torbrowser-launcher
torbrowser-launcher
3. Proxy Servers
ProxyChains (Kali Linux Tool)
Routes traffic through multiple proxies

Config file: /etc/proxychains.conf

bash
# Example: Random chaining with 3 proxies
random_chain
chain_len = 3
[ProxyList]
socks4 114.134.186.12 22020
socks4 188.187.190.59 8888
Usage
bash
proxychains nmap -sT 192.168.1.1
proxychains firefox www.hackers-arise.com
Security Concerns
Free proxies may log/sell your data

Paid proxies (e.g., Luminati) are more trustworthy

4. VPNs (Virtual Private Networks)
Top VPN Services
VPN	Price (Yearly)	Logging Policy
NordVPN	~$60	No logs
ExpressVPN	~$100	No logs
ProtonVPN	Free/$96	No logs
Advantages
Encrypts all traffic

Masks IP address

Bypasses geo-restrictions (Netflix, Hulu)

Limitations
VPN provider can see your traffic

Some countries block VPNs (China, Russia)

5. Encrypted Email (ProtonMail)
End-to-end encryption (even ProtonMail can't read emails)

Based in Switzerland (strong privacy laws)

Free accounts available: https://protonmail.com/

Quick Command Reference
Task	Command
Check IP route	traceroute google.com
Start Tor Browser	torbrowser-launcher
Route Nmap scan via proxies	proxychains nmap -sT <IP>
Test VPN connection	curl ifconfig.me (should show VPN IP)

