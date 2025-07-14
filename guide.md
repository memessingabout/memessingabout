# Linux-to-Python Learning Guide.

**Goal**: Master Linux basics (commands, scripting, system navigation) and Python (from basics to intermediate concepts) to prepare for Zone01’s piscine and build a strong programming foundation.  
**Timeline**: July 14–July 27, 2025 (~2 weeks), with daily 30–60 minute sessions.  
**Approach**: Combine Linux and Python in project-based tasks using Kali Linux. Focus on practical skills, small wins for motivation, and deeper concepts for Zone01 readiness.  
**Resources**: *Linux Basics for Hackers* (OccupyTheWeb), Kali Linux, Python 3.

## Week 1: Linux Foundations & Python Setup (July 14–July 20)
Focus: Get comfortable in Kali’s terminal, master essential Linux commands, and set up Python for scripting.

### Day 1: Linux Environment Setup & Basic Commands (30 min)
- **Goal**: Navigate Kali confidently and set up Python environment.
- **Tasks**:
  - Open terminal. Run `whoami`, `pwd`, `ls -la`, `cd`, `mkdir test_dir`. Note each command’s purpose.
  - Check Python: `python3 --version`. Install pip: `sudo apt install python3-pip`.
  - Create project directory: `mkdir ~/hacking_projects`.
  - *Quick Win*: Save cheat sheet: “`cd ~/hacking_projects` to enter projects; `python3 script.py` to run.”
- **Why**: Builds Kali confidence; ensures Python readiness (Ch. 1–2, *Linux Basics for Hackers*).

### Day 2: File System Navigation & Python Hello World (30 min)
- **Goal**: Master file navigation and write first Python script.
- **Tasks**:
  - Linux: Use `ls`, `cd`, `touch test.txt`, `cat test.txt`, `rm test.txt`. Create structure: `mkdir ~/hacking_projects/day2; touch ~/hacking_projects/day2/notes.txt`.
  - Python: Write `script.py` with `nano`:
    ```python
    print("Hello, Kali Hacker!")
    ```
    Run: `python3 script.py`. Save output: `python3 script.py > output.txt`, view with `cat output.txt`.
  - *Quick Win*: Verify output in `output.txt`.
- **Why**: Links Linux file handling with Python output.

### Day 3: Permissions & Python Variables (40 min)
- **Goal**: Understand Linux permissions and Python data types.
- **Tasks**:
  - Linux: Run `chmod 700 script.py`, `ls -l` to check permissions. Try `chown`, `sudo touch /root/test.txt` (note failure).
  - Python: Edit `script.py`:
    ```python
    name = input("Enter your hacker name: ")
    print(f"Access granted, {name}!")
    ```
    Run and test with your name.
  - *Quick Win*: Save as `~/hacking_projects/day3/greet.py`.
- **Why**: Permissions are key for hacking (Ch. 4–5); variables are Python’s foundation.

### Day 4: Shell Basics & Python Conditionals (40 min)
- **Goal**: Run shell commands and add Python logic.
- **Tasks**:
  - Linux: Use piping/redirection: `ls -l | grep py > files.txt`. View: `cat files.txt`.
  - Python: Update `greet.py`:
    ```python
    name = input("Enter hacker name: ")
    if name == "root":
        print("Superuser access!")
    else:
        print(f"Welcome, {name}.")
    ```
  - *Quick Win*: Test with “root” and another name.
- **Why**: Shell skills are hacker essentials (Ch. 6–7); conditionals add logic.

### Day 5: Scripting Intro & Python Loops (45 min)
- **Goal**: Write a bash script and loop in Python.
- **Tasks**:
  - Linux: Create `scan.sh`:
    ```bash
    #!/bin/bash
    echo "Listing Python files:"
    ls *.py
    ```
    Run: `chmod +x scan.sh; ./scan.sh`.
  - Python: Update `greet.py`:
    ```python
    for i in range(3):
        name = input(f"Attempt {i+1}: Enter name: ")
        if name == "root": break
        print(f"Try {i+1}: {name}")
    ```
  - *Quick Win*: Save as `loop.py`, test breaking with “root”.
- **Why**: Bash scripting automates tasks (Ch. 10–11); loops are Python essentials.

### Day 6: Networking Basics & Python Lists (45 min)
- **Goal**: Explore network commands and Python data structures.
- **Tasks**:
  - Linux: Run `ifconfig` or `ip a`, `ping 8.8.8.8`, `netstat -tulnp`. Note services.
  - Python: Create `ports.py`:
    ```python
    ports = [22, 80, 443]
    for port in ports:
        print(f"Scanning port {port}")
    ```
  - *Quick Win*: Add a port, rerun script.
- **Why**: Networking is hacking core (Ch. 12–13); lists prep for data handling.

### Day 7: Review & Mini-Project (60 min)
- **Goal**: Combine skills in a project.
- **Tasks**:
  - Linux: Write `setup_project.sh` to create a folder and copy `.py` files.
  - Python: Create `file_scanner.py`:
    ```python
    import os
    files = os.listdir(".")
    for file in files:
        if file.endswith(".py"):
            print(f"Found Python file: {file}")
    ```
  - *Quick Win*: Run both scripts, verify output.
- **Why**: Ties Linux and Python for practical outcome.

## Week 2: Deeper Linux & Python Concepts (July 21–July 27)
Focus: Build on basics with intermediate Linux (processes, automation) and Python (functions, file handling, modules).

### Day 8: Processes & Python Functions (45 min)
- **Goal**: Manage Linux processes and modularize Python code.
- **Tasks**:
  - Linux: Run `ps aux`, `top`, `kill <pid>`. Find Python PID: `ps aux | grep python`.
  - Python: Create `utils.py`:
    ```python
    def scan_file(filename):
        return filename.endswith(".py")
    files = ["test.py", "doc.txt"]
    for f in files:
        if scan_file(f):
            print(f"{f} is a Python file")
    ```
  - *Quick Win*: Import `scan_file` in a new script, test it.
- **Why**: Process management is critical (Ch. 8–9); functions organize code.

### Day 9: Automation & Python File I/O (50 min)
- **Goal**: Automate tasks and read/write files in Python.
- **Tasks**:
  - Linux: Create cron job: `crontab -e`, add `*/5 * * * * ls ~/hacking_projects >> log.txt`.
  - Python: Write `log_reader.py`:
    ```python
    with open("log.txt", "r") as f:
        print(f.read())
    ```
  - *Quick Win*: Check `log.txt` after cron runs.
- **Why**: Automation is key (Ch. 15); file I/O is powerful.

### Day 10: Networking Tools & Python Dictionaries (50 min)
- **Goal**: Use Kali’s network tools and Python dictionaries.
- **Tasks**:
  - Linux: Run `nmap localhost` (install: `sudo apt install nmap`). Note open ports.
  - Python: Create `port_map.py`:
    ```python
    services = {22: "SSH", 80: "HTTP", 443: "HTTPS"}
    for port, service in services.items():
        print(f"Port {port}: {service}")
    ```
  - *Quick Win*: Add a port-service pair, rerun.
- **Why**: Nmap is hacking 101 (Ch. 13); dictionaries handle data.

### Day 11: Shell Scripting & Python Modules (50 min)
- **Goal**: Write advanced shell scripts and use Python modules.
- **Tasks**:
  - Linux: Create `monitor.sh`:
    ```bash
    #!/bin/bash
    if pgrep python3; then
        echo "Python is running!"
    fi
    ```
  - Python: Create `system_check.py`:
    ```python
    import os
    if os.path.exists("log.txt"):
        print("Log found!")
    ```
  - *Quick Win*: Run both, verify output.
- **Why**: Scripting automates tasks (Ch. 11); modules extend Python.

### Day 12: Security Tools & Python Error Handling (50 min)
- **Goal**: Explore Kali tools and handle Python errors.
- **Tasks**:
  - Linux: Run `hydra` or `metasploit` (safely, in lab). Read: `man hydra`.
  - Python: Update `log_reader.py`:
    ```python
    try:
        with open("log.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Log file missing!")
    ```
  - *Quick Win*: Test with a missing file.
- **Why**: Security tools are Kali’s core (Ch. 16–17); error handling is robust.

### Day 13: Python in Hacking & Final Prep (60 min)
- **Goal**: Tie Linux and Python in a hacking project.
- **Tasks**:
  - Linux: Run `tcpdump`: `sudo tcpdump -i eth0`.
  - Python: Write `packet_parser.py`:
    ```python
    ports = [22, 80, 443]
    for port in ports:
        print(f"Simulating packet on port {port}")
    ```
  - *Quick Win*: Run both, imagine integration.
- **Why**: Preps for Zone01’s project-based challenges.

### Day 14: Review & Zone01 Prep (60 min)
- **Goal**: Consolidate skills and simulate Zone01 task.
- **Tasks**:
  - Linux: Review commands. Write a script to automate a task (e.g., list Python files).
  - Python: Build a project (e.g., check ports, parse logs). Practice a challenge: reverse a string or sum a list.
  - *Quick Win*: Share project on X for feedback.
- **Why**: Ensures piscine readiness.

## Tips for Success
- **Motivation**: Track daily wins in `~/hacking_projects/notes.txt` (e.g., “Wrote loop.py”). Share progress on X.
- **Structure**: Stick to 30–60 min daily, same time (e.g., after breakfast). Organize scripts in `~/hacking_projects`.
- **Commitment**: Tie tasks to Zone01’s July 28 start. If you slip, do 10 min the next day.
- **Forgetting Fix**: Keep `commands.txt` in `~/hacking_projects` for snippets (e.g., `chmod +x`, `python3 script.py`).
- **Bad Habits**: Avoid YouTube rabbit holes. Use `man` pages or X for specific errors.

## Notes
- Save this as `~/hacking_projects/learning_guide.md`.
- Refer to it daily to stay on track.
- For Zone01 onboarding (July 18, Kisumu), review Day 1–3 before attending.
- If stuck, note the issue (e.g., “Python loop fails”) and seek help on X or ask Grok.

*Last updated: July 14, 2025*