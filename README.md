# PasswordList

This code parses through a file with a focus on creating a list of potential unencrypted passwords with the following parameters:

1. This code snippet searches for specific user-defined leading words, such as <data>, <password>, or <key>, preceding the password entry in the plist file. If any of these leading words are found, the corresponding password is extracted and processed further.

2. A condition where the length of a password is less than or equal to 16, this effectively filters out encrypted passwords from the list. This criterion helps to eliminate noise or irrelevant data, ensuring that only passwords meeting the specified length criteria are considered for further analysis or processing.

To customize the code for specific purposes, users are advised to modify the following information according to their requirements:
  - line 5: for the name of the file that will parsed (ie. plist)
  - line 25: for the leading word of passwords in the list
