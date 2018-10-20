#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Sat Oct 20 20:34:29 2018
#========================================
import os, yaml, subprocess
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def main():
    '''
    '''
    data = dict()
    with open('D:/config.yaml', 'r') as f:
        data = yaml.load(f)
    
    _env = os.environ.copy() #- ENV_NAME:ENV_VALUE
    for e in data['Env']:
        if e['mode'] == 'over':
            _env[e['name']] = e['value']
        
        elif e['mode'] == 'pre': #- Env_name: v1;v2;v3
            _env[e['name']] = e['value'] + ';' + os.environ.get(e['name'], '')
        
        elif e['mode'] == 'post':
            _env[e['name']] = os.environ.get(e['name'], '') + ';' + e['value']
        
        else:
            pass
    
    #- Popen, call, check_call, check_output
    subprocess.call(data['Exec'], env=_env)


main()