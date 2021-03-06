# This class reads in user defined settings for AWS access
# Jonathan Varkovitzky
# May 17, 2012

class user_info:
    def __init__(self):
        #put the *.pem file you wish to use, without the .pem extension
        self.pem_file = 'research'
        #put the name of the secruity group you want to use (must be already setup on AWS)
        self.security_group = 'sshHTTPallowed'
        #select the bucket from which to pull or upload data
        self.topo_bucket = 'cc_topos'
        self.output_bucket = 'cc_output'
        self.product_bucket = 'cc_products'
        #Define which driver file to use for the simulation
        self.driver_file = 'Driver_Test.csv'
