# Inquisitor

Python library to convert network outputs to structured JSON data. 

## Usage
Create a virtual env
```python
python3.6 -m venv .venv
```

## Activate Virtual Env
``` 
source .venv/bin/activate
```

## Install Inquisitor
```python
pip install https://github.com/bobthebutcher/inquisitor/archive/master.zip
```

### NetworkToCode TextFSM Templates
Leverage NetworkToCode TextFSM template repository
[ntc-tempaltes](https://github.com/networktocode/ntc-templates)

```
git clone https://github.com/networktocode/ntc-templates.git
```

## Usage
```python
from inquisitor.constants import CISCO_IOS_TEMPLATE_MAP
from inquisitor.api import data_dict


vrf_data = '''
  Name                             Default RD            Protocols   Interfaces
  MGMT                             <not set>             ipv4        Gi0/0
  test-vrf                         65000:100             ipv4        Gi0/1
'''

data_dict(template=CISCO_IOS_TEMPLATE_MAP['vrfs'], data_type='vrfs', raw_data=vrf_data)

{'vrfs': [{'name': 'MGMT',
   'default_rd': '<not set>',
   'protocols': 'ipv4',
   'interfaces': ['Gi0/0']},
  {'name': 'test-vrf',
   'default_rd': '65000:100',
   'protocols': 'ipv4',
   'interfaces': ['Gi0/1']}]}
```


