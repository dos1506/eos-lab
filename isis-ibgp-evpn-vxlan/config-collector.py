from nornir import InitNornir
from nornir.plugins.tasks import commands, text
from nornir.plugins.functions.text import print_result

nr = InitNornir(config_file="nornir/config.yaml")

def fetch_running_config(task):
    task.run(task=commands.remote_command,
             command="""
             enable
             show running-config
             """
    )

result = nr.run(task=fetch_running_config)

for r in result:
    # 'r' contains hostname
    with open(f"config/{r}.conf", "w") as f:
        # you can access the results by result['hostname']
        f.write('\n'.join(result[r][1].result.splitlines()[3:]))