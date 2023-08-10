import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='34.204.50.9', username='centos', key_filename=r"C:\Users\jaro9\Downloads\vprofile-ci-key.pem")
# stdin,stdout,stderr=ssh.exec_command("free -m")
# print(stdout.readlines())
# ssh.close()

ftp_client = ssh.open_sftp()
ftp_client.put("access_logs.txt", "access_logs")
ftp_client.get("access_logs", "access_logs.txt")
ftp_client.close()