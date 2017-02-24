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
      
def main(execmd,ip='30.30.32.3'): 
    hostname = ip
    #print hostname
    port = 22 
    username = 'root'  
    password = 'FxData!Cds@2016_'  
    #execmd = "/home/icache/icached debug"  
    return sshclient_execmd(hostname, port, username, password, execmd)  
     
      
if __name__ == "__main__":  
    execmd = "/home/icache/icached debug"
    ipaddr='192.168.1.104'
    main(execmd)  
    main(execmd,ipaddr)
    #print 'success'

