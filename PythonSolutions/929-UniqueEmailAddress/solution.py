# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        # Run through the list and pick an email
        # Split it on @ into local_name and domain_name
        # if local name has dots, remove them updat the local name
        # if local name has + then split by + and remove everything after +
        # now you get final local name, join it with domain name and store it in hash table
        # return the count of this freq hash table
        unique_emails = {}
        
        for email in emails:
            email = self.final_email(email)
            if email not in unique_emails:
                unique_emails[email] = 1
        
        return len(unique_emails)
    
    def final_email(self, email):
        local_name, domain_name = email.split("@")
        
        local_name = local_name.split("+")[0]
        local_name = local_name.replace(".", "")
        
        
        return local_name + "@" + domain_name
        
        

# In a single function:

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        email_count = 0
        unique_emails = {}
        
        
        for email in emails:
            local_name, domain_name = email.split("@")
            local_name = local_name.replace(".", "")
            if "+" in local_name:
                local_name = local_name.split("+")[0]
            
            final_email = local_name + "@" + domain_name
            if final_email not in unique_emails:
                unique_emails[final_email] = 1
        
        return len(unique_emails)
            
            
