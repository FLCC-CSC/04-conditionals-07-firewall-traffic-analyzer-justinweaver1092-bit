# FILE NAME - firewall_traffic_analyzer.py

# NAME: Justin Weaver
# DATE: 10/3/25
# BRIEF DESCRIPTION:  firewall_traffic_analyzer 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
print('=== Network Traffic Security Analyzer ===')
print()
port_num=(int(input('Enter the port number (e.g., 80, 22, 443, 3389): ')))
data_size=(int(input('Enter the data transfer size in megabytes (MB): ')))
print('FIREWALL LOG:')
print(f'Port: {port_num}, Transfer Size: {data_size} MB')

if port_num == 443:
    print('Risk Assessment: LOW RISK: Secure encrypted transfer detected.') 

elif port_num == 80 and data_size > 100:
    print ("Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.")

elif port_num == 22 or port_num == 3389 and data_size <= 100:
    print ("Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!")

else:
    print("Risk Assessment: UNKNOWN: Unrecognized traffic pattern.")

print('------------------------')







########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 80
Enter the data transfer size in megabytes (MB): 120

FIREWALL LOG:
Port: 80, Transfer Size: 120 MB
Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 22
Enter the data transfer size in megabytes (MB): 12

FIREWALL LOG:
Port: 22, Transfer Size: 12 MB
Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 443
Enter the data transfer size in megabytes (MB): 1024

FIREWALL LOG:
Port: 443, Transfer Size: 1024 MB
Risk Assessment: LOW RISK: Secure encrypted transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 1725
Enter the data transfer size in megabytes (MB): 234567

FIREWALL LOG:
Port: 1725, Transfer Size: 234567 MB
Risk Assessment: UNKNOWN: Unrecognized traffic pattern.
------------------------
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Did you get tripped up using the `or` or `and` operators? If so, how?

Not so much with the 'or' or the 'and' they kinda fit in naturally where they would in normal speech.
I mainly got tripped up with the 3389 because no where in the lab description did it mention 3389.
And then the order of it 'if' and the 'elif'. I oringally had it in high, med, and low risk order. But then realized it kept shorting circiting when enter a port of 443. 
After that it was a lot of just getting the outputs to match up correctly. 





'''
