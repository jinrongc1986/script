import paramiko  
  
def sshclient_execmd(hostname, port, username, password, execmd):  
    paramiko.util.log_to_file("paramiko.log")  
      
    s = paramiko.SSHClient()  
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
      
    s.connect(hostname=hostname, port=port, username=username, password=password)  
    stdin, stdout, stderr = s.exec_command (execmd)  
    stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.  
    #print stdout.read() 
    output= stdout.read()  
    s.close()  
    return output 
      
def main(querycmd,execmd,ip='30.30.32.3'): 
    hostname = ip
    #print hostname
    port = 22 
    username = 'root'  
    password = 'FxData!Cds@2016_'
    if ip=='30.30.33.3':
        password = '123'
    query_result=sshclient_execmd(hostname, port, username, password, querycmd)
    iptable_restart='service iptables restart'
    if '3306' not in query_result:
        sshclient_execmd(hostname, port, username, password, execmd)
        sshclient_execmd(hostname, port, username, password, iptable_restart)


if __name__ == "__main__":  
    querycmd="cat /etc/sysconfig/iptables"
    execmd = "sed -i '6i -A INPUT -s 30.30.32.0/24 -p tcp -m state --state NEW -m tcp --dport 3306 -j ACCEPT' /etc/sysconfig/iptables"
    ipaddr=['192.168.1.104','192.168.1.106','30.30.32.3','30.30.33.3'] 
    for ip in ipaddr:
	print ip
        main(querycmd,execmd,ip)
