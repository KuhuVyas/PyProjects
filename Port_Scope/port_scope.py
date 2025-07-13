from socket import *
import time

if __name__ == '__main__':
    startTime = time.time()

    target = input('Enter the host to be scanned: ')
    try:
        t_IP = gethostbyname(target)
        print('Starting scan on host:', t_IP)
    except Exception as e:
        print(f"Host resolution error: {e}")
        exit()

    ports_to_scan = [80, 443, 22, 135, 445, 3306]  # common open ports
    for port in ports_to_scan:
        try:
            s = socket(AF_INET, SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((t_IP, port))
            if result == 0:
                print(f'Port {port}: OPEN')
            else:
                print(f'Port {port}: CLOSED')
            s.close()
        except Exception as e:
            print(f"Error on port {port}: {e}")

    print('Scan complete.')
    print('Time taken:', round(time.time() - startTime, 2), 'seconds')
