
# Logincracker
This is a python programm using your passlist and userlist and random User-Agent generation to BRUTE-FORCE a for example login.php webpage.
Installation:
```ruby
pip install -r requirements.txt
```
usage:

Go to file '/lib/worldists/' and insert your username_list and your password_list into the two existing files after removing the hint.

```ruby
python gather_login.py [URL] [USERINDEX] [PASSWORDINDEX]
```

USERINDEX = value for variable 'name' in the Username-input
![1](https://user-images.githubusercontent.com/73026669/111144931-00c6b100-8588-11eb-88e0-9c701d3eae43.PNG)



PASSWORDINDEX = value for variable 'name' in the Password-input
![2](https://user-images.githubusercontent.com/73026669/111144934-015f4780-8588-11eb-9ffd-76f1a9ff2b2e.png)

After success the login-data will be saved at '/lib/Results/cracked.txt'.

# DISCLAIMER: THIS IS FOR EDUCATIONAL PURPOSES ONLY! 
# NO LIABILITY FOR ILLEGAL USE IS ASSUMED!

[![Build Status](https://user-images.githubusercontent.com/73026669/110617122-9c75ad00-8195-11eb-9ba5-422356072776.png)](https://github.com/LukeProducts)



© Copyright by LukeProducts




