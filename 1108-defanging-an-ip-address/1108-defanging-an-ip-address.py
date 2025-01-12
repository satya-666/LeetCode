class Solution(object):
    def defangIPaddr(self, address):
        output_string = address.replace(".", "[.]")
        return(output_string)
        