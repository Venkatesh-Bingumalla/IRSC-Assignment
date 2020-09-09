# IRSC-Assignment -Scheduling API
This involves a single endpoint, which accepts Date-Time and url as a parameters(atmost two arguments)
Ex. 127.0.0.1:8000/Schedule1/2020-9-9 11:50:89/www.hero.com
Based on the argument Date-Time Reacived if it matches with current Date-Time Then a get request is sent to the url which is the second parameter from API It returns Status code
Along with this when the API sent a get request as '/ping' the server must return a JSON as '{"status":"OK"}'
 
