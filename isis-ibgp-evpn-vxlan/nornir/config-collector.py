from nornir import InitNornir
from nornir.plugins.tasks import commands, text
from nornir.plugins.functions.text import print_result

nr = InitNornir(config_file="config.yaml")
print(nr.inventory.hosts)

def fetch_running_config(task):
    task.run(task=commands.remote_command,
             command="show running-config"
    )

for result in nr.run(task=fetch_running_config):
    print_result(result)