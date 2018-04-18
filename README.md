# PlagiarismCheck
Python script that uses FAROO Web Search API to detect plagiarism<br/>
Register for FAROO API key <a href="http://www.faroo.com/hp/api/api.html">here</a> <br/>
The script divides the document into n words subtrings. <br/>
Each substring are sent to FAROO Web Search API as a query.<br/>
Plagiarism is checked into returned result from Faroo.<br/>
The final plagiarism % is calculated using the formula - <br/>
(no of plagiarized subs/ total no of subs)*100
