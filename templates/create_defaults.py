import re

try:
    with open('server.conf', 'r') as f:
        server_conf = f.readlines()
except:
    server_conf = None


if server_conf:
    for line in server_conf:
        line = line[:-1]
        if re.match(r'^.*\s+=\s+.*', line) is not None:
            key, value = line.split(' = ')
            if '#' not in key:
                print '{key}: {value}'.format(key=key, value=value)
            else:
                print '{key}:'.format(key=key.replace('#', ''))
            # key = key.replace('#', '')
            # print '{{% if {key} %}}\n{key} = {{{{ {key} }}}}\n{{% else %}}\n# {key} = {value}\n{{% endif %}}'.format(key=key, value=value)
           
            # if '#' in key:
            #   key = key.repace('#', '')
            #   print '{{% if {key} %}}\n{key} = {value}\n{{% endif %}}\n'.format(key=key, value=value)

