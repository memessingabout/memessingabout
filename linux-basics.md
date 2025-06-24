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
  
---

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
