import re

log_file = 'test-task/openssh.log'
user = 'root' # Можно указать любого пользователя

dict_sshd = {} # Словарь, где каждым ключем является sshd, а значением - список из логов принадлежащих одному процессу sshd

with open(log_file, 'r') as f:
    for row in f:
        if "sshd" in row:
            sshd_search = re.search(r'sshd\[(\d+)\]', row)
            if sshd_search:  
                sshd = sshd_search.group(1) # Извлекаем из строки номер sshd

            if sshd not in dict_sshd:
                dict_sshd[sshd] = [] # Если ключа еще не существует, то создаем его и присваем ему пустой список

            dict_sshd[sshd].append(row.strip()) 


attempts_by_ip = {} # Словарь для хранения количества неудачных попыток по каждому ip


for sshd_id, logs in dict_sshd.items(): 
    ip = None
    found_authentication_failure = None
    found_failed_password = None
    message_repeated = None

    for row in logs: # Проверяем каждый лог в рамках одного sshd
        if 'pam_unix(sshd:auth)' in row and 'authentication failure' in row and f'user={user}' in row: 
            found_authentication_failure = True

        if f'Failed password for {user}' in row:
            found_failed_password = True

        ip_search = re.search(r'(\d+\.\d+\.\d+\.\d+)', row)
        if ip_search:
            ip = ip_search.group(1)

        if 'message repeated' in row: # Если есть повторения 
            repeat_search = re.search(r'(\d+) times:', row)
            if repeat_search:
                message_repeated = int(repeat_search.group(1))
        
    if found_authentication_failure and found_failed_password and ip:   # Если в рамках sshd процесса были найдены неудачные попытки для пользователя
        if ip in attempts_by_ip:
            attempts_by_ip[ip] += 1
        else:
            attempts_by_ip[ip] = 1

        if message_repeated: 
            attempts_by_ip[ip] += message_repeated

print(attempts_by_ip)