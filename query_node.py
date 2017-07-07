'''
Created on Jul 6, 2017

@author: robertLackey
'''
from orionsdk import SwisClient
import getpass
import simplejson as json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests

npm_server = 'localhost'

class NodeManager():
    def __init__(self, username, password):
        self.swis = SwisClient(npm_server, username, password, verify=False)
        
    def query(self):
        print("Query Test:")
        results = self.swis.query("SELECT  DisplayName, NodeID, IPAddress FROM Orion.Nodes")
        
        #number variable to display number of nodes in list
        Number = 1
        Spacer = " : "
        #Print query results and making it more readable
        for row in results['results']:
            ##using Json to format query
            print str(Number) + Spacer + json.dumps(row, sort_keys=True, indent=4,
                                                    separators=(',',':'))
            Number += 1
        
def main():
    username = raw_input('Username: ')
    password = getpass.getpass()

    # Initialize the NodeManager class
    nm = NodeManager(username, password)
    #disable certificate warning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    
    nm.query()
        
if __name__ == '__main__':
    main()
