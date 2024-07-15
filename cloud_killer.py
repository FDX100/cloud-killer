import os  # Import the os module for interacting with the operating system

# Check if the requests library is available, install it if not
try:
    import requests
except Exception:
    print('requests library not found. Please install it by: pip3 install requests')
    install = input('Do you want to install this library for you? (Y or N) >>')
    if install == "Y" or install == 'y':
        os.system('sudo apt-get install python3-pip')
        os.system('pip3 install requests')
    else:
        quit()

# Check if the subprocess library is available, install it if not
try:
    import subprocess
except Exception:
    print('subprocess library not found. Please install it by: pip3 install subprocess')
    install = input('Do you want to install this library for you? (Y or N) >>')
    if install == "Y" or install == 'y':
        os.system('sudo apt-get install python3-pip')
        os.system('pip3 install subprocess')
    else:
        quit()

# Check if the re (regular expression) library is available, install it if not
try:
    import re
except Exception:
    print('re library not found. Please install it by: pip3 install re')
    install = input('Do you want to install this library for you? (Y or N) >>')
    if install == "Y" or install == 'y':
        os.system('sudo apt-get install python3-pip')
        os.system('pip3 install re')
    else:
        quit()

# Check if the multiprocessing library is available, install it if not
try:
    import multiprocessing
except Exception:
    print('multiprocessing library not found. Please install it by: pip3 install multiprocessing')
    install = input('Do you want to install this library for you? (Y or N) >>')
    if install == "Y" or install == 'y':
        os.system('sudo apt-get install python3-pip')
        os.system('pip3 install multiprocessing')
    else:
        quit()

# Print a welcome banner
print('\x1b[1;32;40m' + '''
   _____ _                 _   _  ___ _ _
  / ____| |               | | | |/ (_) | |
 | |    | | ___  _   _  __| | | ' / _| | | ___ _ __
 | |    | |/ _ \| | | |/ _` | |  < | | | |/ _ \ '__|
 | |____| | (_) | |_| | (_| | | . \| | | |  __/ |
  \_____|_|\___/ \__,_|\__,_| |_|\_\_|_|_|\___|_|''' + '\033[0m')
print('''
 ==================================================
                    From FD
                github.com/FDX100
            bypass Cloud Protection
 ===================================================
''')

# Get the target domain from the user and create an empty report file
try:
    domain = input('[+] Enter Target domain >> ')
    report_name = f'Report_{domain}.txt'
    with open(report_name, 'w') as f:
        pass
except KeyboardInterrupt:
    print('\n[-] Cloud Killer is closed !! ')
    quit()

# Define the function that checks the domain
def checker(domain, report_name):
    try:
        # Send a GET request to the domain
        link = requests.get(f'http://{domain}', timeout=1)
        # Check if the response status code is one of the expected values
        if link.status_code in [200, 403, 400, 500, 503, 404]:
            # Ping the domain to get its IP address
            ping_command = subprocess.check_output(f'ping -c 1 -w 1 {domain}', shell=True)
            filtered_re = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ping_command.decode('utf-8'))
            if filtered_re:
                print('\r' + '\033[1;32;40m' + '[+] The domain : ' + domain + ' has IP address: ' + filtered_re[0] + '\033[0m\n')
                # Write the domain to the report file
                with open(report_name, 'a') as f:
                    f.write(domain + '\n')
        else:
            print(f'\r\033[0;31;40m[-] Trying : {domain} \033[0m', end='', flush=True)
    except Exception:
        print(f'\r\033[0;31;40m[-] Trying : {domain} \033[0m', end='', flush=True)

# Define the function that processes subdomains
def process_subdomains(domain, report_name):
    try:
        # Open the file containing the list of subdomains
        with open('subl.txt', 'r') as wordlist:
            subdomains = [f'{word.strip()}.{domain}' for word in wordlist]
            # Use a multiprocessing pool to check subdomains in parallel
            with multiprocessing.Pool() as pool:
                pool.starmap(checker, [(subdomain, report_name) for subdomain in subdomains])
    except KeyboardInterrupt:
        quit()

# Start processing subdomains
process_subdomains(domain, report_name)
print('[-] Cloud Killer is closed !! ')
