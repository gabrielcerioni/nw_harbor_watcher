__author__ = "Gabs - CSE Team"
__credits__ = ["Gabriel Cerioni"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Gabriel Cerioni"
__email__ = "gacerioni@gmail.com"
__status__ = "Internal"

import os
import requests
import logging
from urllib3.exceptions import InsecureRequestWarning


# Configs (if this gets bigger, I'll provide a config file... or even Hashicorp Vault)
# logging.basicConfig(filename='gabs_graphql.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


HARBOR_USER = os.environ.get('HARNESS_HARBOR_USER')
HARBOR_PWD = os.environ.get('HARNESS_HARBOR_PWD')
HARBOR_REACHABLE_DNS = "https://ec2-18-228-170-187.sa-east-1.compute.amazonaws.com"
HARBOR_REPO = "nationwide/nginx"

 


def endpoint_builder(repo, dns):
    return "{0}/v2/{1}/tags/list".format(dns, repo)


def get_repo_tags(url):
    r = requests.get(url, auth=(HARBOR_USER, HARBOR_PWD), verify=False)

    return r.content


if __name__ == '__main__':
    
    harbor_full_endpoint = endpoint_builder(HARBOR_REPO, HARBOR_REACHABLE_DNS)
    response = get_repo_tags(harbor_full_endpoint)
    logging.info("Artifacts Currently Available on {0} repo: --- {1}".format(HARBOR_REPO, response))
